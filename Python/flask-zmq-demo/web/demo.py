# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.zmq import ZMQ
from config import DefaultConfig

app = Flask(__name__)
app.config.from_object(DefaultConfig())

zmq = ZMQ()
zmq.init_app(app)

@app.route("/")
def hello():
    pyobj = {
        'key': 'value'
    }
    zmq.send_pyobj(pyobj)
    return "Hello World!"


if __name__ == "__main__":
    app.run()
