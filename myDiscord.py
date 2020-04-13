# bot.py
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import syslog
import arkCommands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = os.getenv('DISCORD_PREFIX')

bot = commands.Bot(command_prefix=PREFIX)

@bot.event
async def on_ready():
    #guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    guild = discord.utils.get(bot.guilds, name=GUILD)
    syslog.syslog(syslog.LOG_INFO, f'{bot.user.name} verbunden mit {guild.name}(id: {guild.id}')
    members = '\n - '.join([member.name for member in guild.members])
    syslog.syslog(syslog.LOG_INFO, f'Guild Members:\n - {members}')


@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


@bot.command(name='arkmanager', help='ARK Server status from arkmanager, you can add arguments')
async def arkstatus(ctx, command: str = "list-instances", command2: str = "", command3: str = ""):
    command_list = ["arkmanager", command]
    if command2 != "":
        command_list.append(command2)
    if command3 != "":
        command_list.append(command3)
    result = await arkCommands.arkmanager(command_list)
    await ctx.send(result)


@bot.command(name='dig', help='ARK Server status from gamedig, you can add the argument PORT (27015) of the ARK server')
async def arkstatus(ctx, port: str = "27015"):
    result = await arkCommands.dig(port)
    await ctx.send(result)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        syslog.syslog(syslog.LOG_ERR, 'discord bot command error')
        await ctx.send('You do not have the correct role for this command.')


bot.run(TOKEN)
