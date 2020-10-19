from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'b5172a60a33db069872bff19953e6eeb'
posts =[
    {
        'author': 'Sergo Rogalskii',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Today',
    },
    {
        'author': 'Sergo Rogalskii',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Tomorrow',
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

if __name__ == '__name__':
    app.run(debug=True)