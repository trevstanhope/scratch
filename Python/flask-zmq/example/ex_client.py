import zmq
import json

ZMQ_SERVER = "tcp://127.0.0.1:1980"
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(ZMQ_SERVER)

if __name__ == '__main__':
    sample = {'type':'test'}
    dump = json.dumps(sample)
    result = socket.send(dump)
    dump = socket.recv(zmq.NOBLOCK)
    response = json.loads(dump)
    print response
