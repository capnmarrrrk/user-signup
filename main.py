from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/validate", methods=['POST'])
def validation():
    #varibles from form
    form_username = request.form['username']
    form_pw = request.form['password']
    form_verify = request.form['verify']
    form_email = request.form['email']

    match=False;


   
    

    pwError = ""
    usernameError = ""
    missmatchError = ""

    pwFill = ""
    valFill = ""
    emailFill = ""
    emailError = ""

    space = " "
#return render_template('false.html')

    #else:
        #return render_template('true.html')

    #The user leaves any of the following fields empty: username, password, verify password.
    if space in form_username or (len(form_username) < 3 or len(form_username) > 20):
        usernameError = "That's not a valid username"
        form_username = ""
        
    
    if  space in form_pw or (len(form_pw ) < 3 or len(form_pw ) > 20):
        pwError = "That's not a valid password"
        pwFill = ""
        
    
    if form_verify != form_pw:
        missmatchError = "That's not a valid password"
        pwError = "That's not a valid password"
        valFill = ""
        pwFill = ""
        
    
    if space in form_verify or (len(form_verify) < 3 or len(form_verify) > 20):
        missmatchError = "Passwords don't match"
        valFill = ""
        
    if space in form_email or (form_email.count("@") > 1 or form_email.count(".") > 1):
        emailError = "That's not a valid email"
        form_email=""

    if len(form_email) < 3 or len(form_email) > 20:
        emailError = "That's not a valid email"
        form_email=""
            
    if missmatchError == "Passwords don't match" or emailError == "That's not a valid email" :
        return render_template('index.html', username_error=usernameError, user_name=form_username,
            pw_fill=pwFill, pw_error=pwError, val_fill=valFill, mm_error=missmatchError, email_fill=form_email, em_error = emailError )
    else:
        return render_template('welcome.html',user_name=form_username )




    
    #The user's password and password-confirmation do not match.
    #The user provides an email, but it's not a valid email. Note: the email field may be left empty, 
    # but if there is content in it, then it must be validated. The criteria for a valid email address 
    # in this assignment are that it has a single @, a single ., 
    # contains no spaces, and is between 3 and 20 characters long.

    #Each feedback message should be next to the field that it refers to.

    #For the username and email fields, you should preserve what the user typed, 
    # so they don't have to retype it. With the password fields, 
    # you should clear them, for security reasons.

    # If all the input is valid, then you should show the user a welcome page that uses 
    # the username input to display a welcome message of: "Welcome, [username]!"

    # Use templates (one for the index/home page and one for the 
    # welcome page) to render the HTML for your web app.



@app.route("/")
def index():
    return render_template('index.html')
app.run()
