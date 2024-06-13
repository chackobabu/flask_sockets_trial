from flask import Flask, session, render_template,redirect, request, url_for
from flask_socketio import SocketIO, emit, join_room, leave_room, send
import time
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = "safdas"
socketio = SocketIO(app)

@app.route("/")
def index():
    session.clear()
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        print("Hi", session['name'])
        socketio.emit('alert_details', {'message':f"Hey {session['name']}"})
    return redirect(url_for('index'))

@socketio.on('my_event')
def print_message_from_client(data):
    session['id'] = data['data']
    print(session['id'])

if __name__ == '__main__':
    socketio.run(app, port=8080, debug=True)