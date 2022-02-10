# SplitwiseSend
SplitwiseSend sends an SMS reminder to all users in your Splitwise groups that owe money. 

## How It Works
Using the Splitwise API, the program cycles through all of your groups and sends a text message through the Twilio API to all users who are in debt

## Customization Needed
Ensure that you:
- Download all of the necessary libraries:
  - To use a .env, `pip install python-dotenv`
  - To use the Splitwise API, `pip install splitwise`
  - To use the Twilio API, `pip install twilio`
- In your .env file ensure that you add:
  - Splitwise Consumer Key (called CONSUMER_KEY)
  - Splitwise Consumer Secret (called CONSUMER_SECRET)
  - Splitwise API Key (called API_KEY)
  - Twilio Account SID (called account_sid)
  - Twilio Authentication Token (called auth_token)
  - All of the first names (as seen on Splitwise) and their phone number with area code (save it in your .env in the form firstName = phoneNumber)
