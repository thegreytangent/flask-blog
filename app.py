from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    trading_list = ["one", "two", 3]
    return render_template('user.html', name='<h2>afd</h2>', trading_list=trading_list)

@app.errorhandler(404)
def error_404(e):
    return "error {}".format(e)


 