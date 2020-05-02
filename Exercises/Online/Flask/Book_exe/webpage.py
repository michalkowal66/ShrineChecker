from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
# Base class is imported from the module
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# Yet validators and fields are imported directly from WTForms.

app = Flask(__name__)
# We initialize the flask application, creating class instance
bootstrap = Bootstrap(app)
# We initialize the bootstrap module for bootstrap templates
moment = Moment(app)
# We initialize the moment module for time parsing

app.config['SECRET_KEY'] = 'trudny do odgadnięcia ciąg znaków'
# app.config is a dictionary containing configurational variables used either
# by modules or the app itself. In our case we create it for WTForms

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit') 
# <!> Check available fields and validators of WTForms
# https://wtforms.readthedocs.io/en/latest/validators/
# https://wtforms.readthedocs.io/en/2.3.x/fields/


@app.route('/', methods=['GET', 'POST'])
# Adding more possible routes for certain page
# Defining methods as a list determines the available methods for given URL
# If we do not provide methods only GET is available as default.
def home():
    name = None
    form = NameForm()
    # Form variable is defined as NameForm class instance
    if form.validate_on_submit():
    # Returns true after the form has been sent and accepted by all field validators
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Seems like you have a different name now!')

        session['name'] = form.name.data
        # Provided in the form user's name is now stored in the session
        # dictionary in key 'name'.

        return redirect(url_for('home'))
        # Function redirect could've been provided with simply '/' in our case
        # yet as an example of different solution, url_for() function was used
        # being provided with our function's name responsible for '/' URL

        # pre session+redirect version
        # name = form.name.data
        # form.name.data input text is available as field's attribute 'data'
        # form.name.data = ''
        # We clear the field after assigning the name to the local variable name
    return render_template('home.html', form=form, name=session.get('name'))
    # We use rener_template function to render previously prepared template
    # written in html format in order to keep the code cleaner.
    # We pass the form variable predefined in the function body
    # Name variable is being extracted from session data using key 'name'
    # method get() is used to avoid exception caused by calling unknown key
    # insted in case of unknown key method get() returns simply None

# When we click refresh button it repeats last request, repeating POST is not
# desired it's good to use redirecting to avoid it. Redirecting initiates GET
# method, so now last request is GET not POST. This is also known as:
# Design Pattern Post/Redirect/Get
# This solution has also a downside - after redirecting to new URL we lose
# the data passed in the form because the POST request finishes it's work

@app.route('/welcome/<user>')
# Dynamic route taking <name> argument and passing it to the function
# Flask allows us to pass also different types of arguments like:
# string, int, float and path(contrarily to string, path can contain slashes)
def welcome(user):
    return render_template('welcome.html', user=user)

def contact():
    return render_template('contact.html')
app.add_url_rule('/contact', 'contact', contact)
# Different way to create a route to a certain url, decorator @app.route basically
# uses add_url_rule method.

@app.route('/time')
def time():
    return render_template('time.html', current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
# We create an error handling utility to deal with 404 error, we use a special
# template to keep the webpage well organised and clean.

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500   

if __name__ == '__main__':
    app.run(debug=True)
    # Setting debug= True enables live changes tracking