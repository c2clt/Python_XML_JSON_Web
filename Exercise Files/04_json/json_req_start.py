# using the requests library to access internet data

#import the requests library
import requests
import json


def main():
    # Use requests to issue a standard HTTP GET request
    url = "http://httpbin.org/json"
    result = requests.get(url)

    # TODO: Use the built-in JSON function to return parsed data
    dataobj = result.json()
    print(json.dumps(dataobj, indent=4))
    # TODO: Access data in the python object
    print(list(dataobj.keys()))

    print(dataobj['slideshow']['title'])
    print(f"There are {len(dataobj['slideshow']['slides'])} slides")
if __name__ == "__main__":
    main()
