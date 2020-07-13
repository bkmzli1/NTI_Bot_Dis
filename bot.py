import discord
from discord.ext import commands

import config
client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)



def thread_bot():
    bot.run(config.TOKEN)
