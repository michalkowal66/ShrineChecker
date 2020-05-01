from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
@app.route("/home")
#Adding more possible routes for certain page
def home():
    return render_template('home.html')
    #We use rener_template function to render previously prepared template
    #written in html format in order to keep the code cleaner

@app.route("/welcome/<name>")
#Dynamic route taking <name> argument and passing it to the function
#Flask allows us to pass also different types of arguments like:
#string, int, float and path(contrarily to string, path can contain slashes)
def welcome(name):
    return render_template('welcome.html', name=name)

def contact():
    return render_template('contact.html')
app.add_url_rule('/contact', 'contact', contact)
#Different way to create a route to a certain url, decorator @app.route basically
#uses add_url_rule method.

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500   

if __name__ == "__main__":
    app.run(debug=True)
    #Setting debug= True enables live changes tracking