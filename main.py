import json
from re import I
from time import time
import json
from discord.ext.commands import bot
from discord.ext.commands.bot import Bot
from discord_slash import SlashCommand
from discord.ext import commands, tasks
import discord
from discord import message
from discord import channel
from discord_slash.utils.manage_commands import create_option
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json', model_name="Querty")
chatbot.train_model()
chatbot.save_model()

intents = discord.Intents.all()
client = commands.Bot(command_prefix='!', intents=intents)
slash = SlashCommand(client, sync_commands=True)

Token = 'Token'

channel_dict = {}

f = open("storage.json", "w")
json.dump(channel_dict, f)

@slash.slash(name="Channel", description="Choose Querty chat channel", options=[create_option(name="channel", description="Channel", option_type=7, required=True) ])
async def Channel(ctx, channel: discord.TextChannel):
    guild = ctx.guild.id
    
    channel_dict[guild] = channel

    print(channel_dict)

    json.dump(channel_dict, f)

@client.command()
async def Channel(ctx, channel: discord.TextChannel):
    guild = ctx.guild.id
    
    channel_dict[guild] = channel

    print(channel_dict)

    json.dump(channel_dict, f)

@client.event
async def on_message(ctx):
    guild = ctx.guild.id
    print(channel_dict.get(guild))

    if ctx.author == client.user or ctx.content.startswith('?purge'):
        return
    
    if ctx.channel.name == channel_dict.get(guild):
        response = chatbot.request(ctx.content)

        await ctx.channel.send(response)

f.close()
client.run(Token)