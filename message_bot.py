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


class ReminderError(Exception):
    pass


class GuildError(Exception):
    pass


# Connect to Discord
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
ERR_LOG_FILE = "err.log"
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    if len(sys.argv) == 1:  # No parameters were given
        print_error("No parameters given to script, exiting...")
        # TODO: Print correct usage of the script
        close_bot()
        return

    REMINDER_FILE = sys.argv[1]

    try:
        reminder = acquire_reminder(REMINDER_FILE)

        validate_reminder(reminder)

        await send_reminder(reminder)
    except:
        print_error(f"Errors have occured. Closing program.")
        await close_bot()
        return

    await close_bot()


# @bot.event
# async def on_error(event, *args, **kwargs):
#     with open (ERR_LOG_FILE, 'a') as f:
#         if event == "on_ready":
#             f.write(f"


# Returns reminder loaded from given reminder json file
# FIXME: Consider using fcntl.flock() to avoid race conditions & file corruption
def acquire_reminder(reminder_file: str):
    try:
        with open(reminder_file) as json_file:
            # TODO: Error checking - can't be parsed
            reminder = json.load(json_file)
    except IOError as e:
        print_error(f"ERROR: File {reminder_file} doesn't exist.")
        raise e
    except json.decoder.JSONDecodeError as e:
        print_error(f"PARSE_ERROR: file '{reminder_file}' could not be decoded.")
        raise e

    # TODO: Validation of data acquired from JSON file
    return reminder


# TODO: Write this function
# Validates the information within a reminder acquired from a json file
def validate_reminder(reminder: dict):
    # validate all required keys exist
    required_keys = ["server", "channel", "message"]
    for prop_key in required_keys:
        if prop_key not in reminder:
            # missing a required property key
            print_error(
                f"REMINDER_ERROR: Reminder json file is missing the key '{prop_key}'"
            )
            raise REMINDER_ERROR


# Sends given reminder message to appropriate channel
# FIXME: errors when...
# - server doesn't exist
# - channel doesn't exist
# - message can't be sent in channel
async def send_reminder(reminder):
    # TODO: Try to make this more pretty / less try statements
    server = discord.utils.get(bot.guilds, name=reminder["server"])
    if server == None:
        print_error(f"ERROR with finding server '{reminder['server']}'")
        raise GuildError
    channel = discord.utils.get(server.text_channels, name=reminder["channel"])
    if channel == None:
        print_error(f"ERROR with finding channel'{reminder['channel']}'")
        raise GuildError
    try:
        await channel.send(reminder["message"])
    except:
        print_error(f"ERROR with sending message in channel '{reminder['channel']}'")
        raise


def print_error(message):
    print(message)
    with open(ERR_LOG_FILE, "a") as f:
        f.write(message)


async def close_bot():
    print_error("Closing bot...")
    await bot.close()


bot.run(TOKEN)
