import discord
import matplotlib.pyplot as plt
import numpy as np
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.utils import get
from itertools import cycle
import time, os, random, sys, io
# import aiohttp



# Bagelbot mark1

### Jokes ###

Names = open("Reactions.txt", "a+")

jokelist = ["Wanna hear a joke?", "Knock Knock. Who's there?",
            "What do you call a bottomless pit of despair?", "What does the sign on an out-of-business nightclub say?",
            "Why does Santa Claus have such a big sack?", "What’s long and hard and full of seamen?"]

answerlist = ["You", "Not my mom, she left 15 years ago", "BIO 202", "Beat it, we're closed",
              "He only comes once a year", "A submarine"]

bJokes = ["What kind of bagel can fly?", "Why doesn’t a seagull fly over the bay?",
          "I love these balls, so creamy and soft", "How do you hold a bagel back?",
          "What does a bagel do when it is locked out of its house?", "The Zoo has a new bagel exhibit",
          "Why'd the bagel go to the club?"]

bAnswers = ["A plain bagel", "Because then it’d be a bagel.", "Best Bagel Bites of my life", "You put a lox on it",
            "Call a loxsmith", "Apparently they were bread in captivity", "To get toasted"]

allowed = ["Download_Seqs", "Odds", "download_General", "run", "Download_Swiss", "Download_Cif/PDB"]

master = str(os.getcwd())


### End jokes

### Commands ###

Clist = ["joke", "bageljoke", "bakery", "clear", "Tateru", "cramer", "Cramer_help", "Wailord", ]

### End Commands

status = cycle(["Status 1", "Status 2"])

client = commands.Bot(command_prefix = "$")
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$"))
    print("We have logged in as {0.user}".format(client))

# CHECK THIS LATER, PROBLEM WITH DOWNLOAD

@client.event
async def on_error(ctx, error, *args, **kwargs):
    if error == "on_command_error":
        await args[0].send("Somethng Went wrong")
      
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        pass

    print(str(error))
    err = False
    
    for i in range(len(allowed)):
        if allowed[i] in str(error):
            err = True
            
        
    if err != True:
        await ctx.send(str(error) + "!")
        await ctx.send("You should use $help' if you don't know the command")


@client.command()
async def intro(ctx):
    await ctx.send("""Hello @everyone you lovely loafes, my name's BagelBot. My baker would like me to tell you all how I work, what I can do and the future of our iGEM team!
Because my baker is a total lose- lovely person, he spent all of this weekend giving me a ton of Biology functionality to make future work easier. I'm working towards becoming
a tool for future teams to get started with and learn simple DNA manipulation and Phylogenetics, with advanced math and plotting coming at a later date (and hopefully get us some rep as a modeling tool).
If you'd like a full list of my commands, try '$help' (without the '' of course). Looking forward to meeting you!""")


@client.command(aliases = ["Repos", "Repositories"], help = ("Posts links to the 2 repos for the team and BB"))
async def Repo(ctx):
    embed = discord.Embed(title = "Repositories", description = "Here's the repos for myself and the team!:")
    embed.add_field(name = "Team Repository", value = "https://github.com/iGEM-SBU/Wiki-2020", inline = True)
    embed.set_thumbnail
    embed.add_field(name = "My Repositroy", value = "https://github.com/Dreamer3000/BagelBot", inline = True)
    await ctx.send(embed = embed)    
        
        
@client.command(aliases = ["bageljoke"], help = "Random assortment of family-friendly bagel jokes")
async def bjokes(ctx):
            
    x = random.randint(0,len(bJokes) - 1)
    await ctx.send(bJokes[x])
    time.sleep(6)
    await ctx.send(bAnswers[x])

@client.command(aliases = ["joke"], help = "Random assortment of adult jokes, enjoy")
async def jokes(ctx):
            
    x = random.randint(0,len(jokelist) - 1)
    await ctx.send(jokelist[x])
    time.sleep(6)
    await ctx.send(answerlist[x])
    
@client.command(aliases = ["BakeryOpen?"], help = "Will find the latency of the user")
async def bakery(ctx):
    await ctx.send("Like it ever is.")
    await ctx.send("Latency is " + str(round(client.latency * 1000)) + " ms")         


@client.command(aliases = ["clear"], help = "Clears 5 lines of text from the discord chat, including this command")
async def clearz(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)
    
@client.command(aliases = ["megaclear"], help = "Clears 20 lines of text from the discord chat, including this command")
async def MegaClear(ctx, amount = 20):
    await ctx.channel.purge(limit = amount)
    

