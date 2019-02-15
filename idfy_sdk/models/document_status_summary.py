# Users of the SDK should ideally never have to modify, or even look at,  these models.
import pprint
import re  

import six


class DocumentStatusSummary(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'document_status': 'str',
        'completed_packages': 'list[str]',
        'attachment_packages': 'dict(str, list[str])'
    }

    attribute_map = {
        'document_status': 'documentStatus',
        'completed_packages': 'completedPackages',
        'attachment_packages': 'attachmentPackages'
    }

    def __init__(self, document_status=None, completed_packages=None, attachment_packages=None):  
        """Status"""  

        self._document_status = None
        self._completed_packages = None
        self._attachment_packages = None
        self.discriminator = None

        if document_status is not None:
            self.document_status = document_status
        if completed_packages is not None:
            self.completed_packages = completed_packages
        if attachment_packages is not None:
            self.attachment_packages = attachment_packages

    @property
    def document_status(self):
        """Gets the document_status of this Status.  

        The overall status of the document.  

        :return: The document_status of this Status.  
        :rtype: str
        """
        return self._document_status

    @document_status.setter
    def document_status(self, document_status):
        """Sets the document_status of this Status.

        The overall status of the document.  

        :param document_status: The document_status of this Status.  
        :type: str
        """
        allowed_values = ["unsigned", "waiting_for_attachments", "partialsigned", "signed", "canceled", "expired"]  
        if document_status not in allowed_values:
            raise ValueError(
                "Invalid value for `document_status` ({0}), must be one of {1}"  
                .format(document_status, allowed_values)
            )

        self._document_status = document_status

    @property
    def completed_packages(self):
        """Gets the completed_packages of this Status.  

        A list of all the completed files/packages for the main document.  

        :return: The completed_packages of this Status.  
        :rtype: list[str]
        """
        return self._completed_packages

    @completed_packages.setter
    def completed_packages(self, completed_packages):
        """Sets the completed_packages of this Status.

        A list of all the completed files/packages for the main document.  

        :param completed_packages: The completed_packages of this Status.  
        :type: list[str]
        """
        allowed_values = ["unsigned", "native", "standard_packaging", "pades", "xades"]  
        if not set(completed_packages).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `completed_packages` [{0}], must be a subset of [{1}]"  
                .format(", ".join(map(str, set(completed_packages) - set(allowed_values))),  
                        ", ".join(map(str, allowed_values)))
            )

        self._completed_packages = completed_packages

    @property
    def attachment_packages(self):
        """Gets the attachment_packages of this Status.  

        A set of key-value pairs with all the completed packages for the signable attachments, where the key is equal to the attachment's ID.  

        :return: The attachment_packages of this Status.  
        :rtype: dict(str, list[str])
        """
        return self._attachment_packages

    @attachment_packages.setter
    def attachment_packages(self, attachment_packages):
        """Sets the attachment_packages of this Status.

        A set of key-value pairs with all the completed packages for the signable attachments, where the key is equal to the attachment's ID.  

        :param attachment_packages: The attachment_packages of this Status.  
        :type: dict(str, list[str])
        """
        #allowed_values = ["unsigned", "native", "standard_packaging", "pades", "xades"]  
        #if not set(attachment_packages.keys()).issubset(set(allowed_values)): #I have to test the values instead of the keys (which are attachemnt-ids) here?
        #    raise ValueError(
        #        "Invalid keys in `attachment_packages` [{0}], must be a subset of [{1}]"  
        #        .format(", ".join(map(str, set(attachment_packages.keys()) - set(allowed_values))),  
        #                ", ".join(map(str, allowed_values)))
        #    )

        self._attachment_packages = attachment_packages

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DocumentStatusSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
