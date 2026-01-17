from flask import Flask, jsonify, render_template, request
from DepopCalc import program
app = Flask(__name__) 


@app.route("/", methods =['GET', 'POST']) 
def index(): 
    if request.method == 'POST': 
        user_input  = request.form['username'] 
        return f"Hello, {user_input}" 
    return render_template("index.html") 

app.run(debug=True)