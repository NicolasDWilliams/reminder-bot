#!/usr/bin/env python3
# bot.py
# Responsible for interacting with users to create, edit, and remove reminders
# Created by Nicolas Williams, 10/31/2020

# TODO:
# TODO: Restrict reminder creation to leads
# TODO: Handle messages & channels that break json formatting (quotes, slashes)
# TODO: Create & write to err / logfile (for bot & message_send bot)
# Create log_print() function

import os
import json
import sys

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
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print(f"{bot.user.name} successfully connected to Discord.")


# TODO: Implement this command
# @bot.command
# def create_reminder

# TODO: Implement this command
# @bot.command
# def delete_reminder

# TODO: Implement this command
# @bot.command
# def list_reminders

# TODO: Implement this function
# def construct_reminder_obj(channel, message, cron_time):

# TODO: Implement this function
# def write_json(reminder):

# TODO: Implement this function
# def create_cron_job(reminder)

bot.run(TOKEN)
