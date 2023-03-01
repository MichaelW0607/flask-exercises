from flask import Flask, render_template, request

app = Flask(__name__)

my_todo = [
  "Go to california"
  "See a play "
]
  
  
app.route("/")
def index():
  return render_template("todo.html.jinja",todos ="My_todo")

app.route("/add", methods = ["POST"])
def add ():
  new_todo = request.form["new_todo"]
  return new_todo