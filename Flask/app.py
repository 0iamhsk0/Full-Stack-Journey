from flask import Flask
app = Flask(__name__)

# a decorator for registering with the given/default URL
@app.route('/')
def hello():
    return 'Hello, Im learning flask';

if __name__ == '__main__':
    app.run(debug=True)