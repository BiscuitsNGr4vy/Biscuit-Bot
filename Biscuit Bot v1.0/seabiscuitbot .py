import discord
import sys
import os
from sys import exit
from discord.ext import commands
import pyautogui
import queue
from queue import Queue
import asyncio
import random
import logging
import helper
import datetime


# MOUSE CONTROL FUNCTIONS
# print(pyautogui.size())
# moveTo() function - moving the mouse from point A to point B on the x/left&right and y/up&down axis "pyautogui.moveTo(300, 300, duration=3)"
# moveRel function - moves the mouse relative to its previous position "pyautogui.moveRel(0,50, duration=2)
# moves mouse to specified x and y then clicks at a duration of 1sec "pyautogui.click(70, 20, duration=1)"
# moves scroll wheel integer number neg for down or pos for up "pyautogui.scroll(-200)"

# HOTKEY FUNCTIONS
# pyautogui.hotkey('ctrlleft', 'a') Emulates Hotkey on Keyboard

# KEYBOARD FUNCTIONS
# pyautogui.typewrite('TEXT TO TYPE HERE') Types Text AND can press 'enter'

#Example for click to type on location: 
# pyautogui.click(400, 700, duration=1)
# pyautogui.typewrite('THIS IS A TEST')

# ctx - context (information about how the command was executed)


############################################################################################################################################


BOT_TOKEN = "########CHANGE THIS##########"
CHANNEL_ID = 1273474325365915712, 1273879100616085536 ## CHANGE THESE FOR YOUR SPECIFIC DISCORD

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client.remove_command('help')
# bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())  # initialize the bot

