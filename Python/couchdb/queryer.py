import couchdb

server = couchdb.Server()
db = server.create('sttdfgt')
db['johndoe'] = dict(type='Person', name='John Doe')
db['maryjane'] = {'type': 'Person', 'name': 'Mary Jane'}
db['maryfadf'] = {'type': 'Person', 'name': 'Mary Jane', 'age':20}
db['gotham'] = dict(type='City', name='Gotham City')
map_fun = '''function(doc) {
  if (doc.type == 'Person')
  emit(doc.name, null);
  }'''
for row in db.query(map_fun):
  print row.key
