## C:\\servers\\theisle\\TheIsle\\Saved\\Logs\\TheIsle.log
import discord
from discord.ext import commands, tasks
import re
import queue
import time
import random
import os
import traceback



BOT_TOKEN = "########CHANGE ME########"
CHANNEL_ID = 1276341680550842378 ## CHANGE THIS FOR YOUR SPECIFIC DISCORD

intents = discord.Intents.default()
intents.message_content = True

## client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())  # initialize the bot
bot.remove_command('help')


## C:\Users\Olden\Desktop\PythonBot\chatcoms
## C:\Users\Olden\Documents\TheIsleEvrimaServer\TheIsle\Saved\Logs

filename = 'C:\\Users\\Olden\\Documents\\TheIsleEvrimaServer\\TheIsle\\Saved\\Logs\\TheIsle-Shipping.log'

chatcmd = 'C:\\Users\\Olden\\Desktop\\PythonBot\\chatcoms\\usercommands.txt'

slaycmd = 'C:\\Users\\Olden\\Desktop\\PythonBot\\chatcoms\\queuedcoms.txt'

foodcmd = 'C:\\Users\\Olden\\Desktop\\PythonBot\\chatcoms\\feedingthem.txt'

emptycmd = 'C:\\Users\\Olden\\Desktop\\PythonBot\\chatcoms\\drainingthem.txt'

chatlog = 'C:\\Users\\Olden\\Desktop\\PythonBot\\chatcoms\\chatlog.txt'

joinleavecmd = 'C:\\Users\\Olden\\Desktop\\PythonBot\\chatcoms\\joinleave.txt'



@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    myloop.start()
    twoloop.start()
    await bot.change_presence(status=discord.Status.online,
                            activity=discord.Activity(name=f"The Verdant Isle", type=discord.ActivityType.watching))

@tasks.loop(seconds=1)
async def myloop():
    channel = bot.get_channel(CHANNEL_ID)
    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!grow" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:   
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrgrow " + result)
                    #print(result)
                    with open(chatcmd, "a+") as commands:
                        commands.seek(0) # set position to start of file
                        lines = commands.read().splitlines() 
                        if final in lines:
                            None
                            # print('val ready exists in file')
                        else:
                            # write to file
                            commands.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass


    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!GROW" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:   
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrgrow " + result)
                    #print(result)
                    with open(chatcmd, "a+") as commands:
                        commands.seek(0) # set position to start of file
                        lines = commands.read().splitlines() 
                        if final in lines:
                            None
                            # print('val ready exists in file')
                        else:
                            # write to file
                            commands.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass


    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!slay" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrslay " + result)
                    #print(result)
                    with open(slaycmd, "a+") as slaycommand:
                        slaycommand.seek(0) # set position to start of file
                        lines = slaycommand.read().splitlines() 
                        if final in lines:
                            None
                            # print('val ready exists in file')
                        else:
                            # write to file
                            slaycommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass

    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!SLAY" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrslay " + result)
                    #print(result)
                    with open(slaycmd, "a+") as slaycommand:
                        slaycommand.seek(0) # set position to start of file
                        lines = slaycommand.read().splitlines() 
                        if final in lines:
                            None
                            # print('val ready exists in file')
                        else:
                            # write to file
                            slaycommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass

    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!kill" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrslay " + result)
                    #print(result)
                    with open(slaycmd, "a+") as slaycommand:
                        slaycommand.seek(0) # set position to start of file
                        lines = slaycommand.read().splitlines() 
                        if final in lines:
                            None
                            # print('val ready exists in file')
                        else:
                            # write to file
                            slaycommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass

    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!KILL" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrslay " + result)
                    #print(result)
                    with open(slaycmd, "a+") as slaycommand:
                        slaycommand.seek(0) # set position to start of file
                        lines = slaycommand.read().splitlines() 
                        if final in lines:
                            None
                            # print('val ready exists in file')
                        else:
                            # write to file
                            slaycommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass

    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!hunger" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:               
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrfood " + result)
                    #print(result)
                    with open(foodcmd, "a+") as foodcommand:
                        foodcommand.seek(0) # set position to start of file
                        lines = foodcommand.read().splitlines() 
                        if final in lines:
                            None
                            # print('val ready exists in file')
                        else:
                            # write to file
                            foodcommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass

    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!feed" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:               
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrfood " + result)
                    #print(result)
                    with open(foodcmd, "a+") as foodcommand:
                        foodcommand.seek(0) # set position to start of file
                        lines = foodcommand.read().splitlines() 
                        if final in lines:
                            None
                            # print('val ready exists in file')
                        else:
                            # write to file
                            foodcommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass

    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!food" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:               
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrfood " + result)
                    #print(result)
                    with open(foodcmd, "a+") as foodcommand:
                        foodcommand.seek(0) # set position to start of file
                        lines = foodcommand.read().splitlines() 
                        if final in lines:
                            None
                            # print('val ready exists in file')
                        else:
                            # write to file
                            foodcommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass


    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!FOOD" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:               
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrfood " + result)
                    #print(result)
                    with open(foodcmd, "a+") as foodcommand:
                        foodcommand.seek(0) # set position to start of file
                        lines = foodcommand.read().splitlines() 
                        if final in lines:
                            None
                            # print('val ready exists in file')
                        else:
                            # write to file
                            foodcommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass


    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!empty" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrempty " + result)
                    #print(result)
                    with open(emptycmd, "a+") as emptycommand:
                        emptycommand.seek(0) # set position to start of file
                        lines = emptycommand.read().splitlines() 
                        if final in lines:
                            None
                        # print('val ready exists in file')
                        else:
                        # write to file
                            emptycommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass

    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!EMPTY" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrempty " + result)
                    #print(result)
                    with open(emptycmd, "a+") as emptycommand:
                        emptycommand.seek(0) # set position to start of file
                        lines = emptycommand.read().splitlines() 
                        if final in lines:
                            None
                        # print('val ready exists in file')
                        else:
                        # write to file
                            emptycommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass

    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!drain" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrempty " + result)
                    #print(result)
                    with open(emptycmd, "a+") as emptycommand:
                        emptycommand.seek(0) # set position to start of file
                        lines = emptycommand.read().splitlines() 
                        if final in lines:
                            None
                        # print('val ready exists in file')
                        else:
                        # write to file
                            emptycommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass

    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "!DRAIN" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:
                    result = get_text_in_nth_brackets(user, 4)
                    final = ("!afwwrempty " + result)
                    #print(result)
                    with open(emptycmd, "a+") as emptycommand:
                        emptycommand.seek(0) # set position to start of file
                        lines = emptycommand.read().splitlines() 
                        if final in lines:
                            None
                        # print('val ready exists in file')
                        else:
                        # write to file
                            emptycommand.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass     
