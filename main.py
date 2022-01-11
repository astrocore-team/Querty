from re import I
from time import time
import discord
from neuralintents import GenericAssistant

chatbot = GenericAssistant('intents.json', model_name="Querty")
chatbot.train_model()
chatbot.save_model()

client = discord.Client()

Token = 'Token'

@client.event
async def on_message(ctx):
    if ctx.author == client.user or ctx.content.startswith('?purge'):
        return
    
    if ctx.channel.name == 'general':
        response = chatbot.request(ctx.content)

        await ctx.channel.send(response)

client.run(Token)