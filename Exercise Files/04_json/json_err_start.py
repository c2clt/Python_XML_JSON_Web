# Process JSON data returned from a server

# use the JSON module
import json
from json import JSONDecodeError

def main():
    # define a string of JSON code
    jsonStr = '''{
            "sandwich" : "Reuben",
            "toasted" : true,
            "toppings" : [
                "Thousand Island Dressing",
                "Sauerkraut",
                "Pickles"
            ],
            "price" : 8.99
        }'''

    # parse the JSON data using loads
    data = None
    try:
        data = json.loads(jsonStr)
    except JSONDecodeError as err:
        print("Whoops, JSON decoding error:")
        print(err.msg)
        print(f"Line number: {err.lineno}", f"Col number: {err.colno}")

    # print information from the data structure
    if data:
        print("Sandwich: " + data['sandwich'])
        if (data['toasted']):
            print("And it's toasted!")
        for topping in data['toppings']:
            print("Topping: " + topping)


if __name__ == "__main__":
    main()
