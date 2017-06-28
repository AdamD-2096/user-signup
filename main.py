from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('body.html')

@app.route("/hello", methods=['POST'])
def hello():
    firstname = request.form["first"]
    return render_template("greeting.html", name=firstname)


@app.route("/", methods=['POST'])
def validate():
    print('validate')

app.run()