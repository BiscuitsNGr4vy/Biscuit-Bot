import discord
import sys
import os
from discord import app_commands
from discord.ext import commands
import queue
from queue import Queue
import json
import random
import datetime
import helper

BOT_TOKEN = "####### CHANGE THIS##########"
CHANNEL_ID = 1272702872273817721, 1319382305558630530, 1321977877087916092, 1272817130366304276 ## CHANGE THESE FOR YOUR SPECIFIC DISCORD

os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
## bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())  # initialize the bot
client.remove_command('help')

q = Queue(maxsize = 100)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.change_presence(status=discord.Status.online,
                                   activity=discord.Activity(name=f"The Verdant Isle", type=discord.ActivityType.watching))



######################################################## ADVANCED BOT COMMANDS ############################################################

whitelist = {"The Captain", "First Mate", "Quartermasters", "Sailing Master", "Gunners", "Boatswains", "Powder Monkeys", "Pirates", "T-REX Titans", "TEST"}

def custom_cooldown(ctx):
    roles = {role.name for role in ctx.author.roles}
    if not whitelist.isdisjoint(roles):
        #if we're a special role, no cooldown assigned
        return None
    elif "Ptero Pals" in roles:
        #some other privileged role
        discord.app_commands.Cooldown(1, 1200)
    elif "TRIKE Trailblazers" in roles:
        #some other privileged role
        discord.app_commands.Cooldown(1, 900)
    elif "Raptor Royalty" in roles:
        #some other privileged role
        discord.app_commands.Cooldown(1, 300)
    else:
        #everyone else
        return discord.app_commands.Cooldown(1, 3600)
    
########################################################################DISCORD COMMANDS########################################################################################

@client.event
async def on_message(message):
    ctx = await client.get_context(message)
    await client.invoke(ctx)


