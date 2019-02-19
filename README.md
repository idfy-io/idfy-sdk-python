# Idfy Python SDK
[![Build Status](https://travis-ci.org/idfy-io/idfy-sdk-python.svg?branch=master)](https://travis-ci.org/idfy-io/idfy-sdk-python)

A Python SDK for simple integration with the Idfy REST API.

Supports Python 3.5 and above. (3.5, 3.6, 3.7)

Using the async methods will make the program no longer run strictly single-threaded. The SDK is also able to make use of some of the features introduced to the asyncio module in Python 3.7, so running the code on that version or later will yeald slight improvemets to efficiency and robustness when using async methods.

## Installation
The package is available on PyPI. Use of Pipenv is recommended(https://pipenv.readthedocs.io).

    pipenv install idfy-sdk-python



## Documentation
- [Idfy REST API Reference](https://developer.idfy.io/api)
- [Idfy Developer Documentation](https://docs.idfy.io)


## Sample Usage
The example below shows how to get the details of a specific document.

```python
# Import the SDK into your module
import idfy_sdk

# Set your credentials and desired scopes
idfy_sdk.IdfyConfiguration.set_client_credentials("Your client ID here", "Your client secret here", ["A list containing all your desired scopes (see documentation)"])

# Make a call to retrieve the document
service = idfy_sdk.services.SignatureService()

document_info = service.get_document(document_id)

print(document_info)
```

## Support
- Open an [issue](https://github.com/idfy-io/idfy-sdk-python/issues) to report bugs or submit feature requests.
- For other support requests, visit our [support page](https://support.idfy.io) or contact us at [support@idfy.io](mailto:support@idfy.io).