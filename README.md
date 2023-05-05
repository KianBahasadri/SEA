# SEA_discord
This is a discord bot that adds security to the SEA discord server


## End-User Functionality


#### User Authentication and Authorization
Authenticate and authorize new users as they join the server by email verification and classlist cross-reference.

When a user joins the discord server, they will be automatically placed in a waiting channel, and will be instructed (not by the bot) to prompt the bot to verify them.

Once prompted, the bot will give the user a verification code and tell them to send an email containing that code from their school email "xxxx@university.com" to the gmail account "seadiscordbot@gmail.com"

The bot will then check the inbox for unread messages and once it recieves an email with the verification code, the user is now Authenticated.

The bot will now query the local database for all courses which that email address is enrolled in. (The database must be premade by an administrator)

The bot assigns the appropriate discord roles and the user is now properly Authorized.


#### Message anonymization
Anonymize messages so that the identity of the original poster is hidden


## Admin Functionality


#### Classlist parser
Parse a classlist and store it in an SQL database


### Reset User Authorization
For every user in the server, remove authorization related discord roles and re-assign them based on current database


## TODO


- user authentication
- classlist parser
- write documentation
