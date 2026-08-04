from flask import Flask,request

app = Flask(__name__)

@app.route("/")
def home():
    return "hello user this is my first flask app"
@app.route("/about")
def about():
    return 'this is about page'
@app.route("/contact")
def contact():
    return 'this is contact page'
@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method =="POST":
        return 'you send a data'
    else:
        return 'you only seee only data'

if __name__ == "__main__":
    app.run(debug=True)

