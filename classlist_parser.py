"""

I'm making this as a server-side tool because its mad jenk.

usage:
open the classlist
set it to 200 students per page
make sure it is sorted by last name
each row should look like this, { img   Lname,Fname  email  Role }
ctrl+a, ctrl+c, ctrl+v
got it?
dont edit the text, paste it in raw.

"""

print("IMPORTANT NOTE: Please make sure you have read the notes included in this file before using this tool\n")

course_code = input("Please enter the course code, no spaces")
text = input("Please copy and paste the classlist and hit enter").split()

text_size = len(text)
i = 0

# goes to the first "line"
while text[i] != "View":
	i += 1

while i < text_size:
	i += 3
	name = ''

	while ',' not in text[i]:
		i += 1
		name += text[i]
	
	while "@" not in text[i]:
		i += 1
	
	email = text[i]
	role = text[i + 1]
	i += 2





	
	