################################################################################################################################################################################
##########################Other Commands###############################
class Select2(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="ANKY - 100"),
            discord.SelectOption(label="ACRO - 100"),
            discord.SelectOption(label="CAMARA - 100"),
            discord.SelectOption(label="PUERTA - 100"),
            discord.SelectOption(label="SUCHO - 100"),
            discord.SelectOption(label="STEGO - 100"),
            discord.SelectOption(label="SHANT - 100"),
            discord.SelectOption(label="SPINO - 100"),
            discord.SelectOption(label="REX - 100"),
            discord.SelectOption(label="VELO - 100")
            ]
        super().__init__(placeholder="Donor Dinos",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        try:
            if self.values[0] == "ANKY - 100":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 100
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Anky'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "CAMARA - 100":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 100
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Camara'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "PUERTA - 100":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 100
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Puerta'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "SHANT - 100":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 100
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Shant'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "STEGO - 100":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 100
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Stego'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "ACRO - 100":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 100
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Acro'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "SPINO - 100":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 100
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Spino'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "SUCHO - 100":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 100
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'SuchoAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "REX - 100":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 100
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'RexAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "VELO - 100":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 100
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Velo'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)
                        
        except Exception as e:
            print(e)
            pass

class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="AUSTRO - 250"),
            discord.SelectOption(label="AVA - 250"),
            discord.SelectOption(label="DIABLO - 250"),
            discord.SelectOption(label="DRYO - 250"),
            discord.SelectOption(label="GALLI - 250"),
            discord.SelectOption(label="MAIA - 250"),
            discord.SelectOption(label="ORO - 250"),
            discord.SelectOption(label="PACHY - 250"),
            discord.SelectOption(label="TACO - 250"),
            discord.SelectOption(label="HERRERA - 250"),
            discord.SelectOption(label="THERI - 250"),
            discord.SelectOption(label="TRIKE - 250"),    
            discord.SelectOption(label="ALBERT - 250"),
            discord.SelectOption(label="ALLO - 250"),
            discord.SelectOption(label="UTAH - 250"),
            discord.SelectOption(label="BARY - 250"),
            discord.SelectOption(label="CARNO - 250"),
            discord.SelectOption(label="CERATO - 250"),
            discord.SelectOption(label="DILO - 250"),
            discord.SelectOption(label="GIGA - 250")
            ]
        super().__init__(placeholder="Standard Dinos",max_values=1,min_values=1,options=options)
        
    async def callback(self, interaction: discord.Interaction):
        try:
            if self.values[0] == "AUSTRO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Austro'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "AVA - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Ava'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                        #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "CAMARA - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Camara'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "DIABLO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'DiabloAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "DRYO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'DryoAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "GALLI - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'GalliAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "MAIA - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'MaiaAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "ORO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Oro'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "PACHY - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'PachyAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "TACO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Taco'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "PUERTA - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Puerta'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "SHANT - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Shant'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "STEGO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Stego'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "THERI - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Theri'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "TRIKE - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'TrikeAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "ACRO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Acro'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "ALBERT - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Albert'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "ALLO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'AlloAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "BARY - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Bary'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "CARNO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'CarnoAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "CERATO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'CeratoAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "DILO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'DiloAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "GIGA - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'GigaAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "HERRERA - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Herrera'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "SPINO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Spino'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "SUCHO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'SuchoAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "REX - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'RexAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "UTAH - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                                
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'UtahAdultS'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 

                    for element in q.queue:
                        print(element)

            elif self.values[0] == "VELO - 250":
                await interaction.response.send_message(content="Swapping Dino please wait...", ephemeral=True)
                print(q.qsize())                                                                               
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        print(user)
                        data_path = 'C:/Users/Olden/Desktop/The Isle Legacy/servers/1/serverfiles/TheIsle/Saved/Databases/Survival/Players/' + str(user) + '.json'  
                    with open(data_path, 'r') as jsonfile:
                        data = json.load(jsonfile)
                        data["CharacterClass"] = 'Velo'
                        data["Growth"] = '1.0'
                        data["Hunger"] = '9999'
                        data["Thirst"] = '9999'
                        data["Health"] = '9999'
                        data["BleedintRate"] = '0'
                        data["Oxygen"] = '40'
                        data["bBrokenLegs"] = 'false'
                        jsonfile.seek(0)


                        # Open the JSON file for writing 
                    #os.remove(data_path)
                    with open(data_path, 'w') as f: 
                        json.dump(data, f, indent=4) 
                    for element in q.queue:
                        print(element)

        except Exception as e:
            print(e)
            pass


class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 60):
        super().__init__(timeout=timeout)
        self.add_item(Select())


class SelectView2(discord.ui.View):
    def __init__(self, *, timeout = 60):
        super().__init__(timeout=timeout)
        self.add_item(Select2())



@client.command()
@commands.cooldown(1,900,commands.BucketType.user)    ## Cooldown Timer 15min 
async def swap(ctx):
    try:
        await helper.open_account(ctx.author)

        bal = await helper.update_bank(ctx.author)

        if bal[0]<250:
            await ctx.reply("You dont have enough Dino Doubloons!")
        else:
            await ctx.reply("Sending Dino Menu...", ephemeral=True)
            await ctx.author.send("Dino Menu:",view=SelectView())
            q.put('Dino Swap Command')
            ctx.command.reset_cooldown(ctx)
            for element in q.queue:
                print(element) 
    except Exception as e:
        print(e)
        pass

@client.command()
@commands.cooldown(1,900,commands.BucketType.user)
async def donoswap(ctx):
    try:
        await helper.open_account(ctx.author)

        bal = await helper.update_bank(ctx.author)

        if bal[0]<100:
            await ctx.reply("You dont have enough Dino Doubloons!")
        else:
            await ctx.reply("Sending Dino Menu...", ephemeral=True)
            await ctx.author.send("Dino Menu:",view=SelectView2())
            q.put('Dino Swap Command')
            ctx.command.reset_cooldown(ctx)
            for element in q.queue:
                print(element) 
    except Exception as e:
        print(e)
        pass

