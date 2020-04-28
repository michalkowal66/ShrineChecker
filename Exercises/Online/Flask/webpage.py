from flask import Flask, render_template
app = Flask("__main__")

posts = [
    {
        'author': 'Michał Kowal',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '28.04.2019'
    },
    {
        'author': 'Urszula Kowal',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': '29.04.2019'
    }
]

@app.route("/")
@app.route("/home")
#Adding more possible routes for certain page
def home():
    return render_template('home.html')
    #We use rener_template function to render previously prepared template
    #written in html format in order to keep the code cleaner

@app.route("/about")
def about():
    return render_template('about.html', posts=posts, title="About")

if __name__ == "__main__":
    app.run(debug=True)
    #Setting debug= True enables live changes tracking