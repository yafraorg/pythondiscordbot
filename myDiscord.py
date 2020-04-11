# bot.py
import os
import random
import subprocess
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    #guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    guild = discord.utils.get(bot.guilds, name=GUILD)

    print(
        f'{bot.user.name} verbunden - ARK Server Management Bot von nissle.ch:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@bot.command(name='status')
async def nine_nine(ctx):
    result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    response = result.stdout
    await ctx.send(response)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


bot.run(TOKEN)
