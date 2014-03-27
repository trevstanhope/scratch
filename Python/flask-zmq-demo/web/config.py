# -*- coding: utf-8 -*-
import zmq


class DefaultConfig():

    #  For ZMQ
    ZMQ_SOCKET_TYPE = zmq.PUSH
    ZMQ_BIND_ADDR = 'ipc:///tmp/flask-zmq-demo.sock'