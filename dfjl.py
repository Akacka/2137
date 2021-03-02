import discord
import os
import requests
import json
import random
from replit import db

client = discord.Client()
sad_words = ["zły", "smutny", "depresja"]

starter_encouragements = [
    "cheer up",
    "hang in there"
]


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encuragements(encuraging_message):
    if "encuragements" in db.keys():
        encouregements = db["encouragements"]
        encouregements.append(encuraging_message)
        db["encouragements"] = encouregements
    else:
        db["encouragements"] = [encuraging_message]


def delete_encouragements(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    options = starter_encouragements
    if "encouragements" in db.keys():
        options + options + db["encouragements"]

    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(options))

    if msg.startswith('$new'):
        encuraging_message = msg.split("$new ", 1)[1]
        update_encuragements(encuraging_message)
        await message.channel.send("new encouraging message added. ")

    if msg.startswith('$del'):
        encuraging_message = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragements(index)
            encouragements = db["encouragements"]
            await message.channel.send(encouragements)


client.run(os.getenv('TOKEN'))