from flask import Flask, Response, request
from twilio import twiml
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import json
import os


app = Flask(__name__)
app.config['ACCOUNT_SID'] = os.getenv('ACCOUNT_SID')
app.config['AUTH_TOKEN'] = os.getenv('AUTH_TOKEN')

@app.route("/")
def check_app():
    #returns a string so we know that the app is working
    return Response("It works!"), 200

@app.route("/twilio", methods=["POST"])
def inbound_sms():
    data = request.data
    phone_number = json.loads(data)['to']

    client = Client(app.config['ACCOUNT_SID'], app.config['AUTH_TOKEN'])

    message = client.messages \
                    .create(
                        body = "Thank you for signing up for this task!",
                        from_='+17203601358',
                        to = phone_number
                    )
    print(message.sid)

if __name__ == "__main__":
    app.run(debug=True)
