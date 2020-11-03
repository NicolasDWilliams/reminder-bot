#!/usr/bin/env bash
# Test message_bot.py with errors that should result in logout
MSG_BOT="../message_bot.py"

# TODO: Create command that will timeout in case it hangs

# Run without reminder_file argument - should result in error & usage output
# python "$MSG_BOT"

# # Reminder file name doesn't exist
# python "$MSG_BOT" tests/reminders/nonexistent_file.json

# # Reminder file can't be parsed
# python "$MSG_BOT" reminders/parse_failure_sample.json

# Reminder json file is missing a required key
# python "$MSG_BOT" reminders/missing_required_key_sample.json

# Server doesn't exist
# python "$MSG_BOT" reminders/wrong_server_sample.json

# # Channel doesn't exist
# python "$MSG_BOT" reminders/nonexistent_channel_sample.json

# Send message in read-only channel
# python "$MSG_BOT" tests/reminders/read_only_sample.json

# # Send message in restricted channel
# python "$MSG_BOT" tests/reminders/restricted_sample.json

# TODO: Define this behavior
# Given too many arguments - Behavior not yet defined
