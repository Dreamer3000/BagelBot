import discord
from discord.ext import commands
from discord.utils import get
import os
import asyncio
import youtube_dl

#import opuslib.api
#import opuslib.api.decoder
#import opuslib.api.ctl
#import opuslib


Songs_Folder = "Users/justinbeutel/Music/iTunes/iTunes media/Music/Unknown Artist/"
song = '/Users/justinbeutel/Music/iTunes/iTunes Media/Music/Unknown Artist/Unknown Album/Vs Susie - Remix Cover (Deltarune).mp3'
Sogns_list = []
Current_Song = 0

YDL_OPTS = {
    "outtmpl": song + "%(title)s.%(ext)s",
    "format": "bestaudio/best",
    "postprocessors": [{
        "key": "FFmpegExtractAudio",
        "preferredcodec": "mp3",
        "preferredquality": "192",}],
    }

client = commands.Bot(command_prefix = "$")
class MusicBot(commands.Cog):
    
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        # functions in a class need this to function
        print("Music's ready to play Boss")
    #global song, Songs_Folder
    #discord.opus.load_opus('opus')
    
    @commands.command()
    async def join(self, ctx):
        user_voice_channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        #VoiceChannel.connect()
    
        if voice and voice.is_connected():
            await ctx.send("Logged in, ready to toast")
        else:
            voice = await user_voice_channel.connect()
            await ctx.send("Logged in, ready to toast")
    
    @commands.command()
    async def leave(self,ctx):
        
        user_voice_channel = ctx.message.author.voice.channel # The voice channel the user is in
        voice = get(self.client.voice_clients, guild=ctx.guild) # Gets the specific bot voice client the user wants to disconnect

        if voice and voice.is_connected(): # If there is a bot voice client, and it is connected
            bot_voice_channel = voice.channel
            
            if user_voice_channel != bot_voice_channel: # If the user and bot are in different channels
                await ctx.send("You cannot disconnect this bot from {0} when you are in {1}".format(bot_voice_channel, user_voice_channel))
            else:
                await voice.disconnect() # Disconnects the voice client
                await ctx.send("this bot has been disconnected from {0}".format(user_voice_channel))
        
        else:
            await ctx.send("There is no instance of this bot to disconnect from this voice channel currently")
            
    @commands.command(aliases = ["Suzie", "p"])
    async def play(self,ctx):
        await self.client.get_command("join").callback(self, ctx) # Joins the channel the user is in
        
        global song
        
        # Gets voice channel of message author
        user_voice_channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
       
        
        voice.play(discord.FFmpegPCMAudio(executable="Users/justinbeutel/Downloads/ffmpeg", source= song))
        # Sleep while audio is playing.
        while voice.is_playing():
            sleep(.1)
        await voice.disconnect()
        
        await ctx.message.delete()
                
    
def setup(client):
    
    client.add_cog(MusicBot(client))
    