@client.command(aliases = ["MooMoo", "Dcurt"])
async def vanished(ctx):
    await ctx.send("Was he ever here to begin with?")

@client.command()
async def Help(ctx):
    await ctx.send("Here's a fresh batch of my commands: ")
    time.sleep(1)
    await ctx.send(Clist)

@client.command()
async def quit(ctx):
    await ctx.send("Shutting down the bot")
    return await client.logout() # this just shuts down the bot.

@client.command(aliases = ["tateru"], help = "Will a Luma appear?")
async def Tateru(ctx):
    os.chdir(master)
    x = random.randint(1,8000)
    
    ans = 4288
    if x == ans:
        with open("LumaTata.png", "rb") as fh:
            f = discord.File(fh, filename = "LumaTata.png")
        #if not ctx.author.bot:
            
            await ctx.send(file = f)
            await ctx.send("@everyone a LumaTata has appeared!")
    else:
        
        with open("Tata.png", "rb") as fh:
            f = discord.File(fh, filename = "Tata.png")
            
        #if not ctx.author.bot:
            await ctx.send(file = f)

@client.command(aliases = ["wail", "wailord"], help = "He sure seems excited...")
async def Wailord(ctx):
    with open("wail.jpg","rb") as tacos:
        t = discord.File(tacos, filename = "wail.jpg")
    await ctx.send(file = t)

@client.command(aliases=["Vin"], help = "When your only friend is two pieces of bread")
async def vin(ctx):
    await ctx.send("Hi Vin, alone again huh?")
        
@client.command(help = "Find the chance of getting a Luma Tateru!")
async def Tatas(ctx, *, arg):
    await ctx.send("Your chance of finding a Luma Tateru was " + str(100 - ((7999/8000) ** float(arg)) * 100) + "%")

@client.event
async def on_message(message):
    
    if message.content.startswith('$Odds'):
        channel = message.channel
      
        
        if message.author.bot:
            return
        else:
            await channel.send("What's the challenge?")
        
        
        
            def check(m):
                return m.channel == channel
        
            mesg = await client.wait_for("message", check=check, timeout=60)
        
            await channel.send("What are the odds you'll " + str(mesg.content) + "?")
        
            msg = await client.wait_for("message", check=check, timeout = 60)
        
            x = random.randint(1, int(msg.content))
        
            await channel.send("Pick your number")
        
            msg2 =  await client.wait_for("message", check=check, timeout = 60)
       
            await channel.send("You chose: " + str(msg2.content))
            await channel.send("I chose: " + str(x))
        
            if int(msg2.content) == x:
                await channel.send("You have no other choice but to " + mesg.content)
            else:
                await channel.send("I guess you lucked out this time")
    
    await client.process_commands(message)
                
         
@client.listen()          
async def on_message(message):
    
    if message.content.endswith("$Download_Seqs"):
        os.chdir(master)
        channel = message.channel
        author = message.author
        
        def check(m):
            return m.channel == channel
            
        await channel.send("Put in an attachment")
           
        mesg = await client.wait_for("message", check=check, timeout=60)
        
        await channel.send("Processed Attachment")
        
        if os.path.exists(str(author)):
            os.chdir(str(author))

        else:
            os.mkdir(str(author))
            os.chdir(str(author))
        
        await mesg.attachments[0].save("Seqs.phy")
        
        await channel.send("Saved attachment")
       
        os.chdir(master)
       
        
        
@client.listen()          
async def on_message(message):
    
    if message.content.startswith("$download_general"):
        os.chdir(master)
        channel = message.channel
        author = message.author
            
        def check(m):
            return m.channel == channel
        
        await channel.send("What file format do you want it saved in? Include the .")
        
        t = await client.wait_for("message", check=check, timeout=60)
        
            
        await channel.send("Put in an attachment")
           
        mesg = await client.wait_for("message", check=check, timeout=60)
        
        await channel.send("Processed Attachment")
        
        if os.path.exists(str(author)):
            os.chdir(str(author))

        else:
            os.mkdir(str(author))
            os.chdir(str(author))
        
            
        await mesg.attachments[0].save("Pic" + t.content)
            
        await channel.send("Saved attachment")  
        os.chdir(master)
@client.listen()
async def on_message(message):

    if message.content.startswith("$Download_Cif/PDB"):
        os.chdir(master)
        channel = message.channel
        author = message.author
        def check(m):
            return m.channel == channel
            
        await channel.send("Put in an attachment")
           
        mesg = await client.wait_for("message", check=check, timeout=60)
       
        await channel.send("Processed Attachment")
        
        if os.path.exists(str(author)):
            os.chdir(str(author))

        else:
            os.mkdir(str(author))
            os.chdir(str(author))
        
        await mesg.attachments[0].save(mesg.attachments[0].filename)
            
        await channel.send("Saved attachment")
       
        os.chdir(master)
       
