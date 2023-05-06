import imaplib
import email

def status(s):
	RED = "\033[31m"
	GREEN = "\033[32m"

	if s in ("OK"):
		s = GREEN + s
	elif s in ("NO", "ERROR"):
		s = RED + s
	else:
		s = RED + "Unkown error code returned: " + s
	
	return s + "\033[0m"

def bold(t):
	return "\033[1m" + t + "\033[0m"

imap = imaplib.IMAP4_SSL("outlook.office365.com")
imap.login("seadiscordbot@outlook.com", open("PASSWORD", "r").read())

# select the mailbox to read from
imap.select("INBOX")

# search for emails
typ, response = imap.search(None, "ALL")
print(bold("SEA DISCORD BOT EMAIL SCRIPT"))
print(f"\nreading through emails, status: {status(typ)}")

email_ids = response[0].split()

# loop through each email
for email_id in email_ids:
	print("-------------------------------------------------")
	# fetch the email data
	typ, response = imap.fetch(email_id, "(RFC822)")
	print(f"fetching email with id: {email_id}, status: {status(typ)}")
	email_data = response[0][1]

	# parse the email data
	msg = email.message_from_bytes(email_data)
	print(bold("From:"), msg["From"])
	print(bold("Subject:"), msg["Subject"])
	
	text = ""

	# read the content of the email and append to text
	if msg.is_multipart():
		# for multipart emails, iterate through each part
		for part in msg.walk():
			if part.get_content_type() == "text/plain":
				text += part.get_payload()
	else:
		# for non-multipart emails, append body to text
		text = msg.get_payload()

	if len(text) > 100:
		print(f"{status('ERROR')}: BODY NOT SHOWN (over 100 chars)")
	else:
		print(text)
	

# logout of the account and disconnect from the server
imap.logout()

