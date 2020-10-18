from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '<h1>Hello, Sergo</h1>'

@app.route('/about')
def about():
    return '<h1>About my site</h1>'

if __name__ == '__name__':
    app.run(debug=True)