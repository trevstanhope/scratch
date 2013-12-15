rom firebase import firebase
firebase = firebase.FirebaseApplication('https://hivemind.firebaseio.com', authentication=None)
result = firebase.get('/users', None, {'print': 'pretty'})
print result # {'error': 'Permission denied.'}

authentication = firebase.Authentication('THIS_IS_MY_SECRET', 'ozgurvt@gmail.com', extra={'id': 123})
firebase.authentication = authentication
print authentication.extra # {'admin': False, 'debug': False, 'email': 'ozgurvt@gmail.com', 'id': 123, 'provider': 'password'}

user = authentication.get_user()
print user.firebase_auth_token

result = firebase.get('/users', None, {'print': 'pretty'})
print result # {'1': 'John Doe', '2': 'Jane Doe'}
