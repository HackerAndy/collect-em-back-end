# cis-553-python
* [Developer Setup](/DEVELOPER_SETUP.md)
   > Including, instructions on running the application locally
* [What this application does](#application-usage)

---
## Application Description

The functionality provided is used to maintain a personal collection of 'things'. This can be anything ranging from Pokemon cards, to personal yachts. 

The code in this repo is the 'backend' component of a larger application. 
This code functions as an API server that exposes various endpoints to manipulate data stored in a MongoDB. 
This application performs CRUD operations on the data (Create, Read, Update, and Delete). 

---
## Application Usage

Since this is a 'backend' application, its usage is limited to REST API calls. They can be executed from tools like [Postman](https://www.postman.com). 
However, an easier way to test out the functionality is provide by a built-in component called Swagger, described below.


### Swagger API Documentation and Testing for this project  

Once the app is running, an url is reserverd to test out the API calls this app accepts. [http://127.0.0.1:5000/swagger-ui](http://127.0.0.1:5000/swagger-ui)  

![Swagger Example](/_images/swagger-example.jpg)

>Instructions to generate client API code from this swagger implementation can be found here:  https://github.com/swagger-api/swagger-codegen