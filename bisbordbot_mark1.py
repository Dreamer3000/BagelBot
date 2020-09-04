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
    if "Download" in str(error) or "Odds" in str(error) or "download_General" in str(error):
        pass
    else:
        await ctx.send(str(error) + "!")
        await ctx.send("You should use $help' if you don't know the command")


@client.command()
async def intro(ctx):
    await ctx.send("""Hello @everyone you lovely loafes, my name's BagelBot. My baker would like me to tell you all how I work, what I can do and the future of our iGEM team!
Because my baker is a total lose- lovely person, he spent all of this weekend giving me a ton of Biology functionality to make future work easier. I'm working towards becoming
a tool for future teams to get started with and learn simple DNA manipulation and Phylogenetics, with advanced math and plotting coming at a later date (and hopefully get us some rep as a modeling tool).
If you'd like a full list of my commands, try '$help' (without the '' of course). Looking forward to meeting you!""")



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
    
    if message.content.startswith("$Download"):
        
        channel = message.channel
        
            
        def check(m):
            return m.channel == channel
            
        await channel.send("Put in an attachment")
           
        mesg = await client.wait_for("message", check=check, timeout=60)
        
        await channel.send("Processed Attachment")
            
        await mesg.attachments[0].save("Seqs.phy")
            
        await channel.send("Saved attachment")
                #print(y)
        
@client.listen()          
async def on_message(message):
    
    if message.content.startswith("$download_general"):
        
        channel = message.channel
        
            
        def check(m):
            return m.channel == channel
        
        await channel.send("What file format do you want it saved in? Include the .")
        
        t = await client.wait_for("message", check=check, timeout=60)
        
            
        await channel.send("Put in an attachment")
           
        mesg = await client.wait_for("message", check=check, timeout=60)
        
        await channel.send("Processed Attachment")
            
        await mesg.attachments[0].save("Pic" + t.content)
            
        await channel.send("Saved attachment")  
    

####### Math Functions go here: #######

@client.command(help = "Find the mole ratio of two compounds. Takes in 4 arguments: grams of molecule 1, molar mass of molecule 1, grams of molecule 2 andmolar mass of molecule 2")
async def mole_ratio(ctx, arg1, arg2, arg3, arg4):
    mole1 = float(arg1)/float(arg2)
    mole2 = float(arg3)/float(arg4)
    total = mole1 + mole2
    fraction1 = mole1/total
    fraction2 = mole2/total
    await ctx.send("The first molar fraction is " + str(fraction1) + " and the second molar fraction is " + str(fraction2) )

@client.command(help = "Will one day tell you the VESPR Geometry and Steric Number of a molecule, nothing here as of yet")
async def StericNumber(ctx, arg1, arg2):
    # arg1 is number of atoms, arg2 is number of electrons in molecule
    #if
    await ctx.send("Nothing here yet, sorry")
    pass

@client.command(help = "Will tell you the average of however many arguments you pass it, for example: $mean 1 87 52")
async def mean(ctx, *args):
    length = len(args)
    counter = 0
    for i in args:
        counter += int(i)
    await ctx.send("The mean of your numbers is " + str(counter /len(args)))

@client.command(aliases = ["Pythag", "pythagoras", "pythag", "pg"], help = "Takes in 3 arguments, 2 numbers and what side you're looking for (a,b or c). For example: $Pythag 10 14 a")
async def Pythagoras(ctx, arg1, arg2, arg3):
    
    if arg3.lower() == "c":
        answer = (int(arg1) ** 2 + int(arg2) ** 2) ** (1/2)
        await ctx.send("Your answer is " + str(answer))
        
    else:
        if int(arg1) > int(arg2):
            answer = (int(arg1) ** 2 - int(arg2) ** 2) ** (1/2)
            await ctx.send("Your answer is " + str(answer))
            
        elif int(arg2) > int(arg1):
            answer = (int(arg2) ** 2 - int(arg1) ** 2) ** (1/2)
            await ctx.send("Your answer is " + str(answer))

@client.command(aliases = ["plot", "pl", "bagelplot"], help = "Plot's a linear graph of 2 data sets. Data set 1 is the first half of arguments, data set 2 is the second half of arguments. For example: $plot 1 2 3 4 2 4 6 8")
async def Plot(ctx, *args):
    
    test = []
    xlist = []
    ylist = []
    
    for i in args:
        test.append(i)
    
    plt.clf()
    
    for i in range(0,int(len(test)/2)):
        xlist.append(test[int(i)])
        
    for i in range(int(len(test)/2), int(len(test))):
        ylist.append(test[int(i)])
    
    x = np.asarray(xlist)
    y = np.asarray(ylist)

    plt.plot(x,y, 'b--')
    plt.grid(True)
    plt.title(f'{ctx.message.author}\'s Graph')
    plt.savefig(fname='plot')
    #print(os.path.dirname(os.path.realpath('plot.png')))
    with open("plot.png","rb") as tacos:
        t = discord.File(tacos, filename = "plot.png")
    await ctx.send(file = t)
    os.remove('plot.png')
    
    test.clear()
    xlist.clear()
    ylist.clear()


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
    
    
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename[:-3]}') # splice here will remove the .py from filename


client.run("NzM0MTMwMzUxMzIwMDcyMjU2.XxNOKw.NPDB1JKeeWwFEbYAg9punFTN_dM")
