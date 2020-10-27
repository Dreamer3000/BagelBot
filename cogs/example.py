import discord
from discord.ext import commands

client = commands.Bot(command_prefix = "$")
class Example(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        # functions in a class need this to function
        print("We have logged in as {0.user}".format(client))
    
    @commands.command()
    async def something(self,ctx):
        #await ctx.send(
        pass
    

def setup(client):
    
    client.add_cog(Example(client))