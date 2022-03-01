# using the requests library to access internet data

import requests
from requests.auth import HTTPBasicAuth

def main():
    # Access a URL that requires authentication - the format of this 
    # URL is that you provide the username/password to auth against
    url = "http://httpbin.org/basic-auth/jessica/secretword"

    # TODO: Create a credentials object using HTTPBasicAuth
    # myCreds = HTTPBasicAuth("Jessica", "Secretword")
    # myCreds = HTTPBasicAuth("jessica", "secretword")
    # TODO: Issue the request with the authentication credentials
    # auth tuple instead of myCreds
    result = requests.get(url, auth=("jessica", "secretword"))
    printResults(result)
    

def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Returned data: ----------------------")
    print(resData.text)

if __name__ == "__main__":
    main()
