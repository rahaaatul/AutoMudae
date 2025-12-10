"""
Configuration module for Automudae bot.

This module loads environment variables from a .env file and provides default
configurations for the Discord bot, including authentication tokens, channel
settings, roll commands, desired kakeras and series, poke roll preferences,
and repeat intervals.

Attributes:
    token (str): Discord bot token retrieved from environment variables.
    channel_id (str): Discord channel ID for bot operations.
    server_id (str): Discord server ID where the bot operates.
    roll_command (str): Command prefix for roll operations, defaults to "wa".
    desired_kakeras (list): List of desired kakera types to collect.
    desired_series (list): List of desired anime/manga series for rolls.
    poke_roll (bool): Whether to enable poke roll functionality.
    repeat_minute (str): Minute interval for repeat operations.
"""

from dotenv import load_dotenv
import os

# Load environment variables from .env file to configure the application
load_dotenv()

# Retrieve Discord bot authentication token from environment variables
# Falls back to empty string if not set
token = os.getenv("DISCORD_TOKEN", "")

# Retrieve the Discord channel ID where the bot will perform operations
# Falls back to empty string if not set
channel_id = os.getenv("CHANNEL_ID", "")

# Retrieve the Discord server ID for the bot's operational context
# Falls back to empty string if not set
server_id = os.getenv("SERVER_ID", "")

# Retrieve the command prefix used for roll operations
# Defaults to "wa" if not specified in environment variables
roll_command = os.getenv("ROLL_COMMAND", "wa")

# Retrieve desired kakera types as a comma-separated list and split into a list
# Defaults to a predefined set of kakera types if not specified
desired_kakeras = os.getenv(
    "DESIRED_KAKERAS", "kakeraP,kakeraY,kakeraO,kakeraR,kakeraW,kakeraL"
).split(",")

# Retrieve desired anime/manga series as a comma-separated list and split into a list
# Defaults to popular series if not specified
desired_series = os.getenv("DESIRED_SERIES", "One Piece,Dragon Ball Z,Death Note").split(
    ","
)

# Retrieve poke roll setting and convert to boolean
# Defaults to True if not specified or invalid
poke_roll = os.getenv("POKE_ROLL", "True").lower() == "true"

# Retrieve the minute interval for repeat operations as a string
# Defaults to "25" minutes if not specified
repeat_minute = os.getenv("REPEAT_MINUTE", "25")
