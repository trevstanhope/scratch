import json

from firebase import firebase
from firebase import jsonutil

firebase = firebase.FirebaseApplication('https://hivemind.firebaseio.com', authentication=None)

def log_user(response):
  with open('/tmp/users/%s.json' % response.keys()[0], 'w') as users_file:
    users_file.write(json.dumps(response, cls=jsonutil.JSONEncoder))

firebase.get_async('/users', None, {'print': 'pretty'}, callback=log_user)
