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

   

  cursor.execute(f"INSERT INTO `Todos`(`Description`) VALUES ('{new_todo}') ")

  my_todo.append(new_todo)
  return new_todo

cursor = connection.cursor()

cursor.execute("SELECT * FROM `Todos` ")

result = cursor.fetchall()

print(result)