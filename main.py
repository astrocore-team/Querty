from re import I
from time import time
import discord
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model('Querty')

client = discord.Client()

Token = 'OTI5NDc5OTE5Nzc0MzQzMjcx.Ydn7oQ.0Yvn_4eXCdCKS5OVAbaICnzCPYE'

@client.event
async def on_message(ctx):
    if ctx.author == client.user or ctx.content.startswith('?purge'):
        return
    
    if ctx.channel.name == 'general':
        response = chatbot.request(ctx.content)
        await ctx.channel.send(response)

client.run(Token)