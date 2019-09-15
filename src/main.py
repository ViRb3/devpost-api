from flask import Flask
from flask_cors import CORS, cross_origin
import api

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return 'Hello'

@app.route("/user/<username>")
def user(username):
    return api.get_user(username)

@app.route("/project/<project_name>")
def project(project_name):
    return api.get_project(project_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')