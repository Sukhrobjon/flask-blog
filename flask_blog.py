from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '18426b92a85573844291a91f89f3e3e5'
posts = [
    {
        'author' : 'Sukhrob Golibboev',
        'title' : 'Blog Post 1',
        'content' : 'First content',
        'date_posted' : 'January 25, 2019' 
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second content',
        'date_posted': 'January 24, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home(): 
    '''
    first 'post' is the argument to pass to our tempplate
    second 'posts' variable refers to our list of dictionries up 
    '''
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

    
if __name__ == "__main__":
    app.run(debug=True)
