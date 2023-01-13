from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
import os
from dotenv import load_dotenv

# ~~~ Config ~~~
# ~~~ Config ~~~
# ~~~ Config ~~~
load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
db = SQLAlchemy(app)
ma = Marshmallow(app)
jwt = JWTManager(app)

@app.route('/')
def index():
    return jsonify("Hello To The World! We're Running")


if __name__=='__main__':
    app.run(debug=True)