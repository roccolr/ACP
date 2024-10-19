from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/useradv/<name>')
def user_adv(name):
    elements = ['a', 'b', 12]
    return render_template('user_adv.html', name=name, elements=elements)

if __name__ == '__main__':
    app.run(debug=True)