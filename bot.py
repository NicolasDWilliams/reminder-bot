#!/usr/bin/env python3
# bot.py
# A Discord bot for reminders in WolverineSoft Studio
# Created by Nicolas Williams, 10/30/2020

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

client.run(TOKEN)
