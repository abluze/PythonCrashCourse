# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = discord.Client()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    print(f'Connected to {bot.guilds}')

@bot.event
async def on_message(message):
  print(f'message from:{message.author} received by:{bot.user}')
  if message.author == bot.user:
    return

  msg = message.content.lower()

  print(f'message received: {msg}')

  if msg == 'hello':
    await message.channel.send(f'hello, {message.author.name}')
  elif msg == 'bye':
    await message.channel.send(f'farewell, {message.author.name}')

  # do a google search for msg 
  # find the first image, and respond with that image 
  

#@bot.event
#async def on_message(message):
#    await member.create_dm()
#    await member.dm_channel.send(
#        f'Hey, {member.name}!'
#    )
      
bot.run(TOKEN)