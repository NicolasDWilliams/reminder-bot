#!/usr/bin/env python3
# bot.py
# Sends Discord reminders
# Created by Nicolas Williams, 10/30/2020

import os
import json
import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Connect to Discord
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user.name} successfully connected to Discord.")
    if len(sys.argv) == 1:  # No parameters were given
        print("No parameters given to script, exiting...")
        await bot.close()
        return

    reminder = acquire_reminder()
    await send_reminder(reminder)

    # await channel.send(MESSAGE)
    await bot.close()


# Returns reminders stored in json file
# FIXME: Consider using fcntl.flock() to avoid race conditions & file corruption
def acquire_reminder():
    with open(f"reminders/{sys.argv[1]}") as json_file:
        reminder = json.load(json_file)
    return reminder


# Sends given reminder message to appropriate channel
async def send_reminder(reminder):
    server = discord.utils.get(bot.guilds, name=reminder["server"])
    channel = discord.utils.get(server.text_channels, name=reminder["channel"])
    await channel.send(reminder["message"])


bot.run(TOKEN)
