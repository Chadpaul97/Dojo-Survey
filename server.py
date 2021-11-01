from flask import Flask, render_template,request, session, redirect
app = Flask(__name__)
app.secret_key = "MyNinjaWay"



@app.route('/')
def survey():
    if "user" not in session:
        session["user"] = []
    return render_template("index.html")

@app.route('/resultspage')
def resultsPage():
    return render_template("results.html",user=session["user"])


@app.route("/results", methods=["POST"])
def results():
    temp_user ={
        "name": request.form["name"],
        "location": request.form["location"],
        "language": request.form["language"],
        "comments": request.form["comments"],
    }
    session["user"].append(temp_user)
    session.modified = True
    return redirect("/resultspage")

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)