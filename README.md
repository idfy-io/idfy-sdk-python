# Idfy Python SDK
[![Build Status](https://travis-ci.org/idfy-io/idfy-sdk-python.svg?branch=master)](https://travis-ci.org/idfy-io/idfy-sdk-python) ![PyPI](https://img.shields.io/pypi/v/idfy-sdk.svg)

A Python SDK for simple integration with the Idfy REST API.

Supports Python 3.5 and above. (3.5, 3.6, 3.7)

## Installation
The package is available on PyPI. Use of Pipenv is recommended(https://pipenv.readthedocs.io):

    pipenv install idfy-sdk

Although it's just as easy to install without pipenv:

    pip install idfy-sdk

### External libraries
This SDK was made to use as few external libraries as possible. It uses only the excellent "Requests" module (http://docs.python-requests.org/en/master/) which is probably the most commonly used Python library as of the writing of this document.

## Working on the Code
Developers who want to make changes to the codebase are welcome to do so, but if you want to run the included unit-tests you need to download and run the Idfy mock server (https://github.com/idfy-io/idfy-mock-server). Once the server is up and running, all you have to do is navigate to the root folder of the SDK and type:

    python -m unittest

If you're developing on a Linux-based system, remember to replace "python" with your desired Python interpreter as appropriate.

We know that many of our customers have very talented in-house developers, and we want to encourage our customers to make any changes they want to make the SDK perfectly suit their needs. Please feel free to send any potential questions or suggestions for improvement to our support channels listed below. We appreciate the feedback.




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

## Asynchronous Methods
Using the async methods will make the program no longer run strictly single-threaded. The SDK is also able to make use of some of the features introduced to the asyncio module in Python 3.7, so running the code on that version or later might yield slight improvemets to efficiency and robustness when using async methods.

## Support
- Open an [issue](https://github.com/idfy-io/idfy-sdk-python/issues) to report bugs or submit feature requests.
- For other support requests, visit our [support page](https://support.idfy.io) or contact us at [support@idfy.io](mailto:support@idfy.io).