logging.basicConfig(filename='bots.log', level=logging.ERROR, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

q = Queue(maxsize = 100)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await client.change_presence(status=discord.Status.online,
                                   activity=discord.Activity(name=f"TVI Queue: " + str(q.qsize()), type=discord.ActivityType.watching))
    
async def on_ready():
    while True:
        await client.change_presence(status=discord.Status.online,
                                   activity=discord.Activity(name=f"TVI Queue: " + str(q.qsize()), type=discord.ActivityType.watching))
    
#
#@client.command(name= 'restart')
#async def restart(ctx):
#  await ctx.send("Restarting bot...")
#  await client.logout()
#  sys.exit(0)
#

    
######################################################## ADVANCED BOT COMMANDS ############################################################

whitelist = {"The Captain", "First Mate", "Quartermasters", "Sailing Master", "Gunners", "Boatswains", "Powder Monkeys", "Pirates", "T-Rex Titans", "TEST"}

def custom_cooldown(ctx):
    roles = {role.name for role in ctx.author.roles}
    if not whitelist.isdisjoint(roles):
        #if we're a special role, no cooldown assigned
        return None
    elif "Ptero Pals" in roles:
        #some other privileged role
        discord.app_commands.Cooldown(1, 1200)
    elif "Trike Trailblazers" in roles:
        #some other privileged role
        discord.app_commands.Cooldown(1, 900)
    elif "Raptor Royalty" in roles:
        #some other privileged role
        discord.app_commands.Cooldown(1, 300)
    else:
        #everyone else
        return discord.app_commands.Cooldown(1, 3600)

###################################################################GAME CHAT COMMANDS##########################################################################################

@client.event
async def on_message(message):
    ctx = await client.get_context(message)
    await client.invoke(ctx)


@client.command()
async def afwwrgrow(ctx, mess):
        try:
            print(q.qsize()) 
            q.put('Game Chat Grow Command Executed')
            await ctx.send("Growing Dino...")
            pyautogui.click(1298, 442, duration=1)  ## STEAM ID BOX (1298, 442)
            pyautogui.hotkey('ctrlleft', 'a', duration=1)
            pyautogui.press('backspace')
            pyautogui.hotkey('ctrlleft', 'a', duration=1)
            pyautogui.press('backspace')
            pyautogui.typewrite((mess))  
            pyautogui.click(253, 521, duration=5)  
            pyautogui.typewrite('100')  
            pyautogui.click(258, 503, duration=1)
            for element in q.queue:
                print(element) 
        except Exception as e:
            print(e)
            logger.exception("An error occurred: %s", e)
            pass



@client.command()
async def afwwrslay(ctx, mess):
        try:
            print(q.qsize()) 
            q.put('Game Chat Slay Command Executed')
            await ctx.send("Killing Dino...")
            pyautogui.click(1298, 442, duration=1)   ## STEAM ID BOX (1298, 442)
            pyautogui.hotkey('ctrlleft', 'a', duration=1)
            pyautogui.press('backspace')
            pyautogui.hotkey('ctrlleft', 'a', duration=1)
            pyautogui.press('backspace')
            pyautogui.typewrite((mess))
            pyautogui.click(139, 548, duration=5)
            for element in q.queue:
                print(element)
        except Exception as e:
            print(e)
            logger.exception("An error occurred: %s", e)
            pass


@client.command()                                                    ## EMPTY STOMACH TO 0%
async def afwwrempty(ctx, mess):
        try:
            print(q.qsize()) 
            q.put('Game Chat Empty Command Executed')
            await ctx.send("Draining Food...")
            pyautogui.click(1298, 442, duration=1)
            pyautogui.hotkey('ctrlleft', 'a', duration=1)
            pyautogui.press('backspace')
            pyautogui.hotkey('ctrlleft', 'a', duration=1)
            pyautogui.press('backspace')
            pyautogui.typewrite((mess))
            pyautogui.click(323, 518, duration=5) 
            pyautogui.typewrite('0')
            pyautogui.click(331, 497, duration=1) 
            for element in q.queue:
                print(element)
        except Exception as e:
            print(e)
            logger.exception("An error occurred: %s", e)
            pass


@client.command()                                                                                       ## GIVES 30% FOOD
async def afwwrfood(ctx, mess):
        try:
            print(q.qsize()) 
            q.put('Game Chat Food Command Executed')
            await ctx.reply("Feeding Dino...")
            pyautogui.click(1298, 442, duration=1)
            pyautogui.hotkey('ctrlleft', 'a', duration=1)
            pyautogui.press('backspace')
            pyautogui.hotkey('ctrlleft', 'a', duration=1)
            pyautogui.press('backspace')
            pyautogui.typewrite((mess))
            pyautogui.click(323, 518, duration=5) 
            pyautogui.typewrite('30')
            pyautogui.click(331, 497, duration=1)
            for element in q.queue:
                print(element)
        except Exception as e:
            print(e)
            logger.exception("An error occurred: %s", e)
            pass



########################################################################DISCORD COMMANDS########################################################################################


@client.command()
async def help(ctx):
    try:
        await ctx.reply("Sending Commands List")
        em = discord.Embed(title= f"Evrima Commands:",color = discord.Color.green())
        em.add_field(name = "!tp", value="[15m Cooldown or 250DD] Teleport to a new location! (Sends List in DM)", inline=False)
        em.add_field(name = "!slowgrow", value="[1hr Cooldown or 100DD] Slowly Grows to give Player time to select each Mutations with Perfect Diet and Full Hunger.", inline=False)   
        em.add_field(name = "!grow", value="[1hr Cooldown or 50DD] Fast Grows Player and bypasses Mutations.", inline=False)
        em.add_field(name = "!shrink", value="[1hr Cooldown or 100DD] Shrinks Player!", inline=False)   
        em.add_field(name = "!slay", value="[15m Cooldown or 25DD] Kills Player!", inline=False)
        em.add_field(name = "!diet", value="[30m Cooldown or 100DD] Sets perfect diet.", inline=False)   
        em.add_field(name = "!empty", value="[No Cooldown] Drains stomach to 0%.", inline=False)
        em.add_field(name = "!food (Amount)", value="[30m Cooldown or 25DD] Fills stomach to specified amount. Ex: !food 33", inline=False)   
        em.add_field(name = "!resetdiet", value="[No Cooldown] Resets diet.", inline=False)   
        am = discord.Embed(title= f"Legacy Commands:",color = discord.Color.green())
        am.add_field(name = "!swap", value="[15m Cooldown or 250DD] Swap your Legacy Dino with one of the Free Options! (Sends List in DM)", inline=False)
        am.add_field(name = "!donoswap", value="[15m Cooldown or 100DD] Swap your Legacy Dino with one of the Patreon Only Options! (Sends List in DM)", inline=False)   
        bm = discord.Embed(title= f"Economy Commands:",color = discord.Color.green())
        bm.add_field(name = "!balance", value="Checks Dino Doubloons Balance.", inline=False)
        bm.add_field(name = "!bal", value="Checks Dino Doubloons Balance.", inline=False)
        bm.add_field(name = "!beg", value="Begs for Dino Doubloons.", inline=False)    
        bm.add_field(name = "!work", value="Works for Dino Doubloons.", inline=False)
        bm.add_field(name = "!daily", value="Daily Bonus of Dino Doubloons.", inline=False)    
        bm.add_field(name = "!withdraw", value="Withdraw Dino Doubloons from Bank to Wallet.", inline=False)
        bm.add_field(name = "!deposit", value="Deposit Dino Doubloons from Wallet into Bank.", inline=False)  
        bm.add_field(name = "!depo", value="Deposit Dino Doubloons from Wallet into Bank.", inline=False)  
        bm.add_field(name = "!send", value="Send Dino Doubloons to another User. Ex: !send @Test 100", inline=False)
        bm.add_field(name = "!rob", value="Rob User Wallet of Dino Doubloons. Ex: !rob @Test", inline=False)    
        bm.add_field(name = "!slots", value="Play Slots and bet Double or Nothing.", inline=False)  
        await ctx.author.send(embed = em) 
        await ctx.author.send(embed = am)     
        await ctx.author.send(embed = bm) 
        
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)


