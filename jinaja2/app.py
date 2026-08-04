from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def student_profile():
    return render_template(
        "index.html",
        name="ayan",
        is_topper=True,
        subjects=["maths","science","history"]
    )
if __name__ == "__main__":
    app.run(debug=True)  