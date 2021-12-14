from flask import Flask,request,render_template
import pickle

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("login.html")
database={'nachi','james','kaik'}
database0={'nice','bond','fck'}

database2={'9850171541','7796412155'}
database3={'2021-11-11'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    FirstName=request.form['FirstName']
    LastName=request.form['LastName']
   
    dateofbirth=request.form['dateofbirth']
    mobilenumber=request.form['mobilenumber']
    if  FirstName  not in database:
        
	    return render_template('login.html',info='Invalid User')
    if LastName  not in database0:
        
	    return render_template('login.html',info='Invalid User')  

    else:
        if  mobilenumber not in database2: 
            return render_template('login.html',info='Invalid User') 
       
        if dateofbirth not in database3:
             return render_template('login.html',info='Invalid Password')

        else:
	         return render_template('home.html',name=FirstName)

if __name__ == '__main__':
    app.run(debug=True)
