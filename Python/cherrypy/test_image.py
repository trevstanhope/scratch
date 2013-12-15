#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import cherrypy
import os.path
class HelloWorld:
  def index(self):
    x = np.linspace(0,2*np.pi,100)
    y = np.sin(x)
    plt.plot(x,y)
    
    plt.savefig('img/test.png')
    return '<img src="/img/test.png" />'
  index.exposed = True

if __name__ == '__main__':
  currdir = os.path.dirname(os.path.abspath(__file__))
  conf = {
    '/css/style.css': {'tools.staticfile.on':True,
    'tools.staticfile.filename': os.path.join(currdir,'css','style.css')},
    '/img':{'tools.staticdir.on':True,
    'tools.staticdir.dir':os.path.join(currdir,'img')}
    }
  cherrypy.quickstart(HelloWorld(), "/", config=conf)