@client.command()
@commands.has_any_role("Boatswains", "Sailing Master", "Quartermasters", "First Mate", "The Captain", "Gunners", "TEST")
async def adminswap(ctx):
    try:
        await ctx.reply("Sending Dino Menu...", ephemeral=True)
        await ctx.author.send("Dino Menu:",view=SelectView())
        await ctx.author.send(view=SelectView2())
        q.put('Dino Swap Command')   
        for element in q.queue:
            print(element) 
    except Exception as e:
        print(e)
        pass


@client.command()
async def bal(ctx):
    try:
        await helper.open_account(ctx.author)
        user = ctx.author
        users = await helper.get_bank_data()

        wallet_amount = users[str(user.id)]["wallet"]
        bank_amount = users[str(user.id)]["bank"]

        em = discord.Embed(title= f"Dino Doubloons",color = discord.Color.green())
        em.add_field(name = "Wallet Balance",value = wallet_amount)
        em.add_field(name = "Bank Balance",value = bank_amount)
        await ctx.reply(embed = em)
    except Exception as e:
        print(e)
        pass



@client.command()
async def balance(ctx):
    try:
        await helper.open_account(ctx.author)
        user = ctx.author
        users = await helper.get_bank_data()

        wallet_amount = users[str(user.id)]["wallet"]
        bank_amount = users[str(user.id)]["bank"]

        em = discord.Embed(title= f"Dino Doubloons",color = discord.Color.green())
        em.add_field(name = "Wallet Balance",value = wallet_amount)
        em.add_field(name = "Bank Balance",value = bank_amount)
        await ctx.reply(embed = em)
    except Exception as e:
        print(e)
        pass


@client.command()
@commands.cooldown(1,3600,commands.BucketType.user)     ## Cooldown Timer 1hr 
async def beg(ctx):
    try:
        await helper.open_account(ctx.author)

        users = await helper.get_bank_data()

        user = ctx.author

        earnings = random.randrange(101)

        await ctx.reply(f"You found {earnings} Dino Doubloons in the trash!")

        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json","w") as f:
            json.dump(users,f)
    except Exception as e:
        print(e)
        pass

@client.command()
@commands.cooldown(1,10800,commands.BucketType.user)    ## Cooldown Timer 3hr 
async def work(ctx):
    try:
        await helper.open_account(ctx.author)
        user = ctx.author
        users = await helper.get_bank_data()

        earnings = 500

        await ctx.reply(f"You earned {earnings} Dino Doubloons!")

        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json","w") as f:
            json.dump(users,f)
    except Exception as e:
        print(e)
        pass


@client.command()
@commands.cooldown(1,86400,commands.BucketType.user)    ## Cooldown Timer 24hr 
async def daily(ctx):
    try:
        await helper.open_account(ctx.author)
        user = ctx.author
        users = await helper.get_bank_data()

        earnings = 750

        await ctx.reply(f"You earned {earnings} Dino Doubloons!")

        users[str(user.id)]["wallet"] += earnings

        with open("mainbank.json","w") as f:
            json.dump(users,f)
    except Exception as e:
        print(e)
        pass


@client.command()
async def withdraw(ctx, amount = None):
    try:
        await helper.open_account(ctx.author)

        if amount == None:
            await ctx.reply("Please enter the amount")
            return

        bal = await helper.update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[1]:
            await ctx.reply("You dont have enough Dino Doubloons!")
            return
        
        if amount<0:
            await ctx.reply("Amount must be positive!")
            return

        await helper.update_bank(ctx.author, amount)
        await helper.update_bank(ctx.author, -1*amount, "bank")
        await ctx.reply(f"You withdrew {amount} Dino Doubloons!")
    except Exception as e:
        print(e)
        pass


