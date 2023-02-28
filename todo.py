from flask import Flask, render_template, request

app = Flask(__name__)

todos=[
  
]
  
  
app.route("/")
def index():
  return render_template("home.html.jinja",my_variable="My todo")

app.route("add")
def add ():
  new_todo = request.form["new_todo"]
  return new_todo