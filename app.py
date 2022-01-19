# Imports
import os
from dotenv import load_dotenv
from operator import ilshift
from splitwise import Splitwise

load_dotenv()
# Splitwise Authorization
s = Splitwise(os.getenv("KEY1"),os.getenv("KEY2"),api_key=os.getenv("API_KEY"))

# Get a list of all groups, without the non-group expenses
myGroups = s.getGroups()[1:]

for i in myGroups:
  members = i.getMembers()
  for j in members:
    print(j.getFirstName(), j.getBalances()[0].getAmount())
    if(float(j.getBalances()[0].getAmount()) < 0):
      pass
