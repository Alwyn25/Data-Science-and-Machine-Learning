import socketio
import random

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to server")

@sio.event
def disconnect():
    print("Disconnected from server")

def send_random_value():
    random_value = random.randint(1, 100)
    sio.emit('random_value', random_value)
    print(f"Sent random value to server: {random_value}")

if __name__ == "__main__":
    sio.connect('http://localhost:5000')
    send_random_value()
    sio.wait()
