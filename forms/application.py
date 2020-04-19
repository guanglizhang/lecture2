from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name") # take the request the user made, access the form,
                                    # and store the field called `name` in a Python variable also called `name`
    return render_template("hello.html", name=name)

