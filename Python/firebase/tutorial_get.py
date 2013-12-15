from firebase import firebase
firebase = firebase.FirebaseApplication('https://hivemind.firebaseio.com', None)

result = firebase.get('/collections', None)
for collection in result.keys():
  for node in result[collection].keys():
    print result[collection][node]

