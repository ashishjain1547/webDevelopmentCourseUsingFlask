from flask import Flask # Importing the class 'Flask'
from flask import Response
import json 

app = Flask(__name__) # Initializing a Flask application

@app.route('/')
def index():
    return """<h1>Hello World!</h1>
    <h2>You have landed on the default page.</h2> 
    <h3>How may I help you?</h3> 
    <h7>This is like plain text. Nothing special.</h7>"""

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)


@app.route('/test_json', methods=['POST'])
def test_json():
    o = [
        {
            "first_name": "Vaibhav",
            "last_name": "Deshmukh"
        },

        {
            "first_name": "Ashish",
            "last_name": "Jain"
        }
    ]
    return Response(json.dumps(o), status=201, mimetype='application/json')


if __name__ == '__main__':
    app.run(port='5000')