@client.command()
async def deposit(ctx, amount = None):
    try:
        await helper.open_account(ctx.author)

        if amount == None:
            await ctx.reply("Please enter the amount")
            return

        bal = await helper.update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[0]:
            await ctx.reply("You dont have enough Dino Doubloons!")
            return
        
        if amount<0:
            await ctx.reply("Amount must be positive!")
            return

        await helper.update_bank(ctx.author, -1*amount)
        await helper.update_bank(ctx.author, amount, "bank")
        await ctx.reply(f"You deposited {amount} Dino Doubloons!")
    except Exception as e:
        print(e)
        pass


@client.command()
async def dep(ctx, amount = None):
    try:
        await helper.open_account(ctx.author)

        if amount == None:
            await ctx.reply("Please enter the amount")
            return

        bal = await helper.update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[0]:
            await ctx.reply("You dont have enough Dino Doubloons!")
            return
        
        if amount<0:
            await ctx.reply("Amount must be positive!")
            return

        await helper.update_bank(ctx.author, -1*amount)
        await helper.update_bank(ctx.author, amount, "bank")
        await ctx.reply(f"You deposited {amount} Dino Doubloons!")
    except Exception as e:
        print(e)
        pass


@client.command()
async def send(ctx, member:discord.Member, amount = None):
    try:
        await helper.open_account(ctx.author)
        await helper.open_account(member)

        if amount == None:
            await ctx.reply("Please enter the amount")
            return

        bal = await helper.update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[1]:
            await ctx.reply("You dont have enough Dino Doubloons!")
            return
        
        if amount<0:
            await ctx.reply("Amount must be positive!")
            return

        await helper.update_bank(ctx.author, -1*amount, "bank")
        await helper.update_bank(member, amount, "bank")
        await ctx.reply(f"You sent {amount} Dino Doubloons!")
    except Exception as e:
        print(e)
        pass

@client.command()
@commands.cooldown(1,3600,commands.BucketType.user)     ## Cooldown Timer 1hr 
async def rob(ctx, member:discord.Member):
    try:
        await helper.open_account(ctx.author)
        await helper.open_account(member)

        bal = await helper.update_bank(member)

        if bal[0]<100:
            await ctx.reply("They dont have any Dino Doubloons!")
            return
        
        earnings = random.randrange(0, bal[0])

        await helper.update_bank(ctx.author, earnings)
        await helper.update_bank(member, -1*earnings)
        await ctx.reply(f"You mugged {member} for {earnings} Dino Doubloons!")
    except Exception as e:
        print(e)
        pass


@client.command()
async def slots(ctx, amount = None):
    try:
        await helper.open_account(ctx.author)

        if amount == None:
            await ctx.reply("Please enter the amount")
            return

        bal = await helper.update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[0]:
            await ctx.reply("You dont have enough Dino Doubloons!")
            return
        
        if amount<0:
            await ctx.reply("Amount must be positive!")
            return

        final = []
        for i in range(3):
            a = random.choice([":volcano: ", ":sauropod:", ":t_rex:"])

            final.append(a)

        await ctx.reply(str(final))


        if final[0] == final[1] or final[0] == final[2] or final[1] == final[2]:
            await helper.update_bank(ctx.author, 2*amount)
            await ctx.reply(f"You won {amount} Dino Doubloons!")
        else:
            await helper.update_bank(ctx.author, -1*amount) 
            await ctx.reply(f"You lost {amount} Dino Doubloons!")
    except Exception as e:
        print(e)
        pass



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        remaining_time = str(datetime.timedelta(seconds=int(error.retry_after)))

        embed = discord.Embed(title=":clock1: The Verdant Isle", description=f'{ctx.author.mention}, Cooldown Remaining: ' + str(remaining_time), color=0xE74C3C)
        await ctx.reply(embed=embed)

#    if isinstance(error, commands.CommandOnCooldown):    ## Checks for Cooldown
#        msg = 'Cooldown Remaining: {:.0f}s'.format(error.retry_after)
#        await ctx.reply(msg)


client.run(BOT_TOKEN)
## bot.run(BOT_TOKEN)      
