import discord
import secret
from discord.ext import commands
from dataclasses import dataclass

bot = commands.Bot(command_prefix="!",intents=discord.Intents.all(),help_command=None)

@bot.event
async def on_ready():
    print("Hello! I'm the Frenzy Bot")
    channel = bot.get_channel(secret.CHANNEL)
    await channel.send("Hello! Welcome to the Channel")
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")
@bot.command()
async def add(ctx, *arr):
    result = 0
    for i in arr:
        result += int(i)
    await ctx.send(f"Result: {result}")
<<<<<<< HEAD
bot.run(BOT_TOKEN)   
#dominic added a comment 
=======
bot.run(secret.BOT_TOKEN)    
>>>>>>> 18e4fc9f73760aea32d3ccbac7440f33154b7083
