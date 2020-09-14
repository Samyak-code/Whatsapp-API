#First type "pip install twilio" for windows in cmd
#make an account on twilio sandbox
from twilio.rest import Client 
account_sid = 'ACb4279943a0a58042ebf1195b2fb4a953' 
auth_token = 'Enter your own authentication code. I cannot share mine due to security purposes.' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hello World',      
                              to='whatsapp:+919999164111'#your mobile number 
                          ) 
 
print(message.sid)
