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
ERR_LOG_FILE = "err.log"
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    if len(sys.argv) == 1:  # No parameters were given
        print_error("No parameters given to script, exiting...")
        # TODO: Print usage
        await bot.close()
        return

    REMINDER_FILE = sys.argv[1]

    reminder = acquire_reminder(REMINDER_FILE)

    await send_reminder(reminder)

    await bot.close()


# @bot.event
# async def on_error(event, *args, **kwargs):
#     with open (ERR_LOG_FILE, 'a') as f:
#         if event == "on_ready":
#             f.write(f"


# Returns reminder loaded from given reminder json file
# FIXME: Consider using fcntl.flock() to avoid race conditions & file corruption
# FIXME: errors for when file is...
# - doesn't exist
# - can't be parsed
def acquire_reminder(reminder_file: str):
    with open(reminder_file) as json_file:
        # TODO: Error checking - can't be parsed
        reminder = json.load(json_file)

    # TODO: Validation of json file
    return reminder


# Sends given reminder message to appropriate channel
# FIXME: errors when...
# - server doesn't exist
# - channel doesn't exist
# - message can't be sent in channel
async def send_reminder(reminder):
    server = discord.utils.get(bot.guilds, name=reminder["server"])
    channel = discord.utils.get(server.text_channels, name=reminder["channel"])
    await channel.send(reminder["message"])


def print_error(message):
    with open(ERR_LOG_FILE, "a") as f:
        f.write(message)


bot.run(TOKEN)
