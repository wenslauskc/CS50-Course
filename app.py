from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name")
    return render_template("index.html")

@app.route("/greet", method=["POST"])
def greet():
    name = request.form.get("name")
    return render_template("greet.html", name=name)

