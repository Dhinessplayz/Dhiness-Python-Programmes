import discord
import random
import os
import pywintypes
from win10toast import ToastNotifier

TOKEN = 'ODg5NTIwNjcwNzY4MjM0NTc2.YUicrg.1K4hdBBLvQzgyIJnVFtHO9K7tUc'

client = discord.Client()

toast = ToastNotifier()
toast.show_toast("HeckOrganiser","Hecker has been activated", duration = 30)
os.chdir("C:\Dhiness\Python\Hecker BOt")


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({username})')

    if message.author == client.user:
        return

    if message.channel.name == 'hecker-wrld':
        if user_message.lower() == 'hecker':
            await message.channel.send(f'What do you want?')
            return
        elif user_message.lower() == 'heck me':
            await message.channel.send(f'Alright... Your username is {username}... I am good at hecking people')
            return
        elif user_message.lower() == 'protect me':
             await message.channel.send(f'Alright. I will but in return you need to give me one million dollars. Is that ok {username}')
             return
        elif user_message.lower() == 'can i be a hecker':
            await message.channel.send(f'No!')
            return
        elif user_message.lower() == 'why':
            await message.channel.send(f'because you have to learn to become a hecker from the master who lives in Antartica but died because of old age...')
            return
        elif user_message.lower() == 'heck dyno':
            await message.channel.send(f'Dyno hack activated... First Attack... Success... Access reach.... Success.... Acess Granted.... override access breach.... Breach successfull.... {username} is Dyno')
            return

    if message.channel.name == 'general':
        if user_message.lower() == 'my friend hecker will heck you':
            await message.channel.send(f'Ye. I will help {username} to heck anyone. But if the other person pays me 99999999999 then I will work for them...')
            return
        elif user_message.lower() == 'bruh':
            await message.channel.send(f'You have been hecked because you said the keyword "bruh"...')
            return
        elif user_message.lower() == 'heck dyno':
            await message.channel.send(f'Dyno hack activated... First Attack... Success... Access reach.... Success.... Acess Granted.... override access breach.... Breach successfull.... {username} is Dyno')
            return
        elif user_message.lower() == 'hello':
            await message.channel.send(f'User Attack activated... First Attack... Success... Access reach.... Success.... Acess Granted.... override access breach.... Breach successfull.... {username} has no access over their account @Hecker🖤 has control of {username} account. I will give the password to the person that pays me the most... DM @Dhiness for the bidding... 🖤🖤🖤')
            return


client.run(TOKEN)
