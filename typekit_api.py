__author__ = 'roshaninagmote'
import sys
import requests
import json
from contextlib import closing

# I am keeping upper limit of the size of data. Can change it according to the requirement.
UPPER_LIMIT =  1024 * 1024 * 1024 * 1024
CHUNK_SIZE = 1024 * 1024

class TypeKitApi:
    # Setting url in init method
    def __init__(self,url):
        self.url = url

    def get_data(self):
        # Redirected to request_kits method
        kits = self.request_kits(self.url)
        return kits

    def request_kits(self,url):
        # Using Requests as HTTP library in python. It has get method for fetching data
        # Reading data in stream to handle big data.
        # Link referred: "http://docs.python-requests.org/en/latest/user/advanced/#body-content-workflow"
        with closing(requests.get(url, stream=True)) as response:
            content_length = 0
            # Handling HTTP error codes
            try:
                response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                print "And you get an HTTPError:", e.message
                sys.exit()

            # Reading data from obtained response in chunks to handle the big size of data
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    content_length = content_length + len(chunk)
                    # Printing error in case the size limit exceeds
                    if content_length > UPPER_LIMIT:
                        print "response was too big to handle"
                        sys.exit()
                    # Processing when response code is 200 = successful
                    elif response.status_code == 200:
                        # Parsing json data. response_load is dictionary
                        response_load = json.loads(chunk)
                        # value corresponding to 'kits' key is list of created kits. It is returned
                        if 'kits' in response_load:
                            response_kits = response_load['kits']
                            return response_kits
                        else:
                            print("kits is not present in fetched data")
                            sys.exit()
