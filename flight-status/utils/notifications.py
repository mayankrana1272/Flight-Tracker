import firebase_admin
from firebase_admin import messaging, credentials

# Initialize Firebase Admin SDK (use your service account key)
cred = credentials.Certificate("C:\Users\mrana2\Desktop\flight-status\flight-status-tracker-31ae6-firebase-adminsdk-nx1nu-eb3c2eb8c4.json")
firebase_admin.initialize_app(cred)

def send_push_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body
        ),
        token=token
    )
    response = messaging.send(message)
    print('Successfully sent message:', response)