####### Math Functions go here: #######

@client.command(help = "Find the mole ratio of two compounds. Takes in 4 arguments: grams of molecule 1, molar mass of molecule 1, grams of molecule 2 and molar mass of molecule 2")
async def mole_ratio(ctx, arg1, arg2, arg3, arg4):
    mole1 = float(arg1)/float(arg2)
    mole2 = float(arg3)/float(arg4)
    total = mole1 + mole2
    fraction1 = mole1/total
    fraction2 = mole2/total
    await ctx.send("The first molar fraction is " + str(fraction1) + " and the second molar fraction is " + str(fraction2) )

@client.command(aliases = ["SN"], help = "Will one day tell you the VESPR Geometry and Steric Number of a molecule, first input is the number of bonds, second is the number of lone pairs")
async def StericNumber(ctx, arg1, arg2):
    # arg1 is number of bonds, arg2 is number of lone pairs
    SN = int(arg1) + int(arg2)
    SN2 = "Linear"
    SN3 = ["Trigonal Planar", "Bent"]
    SN4 = ["Tetrahedral", "Trigonal Pyramidal", "Bent"]
    SN5 = ["Trigonal Bipyramidal", "See Saw", "T-shaped", "Linear"]
    SN6 = ["Octahedral", "Square Pyrimidal", "Square Planar"]
    x = "Check your input, the geometry doesn't seem right"
    arg2 = int(arg2)
    if SN == 2:
        await ctx.send("Your Molecule is Lienar")
    elif SN == 3:
        if arg2 == 1:
            await ctx.send("Your Molecule is: " + SN3[1])
        if arg2 == 0:
            await ctx.send("Your Molecule is: " + SN3[0])
        else:
            await ctx.send(x)
    elif SN == 4:
        if arg2 == 2:
            await ctx.send("Your Molecule is: " + SN4[2])
        if arg2 == 1:
            await ctx.send("Your Molecule is: " + SN4[1])
        if arg2 == 0:
            await ctx.send("Your Molecule is: " + N4[0])
        else:
            await ctx.send(x)
    elif SN == 5:
        if arg2 == 3:
            await ctx.send("Your Molecule is: " + SN5[3])
        if arg2 == 2:
            await ctx.send("Your Molecule is: " + SN5[2])
        if arg2 == 1:
            await ctx.send("Your Molecule is: " + SN5[1])
        if arg2 == 0:
            await ctx.send("Your Molecule is: " + SN5[0])
        else:
            await ctx.send(x)
    elif SN == 6:
        if arg2 == 2:
            await ctx.send("Your Molecule is: " + SN6[2])
        if arg2 == 1:
            await ctx.send("Your Molecule is: " + SN6[1])
        if arg2 == 0:
            await ctx.send("Your Molecule is: " + SN6[0])
        else:
            await ctx.send(x)


@client.command(aliases = ["IHD"], help = "Calculates the index of Hydrogen Defeciency. Write the number of Carbons, Nitrogens, Hydrogens and Halogens in that order. Syntax: $IHD 6 4 0 0")
async def ihd(ctx, *args):
    
    test = []
    for i in range(0, len(args)):
        test.append(args[i])
    
    if len(test) < 4:
        for i in range(len(test),4):
            test.append(0)
    
    answer = .5 * (2 * int(str(test[0])) - int(str(test[1])) + 2 + int(str(test[2]))  - int(str(test[3])))
    await ctx.send("The IHD of your molecule is: " + str(int(answer)))
    
    await ctx.send("Your molecule will have a minimum of " + str(answer) + " rings and double bonds combined, but MAY have more in some cases. Normally, the minimum will be correct.")
    await ctx.send("Warning: If your molecule has triple bonds, it can have up to " + str(int(answer/2)) +  " triple bonds (2 IHD per triple bond)")
    
@client.command()
async def test1(ctx):
    await ctx.send(str(ctx.author))

@client.command(aliases = ["genshin"])
async def Genshin(ctx, arg1):
   
    answer = .984 ** int(arg1)
    
    await ctx.send("The chance of you finding a 5 star within " + str(arg1) + " pulls is: " + str((1 - answer) * 100) + "%" )
    
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}') # splice here will remove the .py from filename


# Not my real token, sorry if you want to steal my bot.
client.run("UrD098c.MwMzU/xMzBgDDcyMjU2.IhwOKw.NPDB1JKAWswFEbYAg9punFTN_dM")
