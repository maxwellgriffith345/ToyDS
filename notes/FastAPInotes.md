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
- asynchronous code, coroutines with async and await syntax
- asynchronous code tells the computer/program that it will have to wait for something else to finish ie 'slow-file'
- While the code waits for 'slow-file' it can do other work
- the program will check in and see if the task it was waiting for has finished
- Once it checks and sees 'slow-file' has finished it continues whith what it needed it for
- typical 'slow' tasks to wait on are I/O operations
  - waiting on data from a client
  - waiting on data to send over network
  - write/read something fro disk
  - wait for database query to return results
- The prgoram does not need to be "synchronized" with a slow task
  - isn't not necessary for the program to do nothing while it waits for the exact moment the task finishes
- "synchronous" can be thought of as "sequential"
  - the program follows all the steps in sequence before moving to a different task, even if it has to wait for a task to finish
- Asynchronous code is also called Concurrency
- Asynchronous/Concurrency is different that Parallelism
  - both relate to different things happening at the same time
  - but the details are different
- Concurrent Burgers
  - You order a burger at a counter, the person at the register puts the order in the chefs que, but it takes time to make the burger and recie your order
  - So you don't stand there waiting at the cash register you go and do other tasks; pick out a table, fill your drink etc
  - You check to see if your order number is up while you go about your other tasks
  - Your order number is called out, but you don't get it right away, you first finish getting your drink then go get your burger
  - You burger is a coroutine that you are waiting on but you can still do other things unitl it's ready
- Parallel Burgers
  - There are 8 cashiers who are also the cooks, you order at one register and your crush orders at another
  - The two eomployees take the orders and then go and start cooking your burgers
  - You and your crush wait on the counter until the cook finsish your burgers
  - Your crushes burger is done frist and the employee returns hands it off and your crush goes and sits down
  - You can't leave with her because you are still waiting on your food, then your order is up and you go and sit down and eat
  - Another example: cleaning a big dirty house
  - There isn't much waiting involved but alot of work, so it's better to have 8 cleaners all working at once than two cleaners taking turns
  - The turns don't matter because there isn't much waiting
- For Web applications it is better to have a concurrent system as there is lot's of waiting
  - FastAPI offer concurrency and parallelism
  - GO is a language that is great for asnychronicty
- Web + Machine Learning
  - FastAPI offers concurrency and parallelism/multiprocessings
  - multiprocessing is important to CPU bound Machine Learing Systems
  - This makes FastAPi great for data science
- async and await
  - define an operation that will require waiting before giving the results
``` python
# tells python it will need to wait for get_burgers before storing the results of burgers
burgers = await get_burgers(2)

# for await to work you must define async in the function
async def get_burgers(number: int):
  #do something that takes a long time asynchronously
  return burgers
```        
  - when defining the path operatoin functions in FastAPI if app.get can be called with await you need to define your path function with async
  - or when calling a async function from a library within your own function def you need to define it with async 
``` python
@app.get('/burgers') #this is the path operation function it's a path and does a function
async def read_burgers():
  burgers = await get_burgers(2)
  return burgers
```
### PreRec: Environment Variables
- "env var": a variable that lives outside of the Python code
- lives in the operating system and can be read by your program
- helpful for handling application settings (as part of the installation of python)
``` python
# read ENV vars into python
import os
name = os.getenv("MY_NAME")
```
- env var are set outside the code and don't need to be stored (commited to git) with the rest of the files
- this makes them good for configureations or settings and sesative variables like passwords
- all env var are strings so they must convereted once read into a program
- PATH is a special env var to tell the os where to find programs to run
- for example when you try to run python the os will look in the path variable to for where to find "python" to run your code

### PreRec: Virtual Environments
