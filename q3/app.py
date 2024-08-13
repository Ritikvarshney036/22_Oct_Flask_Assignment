from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome to the Flask App</h1><p>Use the /greet/<name> URL to receive a greeting!</p>'

@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return render_template('multiply.html', num1=num1, num2=num2, result=result)

if __name__ == '__main__':
    app.run(debug=True)
