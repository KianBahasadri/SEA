# SEA_discord
This is a discord bot that adds security to the SEA discord server

**CURRENTLY NOT FUNCTIONAL**

## End-User Functionality

#### User Authentication and Authorization
Authenticate and authorize new users as they join the server by email verification and classlist cross-reference.

When a user joins the discord server, they will be automatically placed in a waiting channel, and will be instructed (not by the bot) to prompt the bot to verify them.

Once prompted, the bot will ask the user for their school email e.g. "xxxx@university.com" and send a verification code to that email address.

The bot will then ask the user to send the verification code, and once the bot verifies that it is correct the user is now Authenticated.

The bot will now query the local database for all courses which that email address is enrolled in. (The database must be premade by an administrator)

The bot assigns the appropriate discord roles and adds the discord account to the database. The user is now properly Authorized.


## Admin Functionality

#### Classlist parser
Parse a classlist and store it in an SQL database

#### Reset User Authorization
For every user in the server, remove authorization related discord roles and re-assign them based on current database


## Documentation

- **config.json** holds secrets such as the token.
- **index.js** contains the code that operates the bot.
- **package.json** & **package-lock.json** are npm generated files that stores information about this project such as dependencies and package versions. If you run `npm install` these files will be used to install and configure your local environment.
- **commands/** holds the code for slash commands. They are organized in subdirectories, do not put command files directly inside as it will cause errors.
- **deploy-commands.js** deploys each slash command and its description to discord. When slash commands are used, discord notifies your bot. These requests are rate limited by discord so use them sparingly.
- **events/** holds the code for events such as logging in or recieving a message. It works like commands/ but has no subdirectories.
