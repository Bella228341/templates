from app import app
from flask import render_template
from random import randint
from math import factorial

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/1")
def randnum():
    list_ = [randint(1, 200) for i in range(50)]
    list_.sort()
    return render_template("rundnum.html", l=list_)

@app.route("/3")
def fact():
    num = randint(0, 100)
    if num<50: return str(num*1.5)
    else: return str(factorial(num))

@app.route("/2")
def te():
    d = {"name": "makar",
         "country": "UA",
         "age":"13"}
    return render_template("ftext.html", d=d)
    



