from flask import Flask, request, redirect, render_template, session, flash
import re
# import the Connector function
from mysqlconnection import MySQLConnector

app = Flask(__name__)
app.secret_key="asdaskjhdlkas"
# connect and store the connection in "mysql" note that you pass the database name to the function
mysql = MySQLConnector(app, 'dbuser')


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def main():
    if  "validEmail" not in session:
        session["validEmail"]='True'
    return render_template('user.html')

@app.route('/users',methods=['POST'])
def user():
    if (len(request.form['email']) < 1 or not EMAIL_REGEX.match(request.form['email'])):
        session["validEmail"]='False'
        return redirect('/')
    else:
        session["validEmail"]='True'
        query = "INSERT INTO users(email) VALUES (:email)"
        # We'll then create a dictionary of data from the POST data received.
        data = {
             'email': request.form['email']
           }
        mysql.query_db(query, data)
        return redirect('/success')
    
@app.route('/success')
def sucess():    
    query="select * from users"
    print(query)
    print (mysql.query_db("SELECT * FROM users"))
    session["users"]=mysql.query_db(query)
    return render_template('success.html')

app.run(debug=True)