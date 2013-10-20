#!/usr/bin/python
# Example for using couchdb
# Create database named 'database': curl -X PUT $HOST/database
# Create admin 'name' with password 'secret': curl -X PUT $HOST/_config/admins/name -d '"secret"'
import couchdb

# Connect to DB
couch = couchdb.Server() # Assuming localhost:5984
db = couch['database'] # assuming database exists
# db = couch.create('database')

# Create a document and insert it into the db:
db['something'] = {'type': 'foo', 'data': 'bar'}

# Return if doc exists
'something' in db

