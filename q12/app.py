from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Global variable to keep track of the counter
counter = 0

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Handle a custom event to update the counter
@socketio.on('update_counter')
def handle_update():
    global counter
    counter += 1
    socketio.emit('counter_update', counter, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