'''
    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "LogTheIsleJoinData" and "Save" in last_line:
                user = last_line
                def get_text_in_nth_brackets(user, n):

                    pattern = r"\[(.*?)\]"  
                    matches = re.findall(pattern, user)

                    if len(matches) >= n:
                        return matches[n - 0]  
                    else:
                        return None  # Return None if there are not enough sets of brackets
                try:
                    result = get_text_in_nth_brackets(user, 4)
                    final = (f"Joined: ", result)
                    #print(result)
                    with open(joinleavecmd, "a+") as joinleave:
                        joinleave.seek(0) # set position to start of file
                        lines = joinleave.read().splitlines() 
                        if final in lines:
                            None
                        # print('val ready exists in file')
                        else:
                        # write to file
                            joinleavecmd.write(final + "\n") 
                            await channel.send(final)
                except:
                    await channel.send('Bot Bugged Out')
                    print('Bot Bugged Out')
                    pass   
'''

'''
    with open(filename, encoding="utf-8") as file:           
            lines = file.readlines()
            last_line = lines[-1]
            if "LogTheIsleJoinData" and "Left" in last_line:
                try:
                   final = ("Player Left")
                   await channel.send(final)
                except:
                   await channel.send('Bot Bugged Out')
                   print('Bot Bugged Out')
                   pass
'''
                   

@tasks.loop(seconds=2700)
async def twoloop():
    channel = bot.get_channel(CHANNEL_ID)
    random_num = random.randint(1,5)
    if random_num == 1:
        await channel.send('!sendann Welcome to The Verdant Isle! Join our Discord from the Server Browser to gain access to more of our custom commands!')
    elif random_num == 2:
        await channel.send('!sendann To use the Bot, simply type one of our commands into Local or Global chat! If you have any issues reach out to us on our Discord!')
    elif random_num == 3:
        await channel.send('!sendann Game Chat Commands currently do not work if you have brackets in your Username! Join our Discord to gain access to commands!')
    elif random_num == 4:
        await channel.send('!sendann If you are enjoying the Server, invite your friends! Here at The Verdant Isle, we welcome everyone.')
    elif random_num == 5:
        await channel.send('!sendann Check out our Patreon for exclusive perks in our Discord!')



bot.run(BOT_TOKEN)
