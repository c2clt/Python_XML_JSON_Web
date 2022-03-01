# using the requests library to access internet data

import requests
from requests import HTTPError, Timeout

def main():
    # Use requests to issue a standard HTTP GET request
    try:
        # url = "http://httpbin.org/status/404"
        url = "http://httpbin.org/delay/5"
        result = requests.get(url, timeout=2)
        result.raise_for_status()
        printResults(result)
    except HTTPError as err:
        print(f"Error: {err}")
    except Timeout as err:
        print(f"Request timed out: {err}")    

def printResults(resData):
    print("Result code: {0}".format(resData.status_code))
    print("\n")

    print("Returned data: ----------------------")
    print(resData.text)


if __name__ == "__main__":
    main()
