import discord
from discord.ext import commands
import diccionario

client = commands.Bot(command_prefix='.')
secret = 'your secret'

@client.event
async def on_ready():
    print('ready')

@client.event
async def on_typing(channel, user, when):
    if isinstance(channel, discord.DMChannel):
       await channel.send(content="Que escribís puto")

@client.command(aliases=["def"])
async def _def(ctx, word, lang="eng"):
    definition = diccionario.define(lang, word)
    await ctx.send(definition)


@client.command()
async def hola(ctx):
    await ctx.send("hola")



client.run(secret)


