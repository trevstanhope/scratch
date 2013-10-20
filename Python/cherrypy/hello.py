#!/usr/bin/env python
import cherrypy

class HelloWorld:
    def index(self):
      return "Hello world!"
    index.exposed = True

cherrypy.quickstart(HelloWorld())

