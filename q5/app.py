from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

# Set a secret key for session management
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/setdata', methods=['GET', 'POST'])
def set_data():
    if request.method == 'POST':
        # Store data in the session
        session['username'] = request.form['username']
        session['email'] = request.form['email']
        return redirect(url_for('display_data'))
    return render_template('set_data.html')

@app.route('/display')
def display_data():
    # Retrieve data from the session
    username = session.get('username')
    email = session.get('email')
    return render_template('display_data.html', username=username, email=email)

@app.route('/logout')
def logout():
    # Clear the session data
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
