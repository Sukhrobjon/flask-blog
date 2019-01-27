from flask import Flask, render_template, url_for, flash, redirect
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


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your username and password', 'danger')

    return render_template('login.html', title='Login', form=form)

    
if __name__ == "__main__":
    app.run(debug=True)
