#!/usr/bin/env python3
# message_bot.py
# Sends Discord reminders based on reminder json files in reminders directory
# Argument after script name should be the full path of the json file that
#   contains the reminder information
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
REMINDER_FILE = sys.argv[1]
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    if len(sys.argv) == 1:  # No parameters were given
        print("No parameters given to script, exiting...")
        await bot.close()
        return

    reminder = acquire_reminder(REMINDER_FILE)
    await send_reminder(reminder)

    await bot.close()


# Returns reminder loaded from given reminder json file
# FIXME: Consider using fcntl.flock() to avoid race conditions & file corruption
def acquire_reminder(reminder_file: str):
    with open(reminder_file) as json_file:
        reminder = json.load(json_file)
    return reminder


# Sends given reminder message to appropriate channel
async def send_reminder(reminder):
    server = discord.utils.get(bot.guilds, name=reminder["server"])
    channel = discord.utils.get(server.text_channels, name=reminder["channel"])
    await channel.send(reminder["message"])


bot.run(TOKEN)
