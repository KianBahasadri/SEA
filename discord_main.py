import discord
from discord.ext import commands
import smtplib

def send_code(address, message):
	server = smtplib.SMTP("smtp.office365.com", 587)
	server.starttls()
	server.login("seadiscordbot@outlook.com", open("PASSWORD").read())
	server.sendmail("seadiscordbot@outlook.com", address, message)
	server.quit()
	print(f"Verification email sent to {address}")


TOKEN = open("TOKEN").read()

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
	print("Logged in as {0.user}".format(client))


@client.event
async def on_message(message):
	username = str(message.author)
	user_message = str(message.content)
	channel = str(message.channel.name)
	print(f"#{channel}:{username}: {user_message}")
	
	if message.author == client.user:
		return
	
	await message.channel.send(f"hello {username}!")



client.run(TOKEN)


