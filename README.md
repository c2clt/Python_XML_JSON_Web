## XML
* Extensible Markup Language and related technologies
* Similar to HTML with some changes to better suit general data
* Rich and expressive but more complex than JSON
* Format rules:
    * XML documents must always have a single root tag
    * XML documents can have an optional document declaration
    * Empty tags must have a closing slash: <tag />
    * Attributes must have values that are enclosed in quotes
    * Tags must be properly nested within each other
    * Tags and attributes starting with "xml" are reserved

    ```xml
    <sandwich>
        <name>Reuben</name>
        <bread type="rye" toasted="true" />
        <contents>
            <item name="corned beef" />
            <item name="sauerkraut" />
            <item name="Swiss cheese" />
            <dressing name="Russian" />
        </contents>
        <side-item name="pickle" />
        <price currency="usd">8.99</price>
    </sandwich>
    ```

## JSON: JavaScript Object Notation
* Very concise format for serializing object data
* Derived from JavaScript but supported by most modern languages
* Compact and easy to read, write and process
* Data type:
    * Number: Signed decimal number, no Integer/Float distinction
    * String: Unicode or escaped characters inside double quotes
    * Boolean: Tre or  False value
    * Null: Null value
    * Array: List of ordered values
    * Object: Collection of key-value pairs, keys are strings

    ```json
    {
        "filename" : "JSON example file",
        "version" : 2.0,
        "is_example" : true,
        "linked_file" : null,
        "array" : [1, 2, 3, "4.0"],
        "obj" : {
            "key1" : 1,
            "key2" : ["a", "b", "c"]
        }
    }
    ```

## platform and language independent
* XML and JSON are both platform and language independent
* e.g. Jave Web Service   **<-- { JSON } or { XML } -->**  Python Client App

## urllib
* contains modules for working with URLs
    * urllib.request
    * urllib.error
    * urllib.parse
    * urllib.robotparser
* retrieving data:
    ```python
    response = urllib.request.urlopen(
        url,
        data=None,
        [timeout, ]*,
        cafile=None,
        capath=None,
        cadefault=False,
        context=None
    )
    ```
    * HTTPResponse Object
        * URL: the URL data was ultimately retrieved from (may have been redirected)
        * status: HTTP status code of result, such as 200 or 404
        * getheader()/getheaders(): Functions for accessing a single header or all headers as a group of 2-tuples
        * read(): Function to read the data from the result
* Sending data to web services
    * GET: retrieve data from a web service
    * POST: Create or update data on a service
    * PUT: Create or update a specific data resource on a web service
    * PATCH:: Perform a partial data update or edit on a web service
    * DELETE: delete data on a web service
* drawbacks of urllib
    * only supports a subset of HTTP by default
    * Doesn't automatically decode retured data
    * Common features, such as cookies or authentication, require more modules
    * difficult to implement advanced features, such as timeout
    * Processing returned data, such as JSON, is cumbersome

## Requests library
https://docs.python-requests.org/en/master/

* Requests: Simple API - each HTTP verb is a method name
* Makes working with parameters, headers, and cookies
* Automatically decodes returned content
* Automatically parses JSON content when detected
* Handle redirects, timeout ans errors
* Advanced features like authentication and sessions
```python
import requests
result = requests.get("http://example.com")
result = requests.put("http://example.com/put", data={"key": "value"})
result = requests.delete("http://example.com/delete")
result = requests.head("http://example.com/head")
result = requests.options("http://example.com/options")
```

* making a simple request (e.g. *response = requests.get(url)*)
    * params: Key-value pairs that will be sent in the query string
    * headers: Dictionary of header values to send along with the request
    * auth: Authentication tuple to enable different forms of authentication
    * timeout: Valur in seconds to wait for the server to respond

## Pthon JSON Functions
* Parsing functions:
    ```python
    obj = load(file)
    obj = loads(string)
    ```
* Serialization functions:
    ```python
    dump(obj, file)
    str = dumps(obj)
    ```
* Serilizing Python (**Python Object**) Data to JSON (**JSON representation**)
    * dict: object
    * list, tuple: array
    * str: string
    * int, long, float, Enums: number
    * True: true
    * False: false
    * None: null

* Parsing JSON (**JSON representation**) into Python (**Python Object**)
    * object: dict
    * array: list
    * string: str
    * Integer number: int
    * Floating point number: float
    * true, false: True, False
    * null: None

## XML Parsing Models
* SAX: simple API for XML
    * Reads entire document start to finish, sequentially
    * Generate events as XML content is encountered
    * Your Python app define a class to handle content events
        ```xml
        <tag attr1="abc" attr2="def">Text Content</tag>
        ```
    * Advantages:
        * Memory efficient - doesn't need to load entire doc
        * Fast - your app only gets events it cares about
        * Easy to implement, simple API
    * Drawbacks:
        * No random access to doc content
        * Context is not passed to parser
        * Cannot modify the XML file
    
    ```python
    # Python SAX API
    import xml.sax

    xml.sax.parse(file, handler)
    xml.sax.parseString(string, handler)
    class xml.sax.ContentHandler

    class MyContentHandler(xml.sax.ContentHandler):
        def __init__(self):
            # member variable go here
        def startDocument(self):
            # Processing starting
        def startElement(self, tagName, attrs):
            # opening tag and attrs have been parsed
        def characters(self, text):
            # member variable go here
    ```

* DOM: Document Object Model
    * DOM API:
        * Access any part of an XML structure at random
        * Modify the XML content
        * Represents the XML as a hierarchical tree structure
        * lightweight implementation: *xml.dom.minodom*
        ```python
        domtree = xml.dom.minidom.parseString(str)

        elem.getElementById(id)
        elem.getElementByTagName(tagname)

        elem.getAttribute(attrName)
        elem.setAttribute(attrName, val)
        elem.appendChild(newElem)
        ```

    * ElementTree API
        * Focuses on being simpler and more efficient than DOM
        * Elements are treated like lists

            ```xml
            <elem>
                <b>foo</b>
                <c>bar</c>
                <d>baz</d>
            </elem>
            ```

            ```python
            for child in elem:
                print(child.tag)
            # results in b, c, d
            ```

        * Attributes are treated like dictionaries
            ```xml
            <tag a="b" c="d">
            ```
        
        * Searching for content inXML is straightforward
            ```python
            elem.findall(queryExpression)

            # queryExpression:
            tagname: find immediate child tagname elements of elem
            //tagname: Find all tagname elements regardless of where they are in the doc
            tagname[attr]: Find all tagname elements that have a specified attribute
            tagname[attr=val]: Find tagname elements that have an attribute with a specific value
            ```
        


 