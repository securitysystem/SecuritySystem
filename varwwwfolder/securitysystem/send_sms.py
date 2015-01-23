from twilio.rest import TwilioRestClient
import sys
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACd1d57dcb9013217d1a0b7562b0c1fc80"
auth_token = "4826ddd998d9a798a037208ba284fbc7"
client = TwilioRestClient(account_sid, auth_token)
message = client.messages.create(body=sys.argv[2],
to=sys.argv[1], # Replace with your phone number
from_="+14085604471") # Replace with your Twilio number
print message.sid
