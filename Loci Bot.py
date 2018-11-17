# Loci by Jacob - TheGamePugYT

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print ("Ready when you are xd")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: ping!! xSSS")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title=":information_source: Infomation", description="Desc", color=#0000FF)
    embed.add_field(name="The users name isat(u: {}".formser.name), value="hi", inline=False)
    embed.add_field(name="The users ID is: {}".format(user.id), value="hi2", inline=False)
    await client.send_message(message.channel, embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say(":boot: Cya, {}. Little".format(user.name))
    await bot.kick(user)

bot.run("B0T_TOKEN")