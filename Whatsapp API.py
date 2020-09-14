from twilio.rest import Client 
 
account_sid = 'ACb4279943a0a58042ebf1195b2fb4a953' 
auth_token = 'a387d42f03d9985163aa2852e6383ffa' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Poochi',      
                              to='whatsapp:+919999164111' 
                          ) 
 
print(message.sid)