@client.command()
@commands.dynamic_cooldown(custom_cooldown, type=commands.BucketType.user)    ## Cooldown Timer 1hr                            ## GROWS TO 100% WITHOUT MUTATIONS
async def grow(ctx):
    try:
        await helper.open_account(ctx.author)

        bal = await helper.update_bank(ctx.author)

        if bal[0]<50:
            await ctx.reply("You dont have enough Dino Doubloons!")
        else:
            print(q.qsize()) 
            q.put('Grow Command Executed')
            os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
            userId = (ctx.author.name).format(ctx)
            cost = 50
            await helper.update_bank(ctx.author, -1*cost)
            ctx.command.reset_cooldown(ctx)
            filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
            if (os.path.exists(filePath)):
                        await ctx.reply("Growing Dino...")
                        with open(filePath, 'r') as steamFile:
                            user = steamFile.read().rstrip()
                            pyautogui.click(1140, 444, duration=1)  
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.typewrite((user))  
                            pyautogui.click(253, 521, duration=5)  
                            pyautogui.typewrite('100')  
                            pyautogui.click(258, 503, duration=1)
                            for element in q.queue:
                                print(element)                    
            else:
                await ctx.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID") 
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)


@client.command()   
@commands.cooldown(1,900,commands.BucketType.user)    ## Cooldown Timer 15m                            ## KILLS CURRENT DINO
async def slay(ctx):
    try:
        await helper.open_account(ctx.author)

        bal = await helper.update_bank(ctx.author)

        if bal[0]<25:
            await ctx.reply("You dont have enough Dino Doubloons!")
        else:
            print(q.qsize()) 
            q.put('Slay Command Executed')
            os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
            userId = (ctx.author.name).format(ctx)
            cost = 25
            await helper.update_bank(ctx.author, -1*cost)
            ctx.command.reset_cooldown(ctx)
            filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
            if (os.path.exists(filePath)):
                        await ctx.reply("Killing Dino...")
                        with open(filePath, 'r') as steamFile:
                            user = steamFile.read().rstrip()
                            pyautogui.click(1140, 444, duration=1)
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.typewrite((user))
                            pyautogui.click(139, 548, duration=5)
                            for element in q.queue:
                                print(element)
            else:
                await ctx.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID") 
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)



@client.command()                                                    ## EMPTY STOMACH TO 0%
async def empty(ctx):
    try:
        print(q.qsize()) 
        q.put('Empty Command Executed')
        os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
        userId = (ctx.author.name).format(ctx)
        filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
        if (os.path.exists(filePath)):
                    await ctx.reply("Draining Food...")
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        pyautogui.click(1140, 444, duration=1)
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user))
                        pyautogui.click(323, 518, duration=5) 
                        pyautogui.typewrite('0')
                        pyautogui.click(331, 497, duration=1) 
                        for element in q.queue:
                            print(element)
                        
        else:
            await ctx.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)



@client.command()                                                                                       ## GIVES 100% FOOD
@commands.cooldown(1,900,commands.BucketType.user)    ## Cooldown Timer 15min
async def food(ctx, *, mess):
    try:
        await helper.open_account(ctx.author)

        bal = await helper.update_bank(ctx.author)

        if bal[0]<25:
            await ctx.reply("You dont have enough Dino Doubloons!")
        else:
            print(q.qsize()) 
            q.put('Food Command Executed')
            os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
            userId = (ctx.author.name).format(ctx)
            cost = 25
            await helper.update_bank(ctx.author, -1*cost)
            ctx.command.reset_cooldown(ctx)
            filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
            if (os.path.exists(filePath)):
                        await ctx.reply("Feeding Dino...")
                        with open(filePath, 'r') as steamFile:
                            user = steamFile.read().rstrip()
                            pyautogui.click(1140, 444, duration=1)
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.typewrite((user))
                            pyautogui.click(323, 518, duration=5) 
                            pyautogui.typewrite((mess))
                            pyautogui.click(331, 497, duration=1)
                            for element in q.queue:
                                print(element)
            else:
                await ctx.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID") 
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)


