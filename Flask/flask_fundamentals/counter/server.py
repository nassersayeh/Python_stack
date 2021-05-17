from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)    
app.secret_key = 'nasser sayeh' 
@app.route('/')          
def one():
    if 'count' not in session:
        session['count']=0
    session['count']+=1
    return render_template("index.html",count=session['count'])  
@app.route('/addtwo')          
def three():
    if 'count' not in session:
        session['count']=0
    session['count']+=2
    if 'sik' in session:
        session.pop('sik')
    return render_template("index.html",count=session['count'])  
@app.route('/destroy_session')          
def two():
    session.clear()
    return redirect('/')

@app.route('/addx',methods=["POST"])          
def four():
    print(request.form['num'])
    if 'count' not in session:
        session['count']=0
    session['count']+=int(request.form['num'])
    session['sik']=request.form['num']
    return render_template("index.html",count=session['count'])
if __name__=="__main__":
    app.run(debug=True)
