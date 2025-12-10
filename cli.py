import config
import time
import schedule
import argparse
import os
import sys
from roll import simpleRoll

"""Command-line interface for Automudae Discord Bot.

This module provides a CLI tool to manage environment variables and schedule
the bot's operations.
"""

def manage_env(action, key, value=None):
    """Manages environment variables in the .env file.

    This function allows setting, getting, and removing environment variables
    stored in a .env file in the current directory.

    Args:
        action (str): The action to perform. Must be 'set', 'get', or 'remove'.
        key (str): The environment variable key.
        value (str, optional): The value to set for the key. Required if action is 'set'.

    Returns:
        None: This function prints the result and modifies the .env file.
    """
    env_file = '.env'

    # Read current .env file
    env_vars = {}
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        k, v = line.split('=', 1)
                        env_vars[k] = v

    if action == 'set':
        if value is None:
            print(f"Error: Value required for setting {key}")
            return
        env_vars[key] = value
        print(f"Set {key}={value}")
    elif action == 'remove':
        if key in env_vars:
            del env_vars[key]
            print(f"Removed {key}")
        else:
            print(f"Key {key} not found")
    elif action == 'get':
        if key in env_vars:
            print(f"{key}={env_vars[key]}")
        else:
            print(f"Key {key} not found")

    # Write back to .env file
    with open(env_file, 'w') as f:
        for k, v in env_vars.items():
            f.write(f"{k}={v}\n")

def main():
    """Main entry point for the CLI application.

    Parses command-line arguments and executes the appropriate actions for
    environment variable management or bot scheduling.
    """

    parser = argparse.ArgumentParser(description='Automudae Discord Bot')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Env management subcommand
    env_parser = subparsers.add_parser('env', help='Manage environment variables')
    env_subparsers = env_parser.add_subparsers(dest='env_action', help='Environment actions')

    # Set env var
    set_parser = env_subparsers.add_parser('set', help='Set environment variable')
    set_parser.add_argument('key', choices=['DISCORD_TOKEN', 'CHANNEL_ID', 'SERVER_ID', 'REPEAT_MINUTE'], help='Environment variable key')
    set_parser.add_argument('value', help='Environment variable value')

    # Remove env var
    remove_parser = env_subparsers.add_parser('remove', help='Remove environment variable')
    remove_parser.add_argument('key', choices=['DISCORD_TOKEN', 'CHANNEL_ID', 'SERVER_ID', 'REPEAT_MINUTE'], help='Environment variable key')

    # Get env var
    get_parser = env_subparsers.add_parser('get', help='Get environment variable')
    get_parser.add_argument('key', choices=['DISCORD_TOKEN', 'CHANNEL_ID', 'SERVER_ID', 'REPEAT_MINUTE'], help='Environment variable key')

    # Schedule bot
    schedule_parser = subparsers.add_parser('schedule', help='Schedule the bot to run every hour at specified minute (uses current setting if not provided)')
    schedule_parser.add_argument('minute', type=int, nargs='?', choices=range(0, 60), help='Minute of the hour to run (0-59). If not provided, uses current REPEAT_MINUTE setting.')

    # Run bot (default behavior) - parser not needed since we check for 'run' or None

    args = parser.parse_args()

    if args.command == 'env':
        if args.env_action == 'set':
            manage_env('set', args.key, args.value)
        elif args.env_action == 'remove':
            manage_env('remove', args.key)
        elif args.env_action == 'get':
            manage_env('get', args.key)
    elif args.command == 'schedule':
        # Set the schedule minute for this session
        if args.minute is not None:
            # Use the provided minute for this session only (don't save to env)
            minute_str = f"{args.minute:02d}"
            print(f"Scheduled to run every hour at {args.minute} minutes past the hour (this session only)")
            time_string = ':' + minute_str
        else:
            # Use the saved setting
            print(f"Scheduled to run every hour at {config.repeat_minute} minutes past the hour (using saved setting)")
            time_string = ':' + config.repeat_minute

        # Wait for the scheduled time to run
        schedule.every().hour.at(time_string).do(simpleRoll)

        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nBot stopped by user.")
            sys.exit(0)
    elif args.command is None:
        # Default behavior - run immediately once
        print("Running immediately...")
        simpleRoll()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
