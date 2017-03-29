#!/usr/local/bin/python3

from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
    #return "Hello World!"

@app.route('/about/')
def about():
    return render_template("about.html")
    #return "This is the about page!"
    
# @app.route('/layout/')
# def layout():
#     return render_template("layout.html")

if __name__=="__main__":
    app.run(debug=True)