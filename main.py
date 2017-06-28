from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

def validate(u, p, p2, em):
    errors = {0:"", 1:"", 2:"", 3:""}
    if u == "":
        errors[0] = "please enter a username"
    elif len(u) > 20 or len(u) < 3:
        errors[0] = "username out of range (must be between 3 and 20 Characters)"
    elif
    
    if p == "":
        errors[1] = "please enter a password"

    if p2 == "":
        errors[2] = "please re-enter your password"

    if em == "":
    


@app.route("/" methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form["user"]
        pasw = request.form["pass"]
        pas2 = request.form["pass2"]
        mail = request.form["mail"]
        errors = validate(user, pasw, pas2, mail)
        return render_template('body.html', errors[0], errors[1], errors[2], errors[3])

    if request.method == "GET":   
        return render_template('body.html')

@app.route("/hello", methods=['POST'])
def hello():
    firstname = request.form["first"]
    return render_template("greeting.html", name=firstname)


app.run()

#The user leaves any of the following fields empty: username, password, verify password.

#The user's username or password is not valid -- for example, it contains a space character 
# or it consists of less than 3 characters or more than 20 characters (e.g., a username or password 
# of "me" would be invalid).

#The user's password and password-confirmation do not match.
#The user provides an email, but it's not a valid email. Note:
#  the email field may be left empty, but if there is content in it, then it must be validated.
#  The criteria for a valid email address in this assignment are that it has a single @, a single ., 
# contains no spaces, and is between 3 and 20 characters long.