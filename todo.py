from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors 
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "michael": generate_password_hash("hello"),
    "anthony": generate_password_hash("bye")
}

my_todo = [
  "Go to california"
  "See a play "
]

connection = pymysql.connect(
    host="10.100.33.60",
    user="mwilliams",
    password="220467419",
    database="mwilliams_Todos",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

@app.route("/")
def index():
  cursor = connection.cursor()
  cursor.execute("SELECT * FROM `Todos` ORDER BY `Completed`")
  results = cursor.fetchall()
  return render_template("todo.html.jinja",
  My_todo=results
  )



@app.route("/add", methods = ["POST"])
def add ():
  new_todo = request.form["new_todo"]

  cursor = connection.cursor()
  cursor.execute(f"INSERT INTO `Todos` (`description`) VALUES ('{new_todo}')")
  return redirect("/")

@app.route("/complete", methods = ["POST"])
def complete():
  todo_id = request.form["todo_id"]
  cursor = connection.cursor()
  cursor.excute(f"UPDATE `Todos`complete` = 1 WHERE `id` = {todo_id}")
  return redirect("/")

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username
    