# Imports
import os
from splitwise import Splitwise
from sms import send

# Splitwise Authorization
s = Splitwise(os.getenv("CONSUMER_KEY"),os.getenv("CONSUMER_SECRET"),api_key=os.getenv("API_KEY"))

# Get a list of all groups, without the non-group expenses
myGroups = s.getGroups()[1:]

for i in myGroups:
  # Cycle through groups and get each member
  members = i.getMembers()
  for j in members:
    # For each member, see if they owe money and if they do run the send command in sms.py
    if(float(j.getBalances()[0].getAmount()) < 0):
      send(j.getFirstName(), j.getBalances()[0].getAmount()[1:], i.getName())