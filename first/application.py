
# Import the class `Flask` from the `flask` module, written by someone else.
from flask import Flask

# Instantiate a new web application called `app`, with `__name__` representing the current file
app = Flask(__name__)

# A decorator; when the user goes to the route `/`, exceute the function immediately below
@app.route("/")
def index():
    return "Hello, world!"
