import discord
import secret
import urllib
import requests
import json
from discord.ext import commands
from dataclasses import dataclass

#SATURDAY HACKNIGHT
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
@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = 'Help',
        description = 'All bot commands are provided below',
        color = discord.Color.red()

    )
    embed.add_field(name='Commands',value='`simplify`,`inversecosine`,`inversesine`,`inversetan`,`absolute`,`log`,`factor`,`integrate`,`derive`,`zeroes`,`cos`,`sin`,`tan`,`areaundercurve`',inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def simplify(ctx,a):
    val = urllib.parse.quote_plus(a)
    url = "https://newton.now.sh/api/v2/simplify/"+val
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")
@bot.command()
async def inversecosine(ctx,a):
    url = "https://newton.now.sh/api/v2/arccos/"+a
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")

@bot.command()
async def inversesine(ctx,a):
    url = "https://newton.now.sh/api/v2/arcsin/"+a
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}") 
@bot.command()
async def inversetan(ctx,a):
    url = "https://newton.now.sh/api/v2/arctan/"+a
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")      
@bot.command()
async def absolute(ctx,a):
    url = "https://newton.now.sh/api/v2/abs/"+a
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")
@bot.command()
async def log(ctx,a):
    url = "https://newton.now.sh/api/v2/log/"+a
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")      
 
@bot.command()
async def derive(ctx,a):
    val = urllib.parse.quote_plus(a)
    url = "https://newton.now.sh/api/v2/derive/"+val
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")


@bot.command()
async def factor(ctx,a):
    val = urllib.parse.quote_plus(a)
    url = "https://newton.now.sh/api/v2/factor/"+val
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")
 
@bot.command()
async def integrate(ctx,a):
    val = urllib.parse.quote_plus(a)
    url = "https://newton.now.sh/api/v2/integrate/"+val
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")
@bot.command()
async def zeroes(ctx,a):
    val = urllib.parse.quote_plus(a)
    url = "https://newton.now.sh/api/v2/zeroes/"+val
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")    
@bot.command()
async def cos(ctx,a):
    val = urllib.parse.quote_plus(a)
    url = "https://newton.now.sh/api/v2/cos/"+val
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")



@bot.command()
async def sin(ctx,a):
    val = urllib.parse.quote_plus(a)
    url = "https://newton.now.sh/api/v2/sin/"+val
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")


@bot.command()
async def tan(ctx,a):
    val = urllib.parse.quote_plus(a)
    url = "https://newton.now.sh/api/v2/tan/"+val
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")    
@bot.command()
async def  areaundercurve(ctx,a):
    val = urllib.parse.quote_plus(a)
    url = "https://newton.now.sh/api/v2/area/"+val
    response = requests.get(url)
    get_json = json.loads(response.text)
    await ctx.send(f"Result:{get_json['result']}")    
 
    

bot.run(secret.BOT_TOKEN)
    
     

