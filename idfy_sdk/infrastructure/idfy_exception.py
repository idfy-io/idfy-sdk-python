from idfy_sdk.infrastructure.serialization import deserialize

class IdfyException(Exception): #TODO
    """
    Do I write the mappings for all the different values that I might expect from the Error object
    in IdfyError (as optional parameters), and interate over them in the constructor of Idfy Exception;
    removing all the ones that are None and creating member data dynamically that way?
    """
    def __init__(self, response):
        self.message = "This is an Idfy exception"
        self.data = None
        self.raw_data = response.content
        self.unicode_data = response.text

        try:
            #data = deserialize(response, 'IdfyError') #IdfyError has not yet been created
            self.data = response.json()
        except ValueError:
            print("The Error object in the response could not be deserialized.")
            #data = None
        else:
            self.message = self.data

        super().__init__(self.message)