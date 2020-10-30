#!/usr/bin/env python3
# bot.py
# Script that sends the actual reminder
# Created by Nicolas Williams, 10/30/2020

# Webpage with instructions on Discord bots
# https://realpython.com/how-to-make-a-discord-bot-python/

import os
import json

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Connect to client
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')
client = discord.Client()

@client.event
async def on_ready():
    print("on_ready()")
    guild = discord.utils.get(client.guilds, name=SERVER)
    reminders = acquire_due_reminders()
    for r in reminders:
        channel = discord.utils.get(guild.text_channels, name=r['channel'])
        await channel.send(r['message'])


    # await channel.send(MESSAGE)
    await client.close()


def acquire_due_reminders():
    with open('due_reminders.json') as json_file:
        data = json.load(json_file)
    return data


client.run(TOKEN)
