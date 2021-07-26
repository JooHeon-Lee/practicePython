# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'SID입력'
auth_token = '토큰'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='+', #발신번호
         body='TEST', #내용
         to='+'#받는사람 번호
     )

print(message.sid)