#!/usr/bin/env bash
# Test message_bot.py with errors that should result in logout
MSG_BOT="../message_bot.py"

# Run without reminder_file argument - should result in error & usage output
python "$MSG_BOT"

# Reminder file name doesn't exist
python "$MSG_BOT" tests/reminders/nonexistent_file.json

# Send message in read-only channel
python "$MSG_BOT" tests/reminders/read_only_sample.json

# Send message in restricted channel
python "$MSG_BOT" tests/reminders/restricted_sample.json

# TODO: Define this behavior
# Given too many arguments - Behavior not yet defined
