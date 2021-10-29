import discord
import os
import time
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix = 'EB!', case_intensitive=True)

@bot.event
async def on_ready():
  await bot.change_presence(activity=discord.Game(name="Example Status"))
  print("bot on!")
  time.sleep(5)

@bot.command()
async def command(ctx):
   await ctx.channel.send("message")

bot.run(os.getenv("TOKEN"))