@client.command()                                                                                  ## RESETS DIET
async def resetdiet(ctx):
    try:
        print(q.qsize()) 
        q.put('Reset Diet Command Executed')
        os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
        userId = (ctx.author.name).format(ctx)
        filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
        if (os.path.exists(filePath)):
                    await ctx.reply("Resetting Diet...")
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        pyautogui.click(1140, 444, duration=1)
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user))
                        pyautogui.click(336, 562, duration=5)
                        pyautogui.typewrite('0')
                        pyautogui.click(265, 564, duration=0.7)
                        pyautogui.typewrite('0')
                        pyautogui.click(198, 562, duration=0.7)
                        pyautogui.typewrite('0')
                        pyautogui.click(201, 544, duration=0.7)
                        pyautogui.click(270, 546, duration=0.7)
                        pyautogui.click(333, 540, duration=0.7)
                        for element in q.queue:
                            print(element)
        else:
            await ctx.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)


@client.command()
@commands.dynamic_cooldown(custom_cooldown, type=commands.BucketType.user)    ## Cooldown Timer 30m                             ## GIVES PERFECT DIET
async def diet(ctx):
    try:
        await helper.open_account(ctx.author)

        bal = await helper.update_bank(ctx.author)

        if bal[0]<100:
            await ctx.reply("You dont have enough Dino Doubloons!")
        else:
            print(q.qsize()) 
            q.put('Diet Command Executed')
            os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
            userId = (ctx.author.name).format(ctx)
            cost = 100
            await helper.update_bank(ctx.author, -1*cost)
            ctx.command.reset_cooldown(ctx)
            filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
            if (os.path.exists(filePath)):
                        await ctx.reply("Giving Perfect Diet...")
                        with open(filePath, 'r') as steamFile:
                            user = steamFile.read().rstrip()
                            pyautogui.click(1140, 444, duration=1)
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.typewrite((user))
                            pyautogui.click(323, 518, duration=5) 
                            pyautogui.typewrite('100')
                            pyautogui.click(331, 497, duration=0.5) 
                            pyautogui.click(593, 551, duration=0.5)
                            pyautogui.click(581, 581, duration=0.5)
                            pyautogui.click(484, 556, duration=0.5)
                            pyautogui.click(485, 599, duration=0.5)
                            pyautogui.click(394, 551, duration=0.5)
                        ## pyautogui.click(389, 612, duration=0.5) ## Zombie Button
                            pyautogui.click(336, 562, duration=0.5)
                            pyautogui.typewrite('400')
                            pyautogui.click(265, 564, duration=0.5)
                            pyautogui.typewrite('400')
                            pyautogui.click(198, 562, duration=0.5)
                            pyautogui.typewrite('400')
                            pyautogui.click(201, 544, duration=0.5)
                            pyautogui.click(270, 546, duration=0.5)
                            pyautogui.click(333, 540, duration=0.5)
                            for element in q.queue:
                                print(element) 
            else:
                await ctx.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)


@client.command()
@commands.dynamic_cooldown(custom_cooldown, type=commands.BucketType.user)                                                     ## SHRINKS CURENT DINO TO 1% GROWTH
async def shrink(ctx):
    try:
        await helper.open_account(ctx.author)

        bal = await helper.update_bank(ctx.author)

        if bal[0]<100:
            await ctx.reply("You dont have enough Dino Doubloons!")
        else:
            print(q.qsize()) 
            q.put('Shrink Command Executed')
            os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")
            userId = (ctx.author.name).format(ctx)
            cost = 100
            await helper.update_bank(ctx.author, -1*cost)
            ctx.command.reset_cooldown(ctx)
            filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
            if (os.path.exists(filePath)):
                        await ctx.reply("SO SMOL :pinching_hand: ")
                        with open(filePath, 'r') as steamFile:
                            user = steamFile.read().rstrip()
                            pyautogui.click(1140, 444, duration=1)
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.typewrite((user))
                            pyautogui.click(253, 521, duration=5) 
                            pyautogui.typewrite('1')
                            pyautogui.click(258, 503, duration=0.5)
                            for element in q.queue:
                                print(element) 
            else:
                await ctx.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)



