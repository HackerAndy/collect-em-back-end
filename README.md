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


### Swagger API Documentation  

**Live API testing for this project**

Once the app is running, an url is reserverd to test out the API calls this app accepts. [http://127.0.0.1:5000/swagger-ui](http://127.0.0.1:5000/swagger-ui)  

![Swagger Example](/_images/swagger-example.jpg)

**Generating Code from swagger**
Instructions to generate client API code from this swagger implementation can be found here:  https://github.com/swagger-api/swagger-codegen

**Generating UML diagrams from swagger**
1. Download the json swagger specifications. 
  * The specifications can be found here: http://127.0.0.1:5000/api-docs
    > A version has been saved in this repository under `api-docs.json`
2. Run the swagger-to-uml application
    > NOTE: It is assumed [Application Setup](/DEVELOPER_SETUP.md#application-setup) has been done
  * execute the following command line:
    ```sh
    python3 swagger_to_uml/bin/swagger_to_uml api-docs.json api-docs.puml
    ```
    > This will output on the screen the code necessary for the next step
3. Navigate to https://plantuml.com
  * Click on the `server` link on the left menu of the main site
  * Copy / paste the contents of the previous step and execute!
    > A prior execution of this has bee saved as the file [api-docs-uml.png](api-docs-uml.png) in this project.