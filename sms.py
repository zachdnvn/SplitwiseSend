#Imports
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
 
account_sid = os.getenv("account_sid") 
auth_token = os.getenv("auth_token") 
client = Client(account_sid, auth_token) 

def send(name, amount, group):
  message = client.messages.create (  
    messaging_service_sid=os.getenv("messaging_service_sid") , 
    body='Hey {}! Please pay your Splitwise balance of ${} in {}'.format(name, amount, group),     
    to=os.getenv("{}".format(name)) 
  ) 