@client.command()
@commands.dynamic_cooldown(custom_cooldown, type=commands.BucketType.user)    ## Cooldown Timer
async def slowgrow(ctx):
    try:
        await helper.open_account(ctx.author)

        bal = await helper.update_bank(ctx.author)

        if bal[0]<100:
            await ctx.reply("You dont have enough Dino Doubloons!")

        else:
            print(q.qsize()) 
            q.put('Slow Grow Command Executed')   
            os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                                 ## GROWS SLOWLY TO 100% WITH MUTATIONS
            userId = (ctx.author.name).format(ctx)
            cost = 100
            await helper.update_bank(ctx.author, -1*cost)
            ctx.command.reset_cooldown(ctx)
            filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
            if (os.path.exists(filePath)):
                        await ctx.reply("Growing Dino With Mutations...")
                        with open(filePath, 'r') as steamFile:
                            user = steamFile.read().rstrip()
                            pyautogui.click(1140, 444, duration=1)  ##Searchbar Click
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')
                            pyautogui.typewrite((user))  ##Searchbar Txt ### GROWING THIS USER
                            pyautogui.click(253, 521, duration=5)  ##First Grow Click
                            pyautogui.hotkey('ctrlleft', 'a', duration=1)
                            pyautogui.press('backspace')       
                            pyautogui.typewrite('68')  ##Grow Mutation Stage 2
                            pyautogui.click(258, 503, duration=0.5)
                            pyautogui.click(253, 521, duration=20)
                            pyautogui.hotkey('ctrlleft', 'a', duration=3)
                            pyautogui.press('backspace')    
                            pyautogui.click(253, 521, duration=1)
                            pyautogui.typewrite('100') ##Grow Mutation Stage 3
                            pyautogui.click(258, 503, duration=0.5)
                            pyautogui.click(593, 551, duration=0.5)
                            pyautogui.click(581, 581, duration=0.5)
                            pyautogui.click(484, 556, duration=0.5)
                            pyautogui.click(485, 599, duration=0.5)
                            pyautogui.click(394, 551, duration=0.5)
                            ## pyautogui.click(389, 612, duration=0.5)
                            pyautogui.click(336, 562, duration=0.5)
                            pyautogui.typewrite('400')
                            pyautogui.click(265, 564, duration=0.5)
                            pyautogui.typewrite('400')
                            pyautogui.click(198, 562, duration=0.5)
                            pyautogui.typewrite('400')
                            pyautogui.click(201, 544, duration=0.5)
                            pyautogui.click(270, 546, duration=0.5)
                            pyautogui.click(333, 540, duration=0.5)
                            for element in q.queue:
                                print(element)
            else:
                await ctx.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)



##############################################TELEPORT SETUP###############################################################################


