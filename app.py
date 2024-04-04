from flask import Flask ,render_template,request, redirect, session
import os
from flask_bootstrap import Bootstrap
import re
regexemail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
app=Flask(__name__)
Bootstrap(app)
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/upload',methods=['POST','GET'])
def upload():
    if request.method == 'POST':
        regex = request.form['regex']
        text = request.form['text']
        print(regex)
        x = re.findall(regex, text)
        if x:
            return render_template('result.html',text=text,ans="".join(x),showout=True)
        else:
            return render_template('result.html',ans=x,showout=False)


@app.route('/validate',methods=['POST','GET'])
def checkvalid():
    if request.method=='POST':
        email=request.form['email']
        if(re.fullmatch(regexemail, email)):
            return render_template('email.html',res="You Have Valid Email",email=email,showeout=True)
        else:
            return render_template('email.html',res="OOPS Sorry! Invalid Email",showeout=True)
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)
