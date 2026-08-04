# flash meassage----> action perform hota ak bar fir uska bad remove hojata ha  like atm machine  store one time memoey
#flash() +get _flashed_message()

from flask import Flask, render_template, request,redirect,url_for,flash
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key="my-secret-key"
@app.route("/",methods=["GET","POST"])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        flash(f"welcome,{name}you are registerd succefullly","Sucess")
        return redirect(url_for("succes"))
    return render_template("register.html",form=form)
@app.route("/success")
def success():
    return render_template("success.html")





if __name__ == "__main__":
    app.run(debug=True)