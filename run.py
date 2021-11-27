import os
import configparser
from app.factory import create_app

config = configparser.ConfigParser()
app_configuration = os.path.abspath(os.path.join("application.ini"))
config.read(os.path.abspath(app_configuration))

if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config['TEST']['MONGO_URI']

    app.run()
    