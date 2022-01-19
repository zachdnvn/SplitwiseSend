# Imports
import os
from dotenv import load_dotenv
from operator import ilshift
from splitwise import Splitwise

load_dotenv()
# Splitwise Authorization
s = Splitwise(os.getenv("KEY1"),os.getenv("KEY2"),api_key=os.getenv("API_KEY"))

# User
f = s.getFriends()

# Create array for users
x= [j.getFirstName() for j in f]

# Get list of balance objects for each user
balances = [i.getBalances() for i in f]


for i in balances:
  # If no balance object, balance = 0
  if not i:
      x.append('0')
  for j in i:
    # Add users balance to array
    x.append(j.getAmount())
# print(x)

# Create array for display purposes only lmao
y = []

# Bro
counter = 0

# Imagine this part was not here
while (counter <= 6):
  # Lines up 
  y.append(x[counter])
  y.append(x[counter+7])
  counter += 1
print(y)