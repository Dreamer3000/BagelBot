import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.utils import get
import sys

class DiscordIDE(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        # functions in a class need this to function
        print("Ready to Code Boss")
    
    @commands.Cog.listener()
    async def on_message(self, message):
        try:
            if message.content.startswith("$run"):
               
                channel = message.channel
                author = message.author

                with open(str(author) + ".txt", "w") as t:
                  
                    sys.stdout = t
                    exec(message.content[5:])
                    
                    t.close()
                test = ""
               
                with open(str(author) + ".txt", "r") as t:
                    
                    for line in t:
                        for character in line:
                            test += character
                    
                    t.close()
                   
                await channel.send("Hey " +  author.mention + ", your code is done!")
                
                code = ""
                counter = 0
                for line in message.content[5:].split("\n"):
                    counter += 1
                    code += str(counter)+ "." + line + "\n"
                
                await channel.send("                    ============ ** Code **: ============")
                await channel.send('\n```\n{}\n```'.format(code))
                await channel.send("                    =========== ** Output **: ============")
                
                await channel.send('\n```\n{}\n```'.format(test))
        
        except:
            await channel.send("Input error! Please check your input, or contact the head pastiere")
    



    

def setup(client):
    
    client.add_cog(DiscordIDE(client))