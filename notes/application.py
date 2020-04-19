from flask import Flask, render_template, request, session # gives access to a variable called `session`
                                                           # which can be used to keep vaules that are specific to a particular user
from flask_session import Session # an additional extension to sessions which allows them
                                  # to be stored server-side

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note")
        notes.append(note)

    return render_template("index.html", notes=notes)

# notes is the list where the notes will be stored. 
# If the user doesn’t have a notes list already (checked with if session.get("notes") is None), then they are given an empty one.

# If a request is submitted via "POST" (that is, through the form), then the note is processed from the form in the same way as before.

# The processed note, now in a Python variable called note, is appended to the notes list. 
# This list is itself inside a dict called session. Every user has a unique session dict, and therefore a unique notes list.

# Finally, the notelist is rendered by passing session["notes"] to render_template.