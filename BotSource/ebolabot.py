import discord
import json
from discord.ext.commands import Bot

BOT_PREFIX = ("?")
with open("../auth.json", 'r') as f:
	tokenstore = json.load(f)
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="Making a    bot"))

@client.command(name ='test',
				description="tests the bots new mode",
				brief="test",
				pass_context=True)
async def Test(context):
	await client.say("I exceed opperating params" + " " + context.message.author.mention)


@client.command(name = 'AssignDestiny',
				description="Gives requesters access to the destiny category",
				brief="Request Destiny access",
				pass_context=True)
async def AssignDestiny(context):
	user = context.message.author
	role = discord.utils.get(user.server.roles, name="Destiny")
	await client.add_roles(user,role)
	await client.say("I have assinged you the destiny role" + ", " + context.message.author.mention)
	print("gave user destiny role")



print("launching")
client.run(tokenstore["token"])
