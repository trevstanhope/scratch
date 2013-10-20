   import cherrypy
    from pymongo import Connection

    class mongocherry(object):

    def index(self):
    db=Connection().geo
    output =[]
    output.append('<HTML><HEAD><TITLE>D3 and MONGODB</TITLE><script type="text/javascript" src="http://d3js.org/d3.v2.min.js"></script><style type="text/css">div.bar {display: inline-block;width: 20px;height: 75px;margin-right: 2px;background-color: teal;}</style></HEAD><BODY><h1>D3 and MongoDB</h1>')
    output.append('<script type=”text/javascript”>var dataset=[')

    for x in db.places.find():
    output.append(str(x["loc"][0])+',')
    output.append('0];' +:\n:+'d3.select("body").selectAll("div").data(dataset).enter().append("div").attr("class", "bar").style("height", function(d) {var barHeight = d * 5;return barHeight + "px";});</script></body></html>')

    i=0
    html=”"
    while i<len(output):
    html+=str(output[i])
    i+=1

    return html

    index.exposed = True

    cherrypy.config.update({‘server.socket_host’: ’127.0.0.1′,
    ‘server.socket_port’: 8000,
    })

    cherrypy.quickstart(mongocherry())
