from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Define the home route
@app.route('/')
def home():
    return render_template('chat.html')

# Handle incoming messages
@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)  # Broadcast the message to all clients

if __name__ == '__main__':
    socketio.run(app, debug=True)