class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="SOUTH PLAINS - 250"),
            discord.SelectOption(label="SOUTH PLAINS RIVER - 250"),
            discord.SelectOption(label="WATER ACCESS - 250"),
            discord.SelectOption(label="JUNGLE PLAINS - 250"),
            discord.SelectOption(label="JUNGLE PLAINS POND - 250"),
            discord.SelectOption(label="SOUTH VOLCANO FIELD - 250"),
            discord.SelectOption(label="SOUTH VOLCANO POND - 250"),
            discord.SelectOption(label="HIGHLANDS J SECTOR - 250"),
            discord.SelectOption(label="HIGHLANDS LAKE - 250"),
            discord.SelectOption(label="JUNGLE POND - 250"),
            discord.SelectOption(label="NORTHWEST RIDGE - 250"),
            discord.SelectOption(label="NORTHWEST RIDGE LAKE - 250"),
            discord.SelectOption(label="EAST PLAINS - 250"),
            discord.SelectOption(label="WEST ACCESS - 250"),
            discord.SelectOption(label="WEST ACCESS LAKE - 250"),
            discord.SelectOption(label="WEST RAIL ACCESS - 250"),
            discord.SelectOption(label="WEST RAIL ACCESS LAKE - 250"),
            discord.SelectOption(label="NORTHERN JUNGLE - 250"),
            discord.SelectOption(label="NORTH LAKE - 250"),
            discord.SelectOption(label="SOUTHERN BEACH - 250"),
            discord.SelectOption(label="WATERFALL - 250"),
            discord.SelectOption(label="WATERFALL POND - 250"),
            discord.SelectOption(label="SWAMP EAST - 250"),
            discord.SelectOption(label="SWAMP CENTER - 250"),
            discord.SelectOption(label="SOUTHERN ISLAND - 250")
            ]
        super().__init__(placeholder="Where do you want to Teleport?",max_values=1,min_values=1,options=options)
        
    async def callback(self, interaction: discord.Interaction):
        try:
            if self.values[0] == "SOUTH PLAINS - 250":
                await interaction.response.send_message(content="Teleporting to SOUTH PLAINS please wait...", ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command') 
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                         
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,4)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.3)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.3)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.7)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("166338") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-165939") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("205535") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-175878") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("198930") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-149254") ##INPUT LONG COORDS #
                        elif random_num == 4:
                            pyautogui.typewrite("203399") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-146003") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.5)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")
        
            elif self.values[0] == "SOUTH PLAINS RIVER - 250":
                await interaction.response.send_message("Teleporting to SOUTH PLAINS RIVER please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')  
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                            
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("162958") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-204551") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("157208") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-204262") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("180719") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-190586") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.5)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "WATER ACCESS - 250":
                await interaction.response.send_message("Teleporting to WATER ACCESS please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')  
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                              
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,4)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-289528") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("89396") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-253475") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("46977") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-233631") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("59194") ##INPUT LONG COORDS #
                        elif random_num == 4:
                            pyautogui.typewrite("-240061") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("101973") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.5)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "JUNGLE PLAINS - 250":
                await interaction.response.send_message("Teleporting to JUNGLE PLAINS please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')     
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                            
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,4)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-152983") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("239362") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-144601") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("274053") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-190615") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("261436") ##INPUT LONG COORDS #
                        elif random_num == 4:
                            pyautogui.typewrite("-186163") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("269924") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.5)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "JUNGLE PLAINS POND - 250":
                await interaction.response.send_message("Teleporting to JUNGLE PLAINS POND please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')   
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                               
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-172842") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("245526") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-163983") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("244066") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-173279") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("253341") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.5)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "SOUTH VOLCANO FIELD - 250":
                await interaction.response.send_message("Teleporting to SOUTH VOLCANO FIELD please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')     
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                          
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("305008") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-136352") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("298293") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-174250") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("317027") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-127968") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.5)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "SOUTH VOLCANO POND - 250":
                await interaction.response.send_message("Teleporting to SOUTH VOLCANO POND please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')   
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                            
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("303582") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-142164") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("301924") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-148533") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("300278") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.5) ##Long Box Click
                            pyautogui.typewrite("-151201") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.5)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "HIGHLANDS J SECTOR - 250":
                await interaction.response.send_message("Teleporting to HIGHLANDS J SECTOR please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')  
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                             
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)                    ####################################################)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-30657") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-102359") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-10038") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-127899") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-57599") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-126554") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "HIGHLANDS LAKE - 250":
                await interaction.response.send_message("Teleporting to HIGHLANDS LAKE please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')    
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                          
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,5)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.3)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-153227") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-10544") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-151977") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-20930") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-131744") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-41253") ##INPUT LONG COORDS #
                        elif random_num == 4:
                            pyautogui.typewrite("-123970") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-9550") ##INPUT LONG COORDS #
                        elif random_num == 5:
                            pyautogui.typewrite("-117553") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("5611") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "JUNGLE POND - 250":
                await interaction.response.send_message("Teleporting to JUNGLE POND please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')     
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                       
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        pyautogui.typewrite("-7491") ##INPUT LAT COORDS 
                        pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                        pyautogui.typewrite("80240") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "NORTHWEST RIDGE - 250":
                await interaction.response.send_message("Teleporting to NORTHWEST RIDGE please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')      
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                        
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.3)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-292546") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-150621") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-329824") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-125120") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-318244") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-86193") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "NORTHWEST RIDGE LAKE - 250":
                await interaction.response.send_message("Teleporting to NORTHWEST RIDGE LAKE please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')       
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                        
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-345006") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-60141") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-339626") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-68607") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-345827") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-60894") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "EAST PLAINS - 250":
                await interaction.response.send_message("Teleporting to EAST PLAINS please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')      
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                          
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.3)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-152507") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("497615") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-146250") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("487789") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-139061") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("497918") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "WEST ACCESS - 250":
                await interaction.response.send_message("Teleporting to WEST ACCESS please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')   
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                             
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-118699") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-343833") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-98257") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-351517") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-107085") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-325508") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "WEST ACCESS LAKE - 250":
                await interaction.response.send_message("Teleporting to WEST ACCESS LAKE please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')     
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                            
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-110439") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-348321") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-106171") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-342794") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-99369") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-338230") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "WEST RAIL ACCESS - 250":
                await interaction.response.send_message("Teleporting to WEST RAIL ACCESS please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')       
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                          
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("3255") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-303742") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("32789") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-280053") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("3971") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-260391") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "WEST RAIL ACCESS LAKE - 250":
                await interaction.response.send_message("Teleporting to WEST RAIL ACCESS LAKE please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')    
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                             
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("16057") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-282961") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("12086") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-276440") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("12826") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("-283329") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "NORTHERN JUNGLE - 250":
                await interaction.response.send_message("Teleporting to NORTHERN JUNGLE please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')    
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                           
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-348103") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("113675") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-332389") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("109482") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-314880") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("110733") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "NORTH LAKE - 250":
                await interaction.response.send_message("Teleporting to NORTH LAKE please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')    
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                             
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,4)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-354748") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("327800") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-353954") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("334304") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-382783") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("304868") ##INPUT LONG COORDS #
                        elif random_num == 4:
                            pyautogui.typewrite("-390628") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("317607") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "SOUTHERN BEACH - 250":
                await interaction.response.send_message("Teleporting to SOUTHERN BEACH please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')    
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                            
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("370847") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("160748") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("372859") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("133739") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("366968") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("108499") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.5)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "SWAMP EAST - 250":
                await interaction.response.send_message("Teleporting to SWAMP EAST please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')    
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                              
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("302310") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("142290") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("264603") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("146023") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("346078") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("128808") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "SWAMP CENTER - 250":
                await interaction.response.send_message("Teleporting to SWAMP CENTER please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')    
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                              
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("258550") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("159987") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("291701") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("96934") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("298485") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("54489") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "WATERFALL - 250":
                await interaction.response.send_message("Teleporting to WATERFALL please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')     
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                            
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-199898") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("336091") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-176576") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("318916") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-160186") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("319251") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "WATERFALL POND - 250":
                await interaction.response.send_message("Teleporting to WATERFALL POND please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')      
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                            
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,3)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("-170168") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("328190") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("-175489") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("333850") ##INPUT LONG COORDS #
                        elif random_num == 3:
                            pyautogui.typewrite("-171778") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("331751") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")

            elif self.values[0] == "SOUTHERN ISLAND - 250":
                await interaction.response.send_message("Teleporting to SOUTHERN ISLAND please wait...",ephemeral=True)
                print(q.qsize()) 
                q.put('Teleport Command')     
                os.chdir("C:\\Users\\Olden\\Desktop\\PythonBot")                                                                             
                userId = (interaction.user)
                cost = 250
                await helper.update_bank(interaction.user, -1*cost)
                filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
                if (os.path.exists(filePath)):
                    with open(filePath, 'r') as steamFile:
                        user = steamFile.read().rstrip()
                        random_num = random.randint(1,2)
                        pyautogui.click(1481, 213, duration=1)
                        pyautogui.press('insert') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Out of Spectator
                        await asyncio.sleep(0.5)
                        pyautogui.press('insert') ##Go Into Menu
                        pyautogui.click(1481, 213, duration=0.5)
                        pyautogui.click(172, 888, duration=1.5)  ##Environment Click 
                        pyautogui.click(1710, 494, duration=0.5) ##Lat Box Click
                        if random_num == 1:
                            pyautogui.typewrite("206598") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("473646") ##INPUT LONG COORDS #
                        elif random_num == 2:
                            pyautogui.typewrite("170603") ##INPUT LAT COORDS 
                            pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
                            pyautogui.typewrite("484542") ##INPUT LONG COORDS #
                        pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
                        pyautogui.press('esc') ##Go Out Of Menu
                        await asyncio.sleep(0.7)
                        pyautogui.press('del') ##Go Into Spectator
                        await asyncio.sleep(0.7)
                        pyautogui.press('insert') ##Go Into Menu
                        await asyncio.sleep(0.7)
                        pyautogui.click(1140, 444, duration=2)  ##Searchbar Click
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.hotkey('ctrlleft', 'a', duration=1)
                        pyautogui.press('backspace')
                        pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
                        pyautogui.click(52, 504, duration=6) ##BRING BUTTON
                        for element in q.queue:
                            print(element)
                else:
                    await self.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")
        except Exception as e:
            logger.exception("An error occurred: %s", e)
            print(e)



class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 60):
        super().__init__(timeout=timeout)
        self.add_item(Select())

@client.command()
@commands.cooldown(1,900,commands.BucketType.user)    ## Cooldown Timer 1hr 
async def tp(ctx):
    try:
        await helper.open_account(ctx.author)

        bal = await helper.update_bank(ctx.author)

        if bal[0]<250:
            await ctx.reply("You dont have enough Dino Doubloons!")
        else:
            await ctx.reply("Sending Locations List...")
            await ctx.author.send("Teleport Menu:",view=SelectView())
            ctx.command.reset_cooldown(ctx)
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)

