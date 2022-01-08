import os
import time
from re import I
from time import time
import discord
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model('Core')

client = discord.Client()

Token = 'OTI5NDc5OTE5Nzc0MzQzMjcx.Ydn7oQ.0Yvn_4eXCdCKS5OVAbaICnzCPYE'



@client.event
async def on_message(message):
    if message.author == client.user or message.content.startswith('?purge'):
        return
    
    if message.content.startswith('$ban'):
     await message.channel.send('*Tee Hee*')
     return

    if message.content.startswith('$spam'):
     for I in range(1000):
         await message.channel.send('@everyone HAHA Querty got hacked')
         time.sleep(0.1)
     return

    if message.channel.name == 'general':
        response = chatbot.request(message.content)
        await message.channel.send(response)

client.run(Token)