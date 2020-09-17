from twilio.rest import TwilioRestClient
from credentials import account_sid, auth_token, my_phone_num, my_twilio_num

# Find these values at https://twilio.com/user/account
client = TwilioRestClient(account_sid, auth_token)

my_msg = "Your message here.."

message = client.messages.create( to=my_phone_num, from_=my_twilio_num, body=my_msg)