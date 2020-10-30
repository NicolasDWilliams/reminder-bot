#!/usr/bin/env python3
# bot.py
# A Discord bot for reminders in WolverineSoft Studio
# Created by Nicolas Williams, 10/30/2020

# Webpage with instructions on Discord bots
# https://realpython.com/how-to-make-a-discord-bot-python/

import os

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

client = discord.Client()

# An event is something that happens on Discord that you can use to trigger a
# reaction in your code. Your code will listen for and then respond to events.
# TODO: Allow reminders to be created based on createReminder command
#   - define message, channel, mention targets, reactions, frequency & time

# TODO: Send a message in the discord with the reminder

# TODO: React to the reminder with relevant reactions

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == SERVER:
            break

    print(
            f"{client.user} is connected to the following server:\n"
            f"{guild.name} (id: {guild.id})"
            )
    channel = discord.utils.get(guild.text_channels, name="general")
    await channel.send('This is a test message')

client.run(TOKEN)
