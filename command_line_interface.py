__author__ = 'roshaninagmote'
import sys
import typekit_api

class CommandLineInterface:
    # Setting request method
    def __init__(self, request_method):
        self.request_method = request_method

    def parse(self):
        # Checking number of arguments. If wrong number, print out error and exits the program
        if len(sys.argv) != 2:
            print "Wrong number of arguments"
            print("Usage: python command_line_interface.py \"<valid token>\"")
            sys.exit()

        # Token is accepted from command line argument
        token = sys.argv[1]
        # URL is prepared to fetch data. Referred this link "https://typekit.com/docs/api/auth"
        url = 'https://typekit.com/api/v1/json/kits?token='+token
       # url= 'https://github.com/blackbumer/typekit_cli'
        # Creating typekitapi object to call get_data method. Set url in init method
        typekitapi_obj = typekit_api.TypeKitApi(url)

        # According to the HTTP request method, call get_data from TypeKitApi class
        if self.request_method == 'GET':
            response_kits = typekitapi_obj.get_data()
            # If returned kit data is empty, print no kits created and exit
            if not response_kits:
                print "No kits created yet"
                print "Want to create a new kit? use 'POST' method"
                sys.exit()

            # Itreate through the returned dataset of kits and print kit id and link
            i = 1
            for kit in response_kits:
                print "kit", i, " is  ", kit
                if 'id' in kit:
                    print "kit id is  ", kit['id']
                if 'link' in kit:
                    print "kit link is  ", kit['link'], "\n"
                i += 1

        # This is for method like 'POST', you can use POST to create kits
        else:
            print "Other methods are not implemented in TypeKitApi yet"

def main():
    # Calling command line interface with 'GET' request method.
    CommandLineInterface('GET').parse()

if __name__ == "__main__":
    main()