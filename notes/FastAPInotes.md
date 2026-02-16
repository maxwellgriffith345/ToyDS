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
