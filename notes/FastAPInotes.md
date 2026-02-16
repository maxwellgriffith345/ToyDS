#FastAPI notes

## Questions
- what is fast API
- what is Flask
- how do I use fastAPI and Flask together
- I need a thrid thing to actually run the FastAPI?
- what is an API?
- what is ASGI Asynchronous Server Gateway Interface?
- What are Websockets?
- what is HTTP
- what is a gateway?
- what is an API endpoint?

-FastAPI is a python web framework optimized for high performance APIs
-FastAPI defines the web app structure
  - the what and how for requests
  - how to route reuqests and what to do with them
- It needs a web server to actually run the app and handle requests
  - Uvicorn

## What is an API
[Amazon What is An API](https://aws.amazon.com/what-is/api/)
- Protocol that allows to software components to pass data between each other
- Application Programming Interface
  - application is any software with a distint function
  - interface is the rules/contract that defines how to applications communicate
  - use reqeusts and responses
- One app is the "client" and the other is the "server"
  - the app making requests is the client
  - the app sending the response is the server
- 4 ways APIs can work, focus on REST APIs

## REST APIs
- most popular and flexible API on the web today
- high level: client sends request to the server, the serve uses the request input to run internal functsion to return the output data
- Representational State Transfer
- REST defines functions that clients use to access server data
- GET, PUT, DELETE etc
- data is exchanged using HTTP
- REST API is stateless
  - servers do not save client data between requests
- Client reuqests are formatted like URLs
- Server responses are plain data, no graphical rendering like a web page
-  API endpoint
-  

## FastAPI docs Notes
[FastAPI tutorial](https://fastapi.tiangolo.com/python-types/)

### PreRec: Python Types "Type Hints"
- declare the type of a variable
- FastAPI relies heavly on type hints
- use typehints when declaring function parameters
``` python
def your_function( var1: str, var2: int):
    do something
```
- helps with autocomplete the IED knows what to look for
- Data structures list, tuple, set, dict can be typed when declared as a function parameter
- define a variable that is a list of strings list[str]
- here 'str' inside the list is called a "type parameter"
- for typed dict you pass two parameters one for the keys and one for the values
``` python
#list
def you_func(items: list[str]):
  for item in items: print(item)

#tuple
def your_func(items_t: typle[int,int,str], name: str):
  do something

# dict
# keys are strings, values are float
def your_func(prices: dict{str, float]):
  do something
```
- Can also declare a class as a type
``` python
class Person:
  def __init__(self, name: str):
    self.name = name

#one_person is an instance of class Person
def get_person_name(one_person: Person):
    return one_person.name
```
-Pydantic is a library to do data validation (type validation)
- Create a class with typed attributes
- when you create an instance of that class and initilizae the attributes Pydantic will make sure they are the right type and convert if needed
``` python
from pydantic import BaseModel

#define a 'User" class and inherite BaseModel
# set the types of the attributes
class User(BaseModel:
    id: int
    name: string

# data to create an instances of User
new_data = { "id": "123", "name": "John Doe"}

#create the instance
user = User(**new_data)
```
- FastAPI is all based on Pydantic
- When declaring parameters with type hints you get:
  - Editor Support
  - Type Checks
- FastAPI uses the type declarations to
  - define requirements: request path params, query params, headers, bodies, dependencies
  - convert data: from what was sent in the request to the required type
  - validate data coming from a reuqest
  - document the API
  -  

### PreRec: Concurrency: async and await
