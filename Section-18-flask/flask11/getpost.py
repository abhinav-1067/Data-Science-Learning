from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the website"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

# Variable rule
@app.route("/success/<int:score>")
def success(score):
    return f"The Marks You Got Is {score}"

if __name__ == "__main__":
    app.run()