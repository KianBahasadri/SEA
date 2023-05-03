import discord

TOKEN = open("TOKEN", "r").read()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print("we have logged in as {0.user}".format(client))

img_link = "https://media.discordapp.net/attachments/1050570925290045471/1103143212245340200/its_too_late_give_up.jpg"

@client.event
async def on_message(message):
	username = str(message.author)
	user_message = str(message.content)
	channel = str(message.channel.name)
	print(f"{username}: {user_message} ({channel})")
	
	if message.author == client.user:
		return
	
	if message.channel.name == "general":
		if user_message.lower() == "hi":
			await message.channel.send(f"hello {username}!")
			return
		elif user_message == "img":
			await message.channel.send(img_link)
			return
		else:
			await message.channel.send(f"no hi detected, instead user sent {user_message}")
			return

client.run(TOKEN)

