from flask import Flask, render_template,request
from db import Database

app = Flask(__name__)

dbo = Database()

@app.route("/")
def index():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/perform_registration", methods=['post'])
def perform_registration():
    name = request.form.get('users_name')
    email = request.form.get('users_email')
    password = request.form.get('users_password')

    response = dbo.insert(name,email,password)
    if response:
        return render_template('login.html',message="Registered Successsfully! Kindly Login Here")
    else:
        return render_template('register.html', message="Email Already Exists!")

@app.route("/perform_login", methods=["post"])
def perform_login():
    email = request.form.get("user_email" )
    password = request.form.get("user_password")

    response = dbo.search(email,password)

    if response==1:
        return "Login Successfully!"
    else:
        return render_template("login.html", message="Login Failed!")

    
if __name__ == "__main__":
    app.run(debug=True)