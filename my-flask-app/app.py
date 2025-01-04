from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/ic")
def ic():
    return render_template("id-class.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/pr")
def pr():
    return render_template("prac.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    