# Setup
* [One Time Setup](#pre-requisites-one-time-setup)
  * [Install Python](#python3)
  * [Install MongoDB](#mongodb)
  * [Install MongoDB GUI * optional * ](#compass-mongodb-gui)
  * [Load test data into MongoDB](#pre-load-test-data-int-the-mongodb-database)
  * [Pipenv - Python virtual env](#pipenv-python-virtual-environment)
  * [Python project dependencies](#install-application-dependencies)
* [Running application tests](#running-application-tests)
* [Running the app locally](#running-locally)
---

## Pre-requisites / One time setup
### Install the following:  

1. **Python3**  
    Mac/Windows: https://www.python.org/downloads/

1. **MongoDB**  
    On Mac: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/  
    On Windows: https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/

1. **Compass (MongoDB GUI)**  
    Mac/Windows: https://docs.mongodb.com/compass/current/install/

1. **pipenv** - python virtual environment

    ```shell
    pip3 install --user pipenv
    ```
    > More info on Pipenv can be found here [pipenv](pipenv.pypa.io) and here [pipenv tutorial](https://realpython.com/pipenv-guide/)

### Application setup:  

1. First, perform a git clone on this repo.  
    ``` shell
    git clone https://github.com/DocDrewToo/cis-553-python.git
    cd cis-553-python
    ```

1. Start the python virtual environment 
    ```shell
    pipenv shell
    ```

    > NOTE: The actual`{pipenv_cmd}` used above might depend on your OS / pipenv installation.  
    > NOTE: To install new packages via pipenv, replace the normal pip3 command with pipenv. i.e. `pipenv install numpy`

1. Install application dependencies  
    Install all the python dependencies used in this project via pipenv. Before running the following command, change your current directory to the root directory of this project (from performing the first step above).  

    ```shell
    pipenv install
    ```

1. **Pre-load test data into the MongoDB database**
    A file `mongodb_data.json` contains test data that can be loaded into the mongo database

    To insert test data into the mongo db:  
    ```shell
    python3 preload-data.py insert
    ```
    > NOTE: If needed, the test data can be deleted easily via replacing `insert` with `delete` in the above command.  
    > NOTE: All data stored in the DB will be automatically saved when shutting down the MongoDB instance.


## Running the app Locally
1. Start the MongoDB instance:  
    For Mac:  
    ```shell
    brew services start mongodb-community@5.0
    ```

1. Start the python virtual environment (if not already started):  
    ```shell
    pipenv shell
    ```

1. Start the flask python application:  
    ```shell
    python3 run.py
    ```

1. Test out the functionality!  
[http://127.0.0.1:5000/swagger-ui](http://127.0.0.1:5000/swagger-ui)  

