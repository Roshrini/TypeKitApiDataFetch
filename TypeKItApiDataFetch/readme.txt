Write a command line interface in Python to fetch information about your kits using the public Typekit APIs. Start here:
https://typekit.com/docs/api/v1/:format/kits

How to run:
python command_line_interface.py 3d46b16476180c53816ab41c2de0f00b90222759
<Enter token you want to use to fetch kits>

Approach to solve the assignment:

To solve this assignment, I went through documentation of typekit api to get better sense of what I have to do.
For now, My program assumes that the kits are already created. Also I generated a valid token for my account
at "https://typekit.com/account/tokens"

I explored options for libraries to fetch data as "curl" does in python.
There are libraries like pycurl, urllib and I was able to fetch data using pycurl but I found Requests library is best and simplest to use.

Then, I parsed data obtained through requests.get by using json parser. json.loads() gives dictionary. So, I got data in following format
{
  "kits": [
    {
      "id": "ajd4dmw",
      "link": "/api/v1/json/kits/ajd4dmw/"
    },
    {
      "id": "ard8twk",
      "link": "/api/v1/json/kits/ard8twk/"
    }
  ]
}

Then, I getting id and link for each kit was trivial.

I decided to create TypeKitApi class because even if I just had to implement one function, making class, it becomes easier to extend it.
So, if I have to write code for creating kits. I can just add create_kit method in my TypeKitApi class and call
that method from command_line_interface based on the request_method 'GET' or 'POST'

I also wrote error handling code if response obtained from requests.get() is too large. We can adjust parameters
 in the typekit_api file to check that. I made use of body content workflow. Referred link "http://docs.python-requests.org/en/latest/user/advanced/#body-content-workflow"
 By using this, we can read data in chunks and process it and also give friendly error message if response becomes too big to handle.

Testing:

1) For free account, I could only create 1 kit and test my program on it but I ran my program on some dummy data as well.
2) If no kits are there
3) Invalid token entered
4) Gave wrong number of parameters as arguments to program
5) Handling unsuccessful HTTP GET method
6) I made sure to handle all the above boundary cases so that code should be production ready