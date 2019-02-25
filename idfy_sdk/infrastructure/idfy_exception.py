import json

import requests

from idfy_sdk.infrastructure.serialization import deserialize

class IdfyException(Exception): #TODO
    """This is a custom exception defined in the Idfy SDK

    This is the only custom exception in the Idfy SDK, and
    as such it wraps several different types of errors.

    If it's just used to signal a generic error to the user,
    it might just contain an informative message in
    plain-text. In this case the message will be visible in
    'IdfyException.message'.

    it might also contain JSON, in which case the json data
    can be found in 'IdfyException.error'. If the JSON includes
    a 'message', this will be used as the exceptions message.

    In the vast majority of cases this exception will be used
    to wrap error responses from one of our API endpoints. In
    which case it will always contain the raw requests.Response
    object in IdfyException.response, and the status code of
    the response in IdfyException.http_status_code. It will also
    contain:
        - IdfyException.message
        - IdfyException.code
        - IdfyException.error
        - IdfyException.error_description
            -- This is only used by the Oauth endpoint

    If the SDK fails to find/parse any JSON from the response
    it will put the UTF8 encoded data from the response into
    IdfyError.error and try to return as much useful information
    as possible (Note: If this happens your requests are probably
    not reaching one of our endpoints.)
    """
    def __init__(self, data):
        #check if data is Response or str if not raise Exception

        #print(data.status_code)

        #super().__init__(data)

        if isinstance(data, str):
            try:
                self._error_dict = json.loads(data)
                if self._error_dict["message"] is not None:
                    super().__init__(self._error_dict["message"])
                    self.error = self._error_dict
                else:
                    super().__init__("An error occured in the Idfy SDK. Details are in 'IdfyException.error'.")
                    self.error = self._error_dict

            except ValueError:
                super().__init__(data)
                self.message = data
        
        elif isinstance(data, requests.models.Response):
            try:
                if data.text != '':
                    self._error_dict = data.json()

                    if self._error_dict["message"] is not None:
                        self.message = self._error_dict["message"]
                    
                    if self._error_dict["code"] is not None:
                        self.code = self._error_dict["code"]
                    
                    if self._error_dict["error"] is not None:
                        self.error = self._error_dict["error"]
                    
                    if self._error_dict["error_description"] is not None:
                        self.error_description = self._error_dict["error_description"]
                
                    super().__init__("Server returned {}, with message: {}".format(data.status_code, self.message))
                
                else:
                    super().__init__("Server returned {}, with an empty body.(Target probably doesn't exist)".format(data.status_code))

            except ValueError:
                super().__init__("Response did not contain valid JSON (all Idfy endpoints return JSON).{}".format(data.status_code))
                self.error = data.text

            self.response = data    # This might just be fetching the repr of the object, and not a reference to the object itself.

            self.http_status_code = data.status_code
        
        else:
            raise IdfyException("Invalid value returned from http request.")
           