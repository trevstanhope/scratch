import zmq

class Listener:

    def __init__(self):
        self.ZMQ_SERVER = 'tcp://*:1980'
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect(self.ZMQ_SERVER)
        
    def ping(self):
        self.socket.send('ping')
        response = self.socket.recv()
        if response == 'pong':
            return True
        else:
            return False
        
