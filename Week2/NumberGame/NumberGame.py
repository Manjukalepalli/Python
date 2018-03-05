from flask import Flask, redirect, render_template, session, request
import random

app=Flask(__name__)
app.secret_key="jalskjdl"

@app.route('/')
def home():
    if 'randomKey' in session:
        pass
    else:
        session['randomKey']=random.randint(1,100)
    return render_template('NumberGame.html')
    
@app.route('/numberGame',methods=["POST"])
def numbergame():
    session['num']=request.form['number']
    print(session['num'])
    redirect('/')
        
app.run(debug=True)