from flask import Flask, render_template, request
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
    database="world",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

@app.route("/")
def index():
  cursor = connection.cursor
  cursor.execute("retrieve data")
  results = cursor.fetchall()
  return render_template("todo.html.jinja",todos ="My_todo")

@app.route("/add", methods = ["POST"])
def add ():
  new_todo = request.form["new_todo"]
  return new_todo