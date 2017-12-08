from pymongo import MongoClient
async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
client = MongoClient()
db = client.Cloud
coll = db.dataset
@app.route('/')
def index():
        return render_template('index.html', async_mode=socketio.async_mode)
@socketio.on('echo_event', namespace='/test')
def test_message(message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']})
@socketio.on('broadcast_event', namespace='/test')
def test_broadcast_message(message):
        session['receive_count'] = session.get('receive_count', 0) + 1
        # db.coll.insert( {"message": message['data'] })
        emit('my_response',
             {'data': message['data'], 'count': session['receive_count']},
             broadcast=True)
@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
        session['receive_count'] = session.get('receive_count', 0) + 1
        emit('my_response',
             {'data': 'Disconnected!', 'count': session['receive_count']})
        disconnect()
@socketio.on('connect', namespace='/test')
def test_connect():
        emit('my_response', {'data': 'Connected', 'count': 0})
@socketio.on('disconnect', namespace='/test')
def test_disconnect():
	print('Client disconnected', request.sid)
if __name__ == '__main__':
        socketio.run(app, debug=True)