@client.command()
@commands.has_any_role("Boatswains", "Sailing Master", "Quartermasters", "First Mate", "The Captain", "Gunners", "TEST")
async def admintp(ctx):
    try:
        await ctx.reply("Sending Locations List...")
        await ctx.author.send("Teleport Menu:",view=SelectView())
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)

#############################################################################################################################



#@client.command()
#@commands.has_any_role("Boatswains", "Sailing Master", "Quartermasters", "First Mate", "The Captain", "Gunners", "TEST")
#async def admintp(ctx):
#    print(q.qsize()) 
#    q.put('Teleport Command')                                                                                    ## GROWS SLOWLY TO 100% WITH MUTATIONS
#    userId = (ctx.author.name).format(ctx)
#    filePath = os.path.join(os.getcwd(), "steamids", str(userId) + ".desc.txt")
#    if (os.path.exists(filePath)):
#                await ctx.reply("Teleporting Please Wait...")
#                with open(filePath, 'r') as steamFile:
#                    user = steamFile.read().rstrip()
#                    pyautogui.press('insert') ##Go Out Of Menu
#                    await asyncio.sleep(0.7)
#                    pyautogui.press('del') ##Go Out of Spectator
#                    await asyncio.sleep(0.7)
#                    pyautogui.press('insert') ##Go Into Menu
#                    pyautogui.click(172, 888, duration=0.7)  ##Environment Click 
#                    pyautogui.click(1710, 494, duration=0.7) ##Lat Box Click
#                    pyautogui.typewrite("-253475") ##INPUT LAT COORDS 
#                    pyautogui.click(1689, 531, duration=0.7) ##Long Box Click
#                    pyautogui.typewrite("46977") ##INPUT LONG COORDS #
#                    pyautogui.click(1679, 628, duration=0.5) ##TP Button CLick
#                    pyautogui.press('esc') ##Go Out Of Menu
#                    await asyncio.sleep(0.7)
#                    pyautogui.press('del') ##Go Into Spectator
#                    await asyncio.sleep(0.7)
#                    pyautogui.press('insert') ##Go Into Menu
#                    await asyncio.sleep(0.7)
#                    pyautogui.click(1140, 444, duration=0.5)  ##Searchbar Click
#                    pyautogui.hotkey('ctrlleft', 'a', duration=0.5)
#                    pyautogui.press('backspace')
#                    pyautogui.typewrite((user)) ##Searchbar Txt to Paste User
#                    pyautogui.click(52, 504, duration=0.5) ##BRING BUTTON
#                    for element in q.queue:
#                        print(element)
#    else:
#        await ctx.reply("You do not have a Steam 64 ID linked. Use !link ############ to link your 17 digit Steam 64 ID")





