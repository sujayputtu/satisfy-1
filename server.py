"""
This script will be run on the server. This script keeps the site alive.
"""

from flask import Flask, redirect, url_for, render_template, request, session
import insert
import check_credentials

app = Flask(__name__)
app.secret_key = "we are the best"

db = insert.insert_val()
check = check_credentials.credentials()

@app.route('/', methods=['POST', 'GET'])
def main_page():
    """This function will load the main page of the website."""
    clear = False
    if request.method == 'POST':
        mail = request.form['mail']
        passwd = request.form['passwd']

        mailid = (mail, )
        clear = check.login(mailid, passwd)

        if clear:
            session['username'] = mail

    if not clear:
        return render_template('/index.html')
    else:
        return render_template('/home.html')

@app.route('/signup', methods=['POST', 'GET'])
def signup_page():
    
    """This function will be executed when the sign-up option is selected.
    'mail id' is considered to be mandatory. If the mail id is given, then it will redirect to home page else the page reloads.
    """
    mail = None
    if request.method == 'POST':
        mail = request.form['mail']
        fname = request.form['fname']
        lname = request.form['lname']
        passwd = request.form['passwd']
        rpasswd = request.form['rpasswd']
        dob = request.form['dob']
        city = request.form['city']
        height = request.form['height']
        weight = request.form['weight']

        db.insert_user(mail, fname, lname, passwd, dob, city, height, weight)

    if mail == None:
        return render_template('/signup.html')
    elif not rpasswd == passwd:
        return render_template('/signup.html')
    else:
        return render_template('/home.html')

@app.route('/home')
def homepage():
    return render_template('/home.html')

if __name__ == '__main__':
    app.debug = True
    app.run(ssl_context = 'adhoc')