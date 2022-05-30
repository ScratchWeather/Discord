from nextcord.ext import commands
import requests
import json
import nextcord
import asyncio

bot = commands.Bot(command_prefix='!')
client = nextcord.Client()

@bot.command()
async def offline(ctx):
    exit()

@bot.command()
async def type(ctx, sec):
    await ctx.trigger_typing()
    await asyncio.sleep(sec)

bot.run('token')
