from flask import Flask
from routes.users_controller import users_route

app = Flask(__name__)

app.register_blueprint(users_route)

app.run(debug = True)