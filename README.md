# SEA_discord
This is a discord bot that adds security to the SEA discord server

**CURRENTLY NOT FUNCTIONAL**

## End-User Uses

#### Authentication and Authorization using `/verify_email` and `/verify_code`
Note: The /verify commands should be used in a designated verification channel. The intention is that users will have no privileged channel access until the verification process is complete.

`/verify_email` has one required option, which is the user's school email adddress e.g. "xxxx@university.com". Once this command is sent, a verification code will be sent to that user's email address.

`/verify_code` has one required option, which is the verification code sent to the user's school email address. Once this command is sent and approved, the bot will automatically assign the user's roles.


## Admin Uses

#### Classlist parser
The script
Parse a classlist and store it in an SQL database

#### Reset User Authorization
For every user in the server, remove authorization related discord roles and re-assign them based on current database


## Documentation
I did my best to give an overview of this project and go into detail on specific parts.


#### Directory Structure
This is what the directory structure should look like in production:

SEA_discord/
├── commands/
├── config.json
├── events/
├── index.js
├── node_modules/
├── package.json
├── package-lock.json
├── README.md
├── student_info.db
└── utils/


- **commands/** hold the code for slash commands in subdirectories. Imported in index.js
- **config.json** holds secrets such as the token.
- **events/** holds the code for discord events such as logging in or recieving a message. Imported in index.js
- **index.js** responsible for operating the bot. Imports the code from around the project.
- **student_info.db** holds the student enrollment information


#### Student_info.db
The following is the structure of **student_info.db**

Students
+----+----------+----------+
| id | fistname | lastname |
+----+----------+----------+
|  1 | John     | Doe      |
+----+----------+----------+

Enrollment
+------------+-----------+------+----------+
| student-id | course-id | year | semester |
+------------+-----------+------+----------+
|          1 |         1 | 2022 |        1 |
|          1 |         2 | 2022 |        2 |
+------------+-----------+------+----------+

Courses
+----+---------+
| id |  name   |
+----+---------+
|  1 | math100 |
|  2 | chem100 |
+----+---------+



#### utils/
utils/
├── addRoles.js
├── checkEmailForCode.js
├── classlist_parser.py
└── deploy-commands.js

- **classlist_parser.py** super hacky parser for the classlist. Details are inside.
- **deploy-commands.js** deploys each slash command and its description to discord. When slash commands are used, discord notifies your bot. These requests are rate limited by discord so use them sparingly.

