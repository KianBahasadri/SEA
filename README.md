# SEA_discord
This is a discord bot project that adds security to the SEA discord server. This project is CURRENTLY NOT FUNCTIONAL.

The sections talking about the Functions are non-technical and explain the purpose of the project.  
The section talking about Documentation is a technical coverage of the inner workings of this project.

## End-User Functions

#### Authentication and Authorization
Users can self-verify using the commands `/verify_email` and `/verify_code`.

Note: The /verify commands should be used in a designated verification channel. The intention is that users will have no privileged channel access until the verification process is complete.

`/verify_email` has one required option, which is the user's school email adddress e.g. "xxxx@university.com". Once this command is sent, a verification code will be sent to that user's email address.

`/verify_code` has one required option, which is the verification code sent to the user's school email address. Once this command is sent and approved, the bot will automatically assign the user's roles.


## Administrative Functions

#### Classlist parser
The script classlist_parser.py can parse a classlist and will store it in **student_info.db**. The script is made with python stored on the server-side, inaccessible through the bot. More details in the documentation section.

#### Reset User Authorization
For either a single user or for every user in the server, remove authorization related discord roles and re-assign them based on the current info in **student_info.db**. This will ideally be used at the start of every semester. Furthermore, if data is changed in **student_info.db**, this can be used to ensure every student is given the proper access.


## Documentation
I did my best to give an overview of this project and go into detail on specific parts.


#### Main Directory Structure
This is what the main directory should look like:

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
- **config.json** holds secrets such as the token and email credentials.
- **events/** holds the code for discord events such as logging in or recieving a message. Imported in index.js
- **index.js** responsible for operating the bot. Imports the code from around the project.
- **student_info.db** holds the student enrollment information


#### Technical Explanation of `/verify_email` and `/verify_code`

When `/verify_email` is called, index.js runs a function it imported from *commands/users/verify_email.js*.
This function logically looks like this:  
```
import imap
import verificationCodes dictionary from utils/
generate secret code
send secret code to email address
Create entry in verificationCodes, key = userid, value = secret code
```
when `/verify_code` is called, it looks like this:  
```
import verificationCodes dictionary from utils/
import addRoles function from untils/
secretCode = verificationCodes[userid]
if commandOption == secretCode:
  reply: success
  run addRoles(emailaddress, discordtag)
else:
  reply: failed
```

When `addRoles.js` is called, it looks like this:
```
import sql
perform the following on student_info.db
select * from students where email="emailaddress"
```

#### Student_info.db
The following is the structure of the tables in **student_info.db**

Students  
| id | firstname | lastname |      email      | verified |   discord    |
|----|-----------|----------|-----------------|----------|--------------|
|  1 | John      | Doe      | johndoe@uni.com | True     | johndoe#0000 |
|  2 | Jane      | Doe      | janedoe@uni.com | False    | NULL         |

Enrollment  
| student-id | course-id | year | semester |
|------------|-----------|------|----------|
|          1 |         1 | 2022 |        2 |
|          1 |         2 | 2022 |        2 |

Courses  
| id |  name   |
|----|---------|
|  1 | math100 |
|  2 | chem100 |





#### utils/
utils/  
├── addRoles.js  
├── checkEmailForCode.js  
├── classlist_parser.py  
└── deploy-commands.js  

- **classlist_parser.py** super hacky parser for the classlist. Details are inside.
- **deploy-commands.js** deploys each slash command and its description to discord. When slash commands are used, discord notifies your bot. These requests are rate limited by discord so use them sparingly.