### BASIC BOT COMMANDS####
###########################################################################################################################################



@client.command()  
@commands.has_any_role("Boatswains", "Sailing Master", "Quartermasters", "First Mate", "The Captain", "Gunners", "TEST")          ## SENDS ANNOUNCEMENT TO SERVER
async def sendann(ctx, *, mess):
    try:
        print(q.qsize()) 
        q.put_nowait('Announcement Sent')
        await ctx.reply("Sending Announcement")
        pyautogui.click(155, 267, duration=0.4)
        pyautogui.hotkey('ctrlleft', 'a', duration=0.4)
        pyautogui.press('backspace')
        pyautogui.typewrite((mess))
        pyautogui.click(1737, 380, duration=0.2) 
        for element in q.queue:
            print(element)     
    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)                  


@client.event
async def on_command_error(ctx, error):
    try:
        if isinstance(error, commands.CommandOnCooldown):    ## Checks for Cooldown
                remaining_time = str(datetime.timedelta(seconds=int(error.retry_after)))

                embed = discord.Embed(title=":clock1: The Verdant Isle", description=f'{ctx.author.mention}, Cooldown Remaining: ' + str(remaining_time), color=0xE74C3C)
                await ctx.reply(embed=embed)

    except Exception as e:
        logger.exception("An error occurred: %s", e)
        print(e)





client.run(BOT_TOKEN)  
# bot.run(BOT_TOKEN) 
 

 
