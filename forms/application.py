from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["GET","POST"]) #allow both get (directly input link) and post methods
def hello():
    if request.method == "GET": #if use get method, will be directed to the page "please submit the form instead"
        return "Please submit the form instead."
    else:
        name = request.form.get("name") # take the request the user made, access the form,
                                        # and store the field called `name` in a Python variable also called `name`
        return render_template("hello.html", name=name)

