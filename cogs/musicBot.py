import discord
from discord.ext import commands
from discord.utils import get
import os
import asyncio
import youtube_dl
import re
import typing as t

#import opuslib.api
#import opuslib.api.decoder
#import opuslib.api.ctl
#import opuslib

URL_REGEX = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

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

class Queue():
    
    def __init__(self):
        self.queue = []
        self.position = 0
    
    def add(self, *args):
        
        self.queue.extend(args)
        
        
    def get_first(self):
        
        if not self.queue:
            raise QueueIsEmpty
        
        return self.queue[0]
    
    def next(self):
        
        if not self.queue:
            raise QueueIsEmpty
        
        self.position += 1
        if self.position > len(self.queue) - 1:
            return None
        
        return self.queue[self.position]
    
    
client = commands.Bot(command_prefix = "$")
class MusicBot(commands.Cog):
    
    def __init__(self, client):
        self.client = client
        """
        super().__init__(*args, **kwargs)
        self.queue = Queue()
        """
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
                await ctx.send("You can't disconnect me from {0} when you are in {1}".format(bot_voice_channel, user_voice_channel))
            else:
                await voice.disconnect() # Disconnects the voice client
                await ctx.send("This place is getting kind of stale")
        
        else:
            await ctx.send("There is no instance of this bot to disconnect from this voice channel currently")
            
    @commands.command(aliases = ["Suzie", "p"])
    async def play(self, ctx):
        await self.client.get_command("join").callback(self, ctx) # Joins the channel the user is in
        
        global song
        
        # Gets voice channel of message author
        user_voice_channel = ctx.message.author.voice.channel
        voice = get(self.client.voice_clients, guild=ctx.guild)
        
        if voice and voice.is_connected():
            
            player = voice.create_ffmpeg_player(song)
            player.start()
        
        
        """
        query = query.strip("<>")
        if not re.match(URL_REGEX, query):
            query = f"ytsearch:{query}"
       
        
        voice.play(discord.FFmpegPCMAudio(executable="Users/justinbeutel/Downloads/ffmpeg", source= song))
        # Sleep while audio is playing.
        while voice.is_playing():
            sleep(.1)
        await voice.disconnect()
        
        await ctx.message.delete()
        """       
    
def setup(client):
    
    client.add_cog(MusicBot(client))
    