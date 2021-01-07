import discord
import os

client = discord.Client()
help_text = """
 
```Help```
Brings you here


```Welcome to DS```
Output: Hai whale come :whale: to DS! What language are you learning?


```to the guillotines!```
Output: Haha joke stealing go brrrrrr


```im sad```
Output: ***sed***


```elo/ello```
Output: Hai


```https://tenor.com/view/revive-rise-up-dancing-dorito-dance-i-revive-this-chat-gif-16381411'```
Output: Haha joke stealing go brrrrrr


```!perms```
Output: Amay has no perms :{
"""
@client.event

async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event

async def on_message(message):
  if message.author == client.user:
    return
  
  args = message.content.lower().split(" ")
  main_arg = args[0]
  print(message.content)
#todo de memeify the code
  if message.content.lower() == 'welcome to ds':
    await message.channel.send('Hello whalecome :whale: to DS! What language are you learning?')

  elif message.content.lower() == 'to the guillotines!':
    await message.channel.send('Haha joke stealing go brrrrrr')
  
  elif message.content.lower() == 'im sad':
    await message.channel.send('***sed***')

  elif message.content.lower() == 'good choice':
    await message.channel.send('Yes, very good indeed')

  if main_arg == 'Hello':
    await message.channel.send('ello')

  elif main_arg == 'ello':
    await message.channel.send('Hai')
  elif main_arg == 'NoHi':
    await message.channel.send('')

  elif main_arg == \
  'https://tenor.com/view/revive-rise-up-dancing-dorito-dance-i-revive-this-chat-gif-16381411':
    await message.channel.send('Haha joke stealing go brrrrrr')

  elif main_arg == '!perms':
    await message.channel.send('Amay has no perms :{')
  
  elif main_arg == "!help":
    await message.channel.send(help_text)

  # logging

  with open("devspace_log.txt", "a") as f:
    f.write(message.content + "\n")

@client.event

async def on_raw_reaction_add(payload):
  message_id = payload.message_id
  if message_id ==  796613349835669544:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    # guild()
# TODO add more langs
# reeee python doesn't have switch statements
    if payload.emoji.name == 'cpp':
      role = discord.utils.get(guild.roles, name = 'cpp')
    elif payload.emoji.name == 'python':
      role = discord.utils.get(guild.roles, name = 'python')
    else:
      role = discord.utils.get(guild.roles, name=payload.emoji.name)

    if role is not None:
      print(role.name)

async def on_raw_reaction_remove(payload):
  pass

client.run(os.getenv('TOKEN'))