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


def get_email_ids():
	# search for unread emails
	typ, response = imap.search(None, "UNSEEN")
	print(f"\nreading through emails, status: {status(typ)}")
	email_ids = response[0].split()
	return email_ids


def search_for_code(code):
	email_ids = get_email_ids()

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

		if len(text) > 200:
			print(f"{status('ERROR')}: BODY NOT SHOWN (over 200 chars)")
		else:
			print(text)
		

def logout():
	imap.logout()


def login():
	global login
	print(bold("EMAIL SCRIPT EXECUTED"))
	imap = imaplib.IMAP4_SSL("outlook.office365.com", port=993)
	imap.login("seadiscordbot@outlook.com", open("PASSWORD", "r").read())

	# select the mailbox to read from
	imap.select("INBOX")


imap = None
