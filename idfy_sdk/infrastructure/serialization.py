import datetime
import json   
import re
import six

import idfy_sdk.models

PRIMITIVE_TYPES = (float, bool, bytes, six.text_type) + six.integer_types
NATIVE_TYPES_MAPPING = {
    'int': int,
    'long': int,
    'float': float,
    'str': str,
    'bool': bool,
    'date': datetime.date,
    'datetime': datetime.datetime,
    'object': object,
}


def deserialize(response, response_type=None):
    """
    Deserializes response into an object.
    """
    # handle file downloading
    # save response body into a tmp file and return the instance
    if response_type == "file":
        return __deserialize_file(response)


    # fetch data from response object
    try:
        data = response.json()
    except ValueError:
        data = response.text
    
    if response_type is None: return json.dumps(data)   # Sometimes It's not fetching complex objects.

    return __deserialize(data, response_type)

def __deserialize(data, klass):
    """
    Deserializes dict, list, str into an object.
    """
    if data is None:
        return None

    if type(klass) == str:
        if klass.startswith('list['):
            sub_kls = re.match('list\[(.*)\]', klass).group(1)  #pylint: disable=W1401
            return [__deserialize(sub_data, sub_kls)
                    for sub_data in data]

        if klass.startswith('dict('):
            sub_kls = re.match('dict\(([^,]*), (.*)\)', klass).group(2) #pylint: disable=W1401
            return {k: __deserialize(v, sub_kls)
                    for k, v in six.iteritems(data)}

        # convert str to class
        if klass in NATIVE_TYPES_MAPPING:
            klass = NATIVE_TYPES_MAPPING[klass]
        else:
            klass = getattr(idfy_sdk.models, klass)

    if klass in PRIMITIVE_TYPES:
        return __deserialize_primitive(data, klass)
    elif klass == object:
        return __deserialize_object(data)
    elif klass == datetime.date:
        return __deserialize_date(data)
    elif klass == datetime.datetime:
        return __deserialize_datatime(data)
    else:
        return __deserialize_model(data, klass)

def __deserialize_primitive(data, klass):
    """
    Deserializes string to primitive type.
    """
    try:
        return klass(data)
    except UnicodeEncodeError:
        return six.u(data)
    except TypeError:
        return data

def __deserialize_object(value):
    """
    Just return the value if it's an object.
    """
    return value

def __deserialize_date(string):
    """
    Deserializes string to date.
    """
    try:
        from dateutil.parser import parse
        return parse(string).date()
    except ImportError:
        return string
    #except ValueError:
    #    raise rest.ApiException(
    #        status=0,
    #        reason="Failed to parse `{0}` as date object".format(string)
    #    )

def __deserialize_datatime(string):
    """
    Deserializes string to datetime.

    The string should be in iso8601 datetime format.
    """
    try:
        from dateutil.parser import parse
        return parse(string)
    except ImportError:
        return string
    #except ValueError:
    #    raise rest.ApiException(
    #        status=0,
    #        reason=(
    #            "Failed to parse `{0}` as datetime object"
    #            .format(string)
    #        )
    #    )

def __deserialize_model(data, klass):
    """
    Deserializes list or dict to model.
    """

    if not klass.swagger_types and not hasattr(klass,
                                                'get_real_child_model'):
        return data

    kwargs = {}
    if klass.swagger_types is not None:
        for attr, attr_type in six.iteritems(klass.swagger_types):
            if (data is not None and
                    klass.attribute_map[attr] in data and
                    isinstance(data, (list, dict))):
                value = data[klass.attribute_map[attr]]
                kwargs[attr] = __deserialize(value, attr_type)

    instance = klass(**kwargs)

    if hasattr(instance, 'get_real_child_model'):
        klass_name = instance.get_real_child_model(data)
        if klass_name:
            instance = __deserialize(data, klass_name)
    return instance

def __deserialize_file(response):
    """Deserializes body to file 

    More specifically it just returns a pointer to the binaty content
    of the response so the user can decide what do do with the data.
    """

    return response.content

def serialize(obj):
    """Builds a JSON POST object.

    If obj is None, return None.
    If obj is str, int, long, float, bool, return directly.
    If obj is datetime.datetime, datetime.date
        convert to string in iso8601 format.
    If obj is list, calls itself on each element in the list.
    If obj is dict, return the dict.
    If obj is a model, return the properties dict.
    """
    if obj is None:
        return None
    elif isinstance(obj, PRIMITIVE_TYPES):
        return obj
    elif isinstance(obj, list):
        return [serialize(sub_obj)
                for sub_obj in obj]
    elif isinstance(obj, tuple):
        return tuple(serialize(sub_obj)
                        for sub_obj in obj)
    elif isinstance(obj, (datetime.datetime, datetime.date)):
        return obj.isoformat()

    if isinstance(obj, dict):
        obj_dict = obj
    else:
        # Convert model obj to dict except
        # attributes `swagger_types`, `attribute_map`
        # and attributes which value is not None.
        # Convert attribute name to json key in
        # model definition for request.
        obj_dict = {obj.attribute_map[attr]: getattr(obj, attr)
                    for attr, _ in six.iteritems(obj.swagger_types)
                    if getattr(obj, attr) is not None}

    return {key: serialize(val)
            for key, val in six.iteritems(obj_dict)}

