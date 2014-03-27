# -*- coding: utf-8 -*-

import zmq


def main():
    c = zmq.Context()
    s = c.socket(zmq.PULL)
    s.bind('ipc:///tmp/flask-zmq-demo.sock')

    while True:
        pyobj = s.recv_pyobj()
        if pyobj:
            print pyobj['key']

if __name__ == '__main__':
    main()
