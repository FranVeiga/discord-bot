import discord
from discord.ext import commands
import diccionario
import youtube_dl as yt
from youtube_search import YoutubeSearch
import os


class MusicBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix=command_prefix)
        
        self.queue=[]
   
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                    }],
                }  

    def yt_search(self, search_terms):
        result = YoutubeSearch(search_terms, max_results=1).to_dict()
        
        print(result)
        url_prefix = 'https://www.youtube.com'
        url_suffix = result[0]['url_suffix']
        
        url = url_prefix + url_suffix
        return url


    def to_audio_source(self, search):

        if search.startswith('https'):
            url = search
        else:
            url = self.yt_search(search)

        with yt.YoutubeDL(self.ydl_opts) as ydl:
            file = ydl.extract_info(url, download=True)
            path = str(file['title']) + "-" + str(file['id'] + ".mp3")

        return {'path' : path, 'audio_source' : discord.FFmpegPCMAudio(path)}




client = MusicBot(command_prefix='.')
secret = ''


@client.event
async def on_ready():
    print('ready')

@client.command(aliases=['cls'])
async def clear(ctx, no=0):
    if no != 0:
        await ctx.channel.purge(limit=no)
    else:
        await ctx.channel.purge()

@client.command(aliases=["def"])
async def _def(ctx, word, lang='eng'):
    definition = diccionario.define(lang, word)
    await ctx.send(definition)


@client.command()
async def join(ctx):
    try:
        channel = ctx.author.voice.channel
        await channel.connect() 
    except discord.ClientException as e:
        await ctx.channel.send("I'm already on another channel")

@client.command(aliases=['leave'])
async def disconnect(ctx):
    await ctx.voice_client.disconnect()


    
async def next_song(voice_client, playing=None):
    voice_client = ctx.voice_client
    if playing == None:
        current_song = client.queue.pop(0)
        voice_client.play(current_song['audio_source'], after=lambda x: next_song(playing=True))
        voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)
        remove_song(current_song['path'])
        os.remove(current_song['path'])
        
        
       




@client.command(aliases=['p', 'play', 'q'])
async def queue(ctx, search):
    
    if ctx.voice_client is None:
        await ctx.invoke(join)
    voice_client = ctx.voice_client

    client.queue.append(client.to_audio_source(search))
    
    if len(client.queue) == 1:
        next_song(voice_client) 

    voice_client.play(client.queue[0]['audio_source'], after=lambda x: endSong(self.queue[0]['path']))
    voice_client.source = discord.PCMVolumeTransformer(voice_client.source, 1)

@client.command()
async def a(ctx, *, url):
    pass



client.run(secret)


