from flask import Flask, render_template

app = Flask(__name__)

# Define a simple home route
@app.route('/')
def home():
    return "Welcome to the Home Page!"

# Simulate an error for demonstration
@app.route('/cause-error')
def cause_error():
    raise Exception("This is a simulated error.")

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
