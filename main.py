from flask import Flask, request, redirect, render_template
import re

app = Flask(__name__)
app.config['DEBUG'] = True

def validate(u, p, p2, em):
    errors = {0:"", 1:"", 2:"", 3:"", 4:u, 5:em}
    if u == "":
        errors[0] = "please enter a username"
    elif len(u) > 20 or len(u) < 3:
        errors[0] = "username must be between 3 and 20 characters"
        errors[4] = ""
    elif " " in u:
        errors[0] = "no spaces please"
        errors[4] = ""
    
    if p == "":
        errors[1] = "please enter a password"
    elif len(p) > 20 or len(p) < 3:
        errors[1] = "password must be between 3 and 20 characters"
    elif " " in p:
        errors[1] = "no spaces please"
    
    if p2 == "":
        errors[2] = "please re-enter your password"
    
    if p2 != p:
        errors[1] = "password must match"
        errors[2] = "password must match"

    emat = re.search("\w+@\w+.\w+", em)
    if em == "":
        pass
    elif not emat:
        errors[3] = "please enter a valid email"
        errors[5] = ""

    return errors
    


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form["user"]
        pasw = request.form["pass"]
        pas2 = request.form["pass2"]
        mail = request.form["mail"]
        errors= validate(user, pasw, pas2, mail)
        if errors[0] == "" and errors[1] == "" and errors[2] == "" and errors[3] == "":
            return redirect('/hello?n={0}'.format(user))
        return render_template('body.html', zero=errors[0], one=errors[1], two=errors[2], three=errors[3], four=errors[4], five=errors[5])

    if request.method == "GET":   
        return render_template('body.html')

@app.route("/hello")
def hello():
    firstname = request.args.get('n')
    return render_template("greetings.html", name=firstname)


app.run()



#The user's username or password is not valid -- for example, it contains a space character 
# or it consists of less than 3 characters or more than 20 characters (e.g., a username or password 
# of "me" would be invalid).

#The user's password and password-confirmation do not match.
#The user provides an email, but it's not a valid email. Note:
#  the email field may be left empty, but if there is content in it, then it must be validated.
#  The criteria for a valid email address in this assignment are that it has a single @, a single ., 
# contains no spaces, and is between 3 and 20 characters long.