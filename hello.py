from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("home.html.jinja", my_variable="jinja", my_list=["apples", "bananas", "oranges"])