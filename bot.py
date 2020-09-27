import discord
from discord.ext import commands
import diccionario

client = commands.Bot(command_prefix='.')
secret = 'your token'

# variable that stores the bot's voice connection (if any) 
client.voice_connection = None

@client.event
async def on_ready():
    print('ready')

@client.command(aliases=['cls'])
async def clear(ctx, no=0):
    if no != 0:
        await ctx.channel.purge(limit=no)
    else:
        await ctx.channel.purge()

@client.command()
async def ping(ctx):
    await ctx.channel.send(f'{round(client.latency * 1000)}ms')

@client.event
async def on_typing(channel, user, when):
    if isinstance(channel, discord.DMChannel):
       await channel.send(content="Que escribís puto")

@client.command(aliases=["def"])
async def _def(ctx, word, lang="eng"):
    definition = diccionario.define(lang, word)
    await ctx.send(definition)



@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect() 

@client.command(aliases=['leave'])
async def disconnect(ctx):
    await ctx.voice_client.disconnect()
    


client.run(secret)


