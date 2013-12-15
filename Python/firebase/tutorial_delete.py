from firebase import firebase
firebase = firebase.FirebaseApplication('https://your_storage.firebaseio.com', None)
firebase.delete('/users', '1')
# John Doe goes away.
