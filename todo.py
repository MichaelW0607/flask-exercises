from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors 

app = Flask(__name__)

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
  cursor.execute("SELECT * FROM `Todos`" )
  cursor.execute("SELECT * FROM `Todos` ORDER BY `Complete`")
  results = cursor.fetchall()
  return render_template("todo.html.jinja",
  My_todo=results
  )



@app.route("/add", methods = ["POST"])
def add ():
  new_todo = request.form["new_todo"]

  cursor = connection.cursor()
  cursor.excute(f"INSERT INTO `Todos` (`description`) VALUES ('{new_todo}')")
  return redirect("/")

@app.route("/complte", methods = ["POST"])
def complete():
  todo_id = request.form["todo_id"]
  cursor = connection.cursor()
  cursor.excute(f"UPDATE `Todos`complete` = 1 WHERE `id` = {todo_id}")
  return redirect("/")
