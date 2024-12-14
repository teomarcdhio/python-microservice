# Import required packages
from flask import Flask, jsonify

# Instantiate the flask app
app = Flask(__name__)

# Route the api request so that the root path returns a json object 
@app.route('/')
def message():
    return jsonify(message=f"Hello, World!")

# If main.py is run directly, serve the app in debug mode; host definition is required to expose the flask app when using on a container.
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)