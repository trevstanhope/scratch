#!/usr/bin/env python
import cherrypy

class HelloWorld:
    def index(self):
      return "test"
    index.exposed = True

cherrypy.quickstart(HelloWorld())


