# Libraries
from flask import Flask, render_template
import zmq
import json

# Constants
FLASK_IP = '0.0.0.0'
FLASK_PORT = 5000
ZMQ_SERVER = "tcp://*:1980"

# ZMQ
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind(ZMQ_SERVER)

# Flask
app = Flask(__name__)

## Routes
#@app.route('/')
#def index():
#    packet = socket.recv()
#    print json.loads(packet)
#    return render_template('index.html')
     
# Main
if __name__ == '__main__':
    app.run(FLASK_IP, port=FLASK_PORT, debug=True)
    pass
