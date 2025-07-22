import discord
import sys
import os
from discord import app_commands
from discord.ext import commands


BOT_TOKEN = "############CHANGE ME###########"
CHANNEL_ID = 1272702872273817721, 1319382305558630530, 1321977877087916092, 1272817130366304276, 1273879215565181053 ## CHANGE THIS FOR YOUR SPECIFIC DISCORD


client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
## bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())  # initialize the bot
client.remove_command('help')


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.change_presence(status=discord.Status.online,
                                   activity=discord.Activity(name=f"The Verdant Isle", type=discord.ActivityType.watching))
    
########################################################################DISCORD COMMANDS########################################################################################


@client.event
async def on_message(message):
    ctx = await client.get_context(message)
    await client.invoke(ctx)


@client.event
async def on_message(message):
    if message.content.startswith("!link"):
        try:
            os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
            
            if (message.content[5:].lstrip().replace(" ", "") == "" or message.content[5:].lstrip() == "delete" or message.content[5:].lstrip() == "remove"):
                if (os.path.exists(os.path.join(os.getcwd(), "steamids", str(message.author.name) + ".desc.txt"))):
                    os.remove(os.path.join(os.getcwd(), "steamids", str(message.author.name) + ".desc.txt"))

                    await message.author.send("Your Steam 64 ID has been removed.")
                else:
                    await message.author.send("Unable to remove your Steam ID, because you don't have one. Use !link ############ to link your 17 digit Steam 64 ID")
            else:
                with open(os.path.join(os.getcwd(), "steamids", str(message.author.name) + ".desc.txt"), "w") as descriptionFile:
                    descriptionFile.write(message.content[5:].lstrip())

                await message.author.send("Your Steam 64 ID has been saved. Use !steamid to verify your steam is correct or !link remove to change the Steam 64 ID")
        except Exception as e:
            print(e)
            print('BOT ERROR')
            
    if message.content.startswith("!steamid"):
        try:
            os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
            userId = (message.author.name).format(message)

            descriptionPath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")

            if (os.path.exists(descriptionPath)):
                with open(descriptionPath) as descriptionFile:
                    await message.author.send(descriptionFile.read())
                    await message.author.send("If your Steam 64ID is correct, you can proceed to https://discord.com/channels/306822100499300352/1273879100616085536")
            else:
                await message.author.send("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")   
        except Exception as e:
            print(e)
            print('BOT ERROR')


client.run(BOT_TOKEN)  
