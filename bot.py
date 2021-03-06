#!/usr/bin/env python3
# bot.py
# Responsible for interacting with users to create, edit, and remove reminders
# Created by Nicolas Williams, 10/31/2020

# TODO: Restrict reminder creation to leads
# TODO: Handle messages & channels that break json formatting (quotes, slashes)
# TODO: Create & write to err / logfile (for bot & message_send bot)
# Create log_print() function

import os
import json
import sys
import signal

from crontab import CronTab
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Connect to Discord
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
# Virtual environment Python executable
PYTHON_EXEC = os.getenv("PYTHON_EXEC_PATH")
# Directory that holds reminders messages
REMINDERS_DIR = os.getenv("REMINDERS_DIR")
# Location of bot.py script (this script)
BOT_PATH = os.getenv("BOT_SCRIPT_PATH")
bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print(f"{bot.user.name} successfully connected to Discord.")


# TODO: Validate that user is a lead
# TODO: Validation
# - User is lead
# - Hour not negative
# - dow is valid
# - channel exists
# - compare channel text vs ID (if they use #)

# TODO: Show usage of function or else nobody can use it

# TODO: Handle Errors
# - wrong # params
# - nickname already taken
# - resolve nickname spaces
@bot.command(name="create_reminder", help="Creates a reminder")
async def create_reminder(
    ctx,
    reminder_nickname: str,
    given_message: str,
    given_channel: str,
    given_hour: str,
    given_dow: str,
):
    print(
        f"Command received: $create_reminder \n\tmsg={given_message}\n\tchannel={given_channel}\n\thour={given_hour}\n\tdow={given_dow}"
    )

    # FIXME: Validate parameters
    # test variables for after validation
    server = ctx.guild.name
    channel = given_channel
    message = given_message
    hour = given_hour
    minute = 0
    dom = "*"
    month = "*"
    dow = given_dow

    # TODO: Validate & affirm action with user

    # TODO: Construct json file
    json_obj = {
        "server": server,
        "channel": channel,
        "message": message,
    }

    json_file_path = f"{REMINDERS_DIR}/{reminder_nickname}.json"
    with open(json_file_path, "w") as f:
        json.dump(json_obj, f, indent=4)

    # TODO: Save json file

    # TODO: Create cronjob time string
    seperator = " "
    cron_command = seperator.join([PYTHON_EXEC, BOT_PATH, json_file_path])
    cron_entry = create_cron_entry(minute, hour, dom, month, dow, cron_command)

    # Write the cron job


# TODO: Implement this command
@bot.command(name="delete_reminder", help="Deletes stored reminders")
async def delete_reminder(ctx, reminder_name):
    await ctx.send(
        f"{ctx.message.author.mention} So this is awkward...\n"
        "The 'delete_reminder' command has not yet been implemented. So"
        " you'll need to DM Nico Williams and ask him to delete the reminder"
        " for you. Sorry for the inconvenience!"
    )


# TODO: Implement this command
# @bot.command
# def list_reminders

# TODO: Implement this function
# def construct_reminder_obj(channel, message, cron_time):

# TODO: Implement this function
# def write_json(reminder):

# TODO: Implement this function
# def create_cron_job(reminder)

# TODO: Implement this function
# @bot.command
# def shutoff_bot(ctx):

# Close the Discord bot
async def close_bot(disc_bot):
    print("Closing Discord bot...")
    await disc_bot.close()


# Validates components of a potential cron entry and returns the entry as a
# string
# TODO: Make sure dow is capitalized or a number
def create_cron_entry(minute, hour, dom, month, dow, command):
    seperator = " "
    cron_minute = str(minute)  # 0-59
    cron_hour = str(hour)  # 0-23
    cron_dom = str(dom)  # 1-31
    cron_month = str(month)  # 1-12
    cron_dow = str(dow)  # 0-7 (0 & 7 both represent Sunday)

    # Create cronjob command
    cron_command = command

    cron_str = seperator.join(
        [cron_minute, cron_hour, cron_dom, cron_month, cron_dow, cron_command]
    )
    print(f"Resulting cron string:\n\t{cron_str}")
    return cron_str


bot.run(TOKEN)
