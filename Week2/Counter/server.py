from flask import Flask, render_template, session,redirect
app=Flask(__name__)
app.secret_key="jaljdslja"

@app.route('/')
def main():
    if 'count' in session:
        num = int(session['count'])
        session['count']= str(num+1)
    else:
        session['count']='1'
    return render_template('index.html',count=session['count'])

@app.route('/index',methods=['POST'])    
def index():
    session['count']+=1
    return redirect('/')
    
app.run(debug=True)