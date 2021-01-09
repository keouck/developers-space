import discord
import os
from load_files import load_files
import re
from discord.ext import commands



client = discord.Client()
react_role_emojis, help_text = load_files()
pattern = re.compile(r'(re+\b)')

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
        await message.channel.send(
            'Hello whalecome :whale: to DS! What language are you learning?')

    elif message.content.lower() == 'to the guillotines!':
        await message.channel.send('Haha joke stealing go brrrrrr')


    elif message.content.lower() == '***tok***':
        await message.channel.send('Yes, ***tok***')

    elif message.content.lower() == 'im sad':
        await message.channel.send('***sed***')

    elif message.content.lower() == 'no u':
        await message.channel.send(
            'https://tenor.com/view/reverse-nozumi-uno-jojo-card-gif-15706915')


    elif message.content.lower() == 'good choice':
        await message.channel.send('Yes, very good indeed')

    elif pattern.match(main_arg):
        await message.channel.send(
            'https://tenor.com/view/ree-pepe-triggered-angry-ahhhh-gif-13627544'
        )
    elif main_arg == 'Hello':
        await message.channel.send('ello')

    elif main_arg == 'ello':
        await message.channel.send('Hai')


    elif 'https://tenor.com/view/revive-rise-up-dancing-dorito-dance-i-revive-this-chat-gif-16381411' in message.content:
        await message.channel.send('Haha joke stealing go brrrrrr')

    elif message.content.lower() == '!perms':
        await message.channel.send('Amay has no perms :{')
    elif message.content.lower() == '!help':
        await message.channel.send(help_text)
    elif main_arg == '!nohi':
        await message.channel.send(
            "Don't just say Hi in chat, you can get help a lot faster by skipping unnessasary conversastion \n https://www.nohello.com/"
        )
    elif main_arg == '!dontasktoask':
        await message.channel.send(
            "don't just ask to ask we would rather have you ask your question directly instead since it saves time \n https://dontasktoask.com/"
        )
    elif main_arg == '!thexyproblem':
        await message.channel.send(
            "Your problem is X but your question is Y i.e you are asking about your _attempted_ solution rather than you actual question,\n this leads to enormorus amounts of wasted time and energy on both sides(you and the person who's helping) \n https://xyproblem.info/"
        )
    elif main_arg == "!google":
        await message.channel.send("Google your issues first \n www.google.com"
                                   )
    elif main_arg == "!ioc":
        await message.delete()
        await message.channel.send(
            "An Image of code isn't helpful use a codeblock instead")
    elif main_arg == "tok":
        await message.channel.send("***tok***")
    elif main_arg == "!cb":
        await message.channel.send('''surround your code with 3 backticks \``` like this \``` and type the name of your language in (discord formatting) after the first three backticks. For example:
        
\```python
print('hello world!') 
```''')
        await message.channel.send('''         
         

Makes:

```python
print('hello world!') 
```''')   

#roles select
@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 796613349835669544:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
        # reeee python doesn't have switch statements
        if payload.emoji.name in react_role_emojis:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)
        else:
            role = discord.utils.get(guild.roles, name=payload.emoji.name)

        if role is not None:
            member = payload.member
            print(member)
            if member is not None:
                await member.add_roles(role)
               
                print("done")
            else:
                print('Member not found')
                print(role)
        else:
            print('Role not found')

bot = commands.Bot(command_prefix='!')

@commands.command()

@commands.has_permissions(kick_members=True)

async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.send(f'User {member} has been yeeted')
    await client.kick(member)

client.run(os.getenv('TOKEN'))

  