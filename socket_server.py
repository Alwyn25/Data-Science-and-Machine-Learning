import socketio
import eventlet

sio = socketio.Server()

@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")

@sio.event
def random_value(sid, data):
    print(f"Received random value from client {sid}: {data}")
    # Process data or send a response if needed

@sio.event
def disconnect(sid):
    print(f"Client disconnected: {sid}")

if __name__ == "__main__":
    app = socketio.WSGIApp(sio)
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
