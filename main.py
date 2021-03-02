import discord
import time
import datetime

client = discord.Client()
#link do bota
TOKEN = 'ODE2MjkwMTU1Mjk1NjcwMzAy.YD4zcg.8vWNXdX4yR2HjvdJ6BeK9ErZ0Jk'

#tutaj coś robi

# @client.event
# async def on_ready():
#     general_channel = client.get_channel(816259598494466048)
#     print("online jestem")
#     await general_channel.send("tak pan bóg powiedział ")

while True:
    now = datetime.datetime.now()
    if str(now.hour) == '18' and str(now.minute) == '46':
        print("wybiła godzina na kremówke")
        @client.event
        async def on_ready():
            general_channel = client.get_channel(816259598494466048)
            print("online jestem")
            await general_channel.send("tak pan bóg powiedział ")
        break








#to coś go budzi do życia
client.run(TOKEN)
