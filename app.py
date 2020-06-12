import os
from flask import Flask
from flask_restful import Api
from resources.userreg import UserReg
from resources.loggin import login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///mongo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = '1234567890)(*&^%$#@!)'
api = Api(app)

api.add_resource(UserReg, '/register')
api.add_resource(login, '/loggin')

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()
    app.run(port=5000)
