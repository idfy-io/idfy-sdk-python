#import sys
#This should probably be removed, the script is supposed to be in the Python path if you want to run it
#sys.path.append('E:\Code\Python-SDK\Python-SDK')    # pylint: disable=W1401

import requests

from idfy_sdk import urls as urls
from idfy_sdk.idfy_configuration import IdfyConfiguration as config
from idfy_sdk.services.identification.identification_service import IdentificationService
from idfy_sdk.infrastructure.idfy_exception import IdfyException

config.BaseUrl = urls.TestBaseUrl   #No option to dynamically set the port for the mock server yet.
config.OAuthBaseUrl = urls.TestBaseUrl

config.set_client_credentials("clientId", "clientSecret", ['document_read', 'document_write'])

api_headers = {'X-Idfy-SDK': 'Python This code is still in development.', 'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmb28iOiJiYXIifQ.UIZchxQD36xuhacrJF9HQ5SIUxH5HBiv9noESAacsxU', 'Content-Type': 'application/json'}

try:
    pass
    id_service = IdentificationService() #"identification_clientId", "identification_clientSecret", ['document_read', 'document_write']
    result = id_service.get_session(request_id="1")   #I use a service here in order to fetch a token before the http lib gets patched out.
except(requests.exceptions.ConnectionError) as e:
    raise(requests.exceptions.ConnectionError("Couldn't connect to mock server. Are you sure the mock server is currently running?")) from e
except(Exception) as e:
    raise(IdfyException("An unexpected error occurred while trying to connect to the mock server")) from e

#else:
#    if not result.status_code == 200 :
#        raise(ConnectionError("Conection established, but server is not responding as expected. Do you have something else running on localhost port 5000?"))
