# -*- coding: utf-8 -*-
# @Author kittaaron

from twilio.rest import Client

account_sid = "twilio账号"
auth_token = "twilio32位长token"

client = Client(account_sid, auth_token)

def sendMsg(msg):
    message = client.messages.create(
        #to="+8615622813257",
        to="+8615622813257",
        from_="+18125583488",
        body=msg
)
