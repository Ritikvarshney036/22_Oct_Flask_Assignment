from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Route to trigger a notification
@app.route('/notify')
def notify():
    message = "A new notification has arrived!"
    socketio.emit('new_notification', {'message': message}, broadcast=True)
    return "Notification sent!"

# Event for handling custom events (if needed)
@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    socketio.run(app, debug=True)
