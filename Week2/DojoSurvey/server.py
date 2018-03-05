from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key ="ashdalh"

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=["POST"])
def users():
    print(request.form)
    session["name"]=request.form["name"]
    session["location"]=request.form["location"]
    session["language"]=request.form["language"]
    session["comment"]=request.form["comment"]
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html')
    
app.run(debug=True)    
