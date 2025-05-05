from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Define a route for the root
@app.route('/')
def home():
    return 'Welcome to the Softy Pinko Backend!'

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)

