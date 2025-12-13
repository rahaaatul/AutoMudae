import config
import time
import schedule
import argparse
import sys
from roll import simpleRoll
import pathlib
import importlib.metadata


def get_version():
    """Get version from installed package or pyproject.toml"""
    try:
        # Try to get version from installed package metadata
        return importlib.metadata.version("AutoMudae")
    except importlib.metadata.PackageNotFoundError:
        # Fallback to reading from pyproject.toml (development mode)
        pyproject_path = pathlib.Path(__file__).parent / "pyproject.toml"
        try:
            with open(pyproject_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.strip().startswith("version = "):
                        # Extract version from "version = "0.2.0""
                        return line.split('"')[1]
        except Exception:
            pass
    return "unknown"


def validate_credentials():
    required = ["token", "channel_id", "server_id"]
    missing = []

    # Check each required credential
    for cred in required:
        if not config.config_manager.get_credential(cred):
            missing.append(cred)

    # Display error message with setup instructions if credentials are missing
    if missing:
        print("❌ Missing required credentials:")
        for cred in missing:
            print(f"   - {cred}")
        print("\n💡 Set them with:")
        print('   mudae config credentials set token "your_discord_token"')
        print('   mudae config credentials set channel_id "your_channel_id"')
        print('   mudae config credentials set server_id "your_server_id"')
        return False
    return True


def main():
    # Create main argument parser
    parser = argparse.ArgumentParser(
        description="Automudae Discord Bot", add_help=False
    )
    parser.add_argument(
        "-h", "-?", "--help", action="help", help="Show this help message and exit"
    )
    parser.add_argument("-v", "--version", action="version", version=get_version())
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Configuration management subcommand group
    config_parser = subparsers.add_parser(
        "config", help="Manage bot configuration", add_help=False
    )
    config_parser.add_argument(
        "-h", "-?", "--help", action="help", help="Show this help message and exit"
    )
    config_subparsers = config_parser.add_subparsers(
        dest="config_type", help="Configuration type", required=False
    )

    # Bot credentials management subcommand
    credentials_parser = config_subparsers.add_parser(
        "credentials", help="Manage bot credentials", add_help=False
    )
    credentials_parser.add_argument(
        "-h", "-?", "--help", action="help", help="Show this help message and exit"
    )
    credentials_subparsers = credentials_parser.add_subparsers(
        dest="action", help="Credentials actions", required=False
    )

    # Set credential
    set_cred_parser = credentials_subparsers.add_parser("set", help="Set a credential")
    set_cred_parser.add_argument(
        "key",
        choices=[
            "token",
            "channel_id",
            "server_id",
            "roll_command",
            "poke_roll",
            "repeat_minute",
        ],
        help="Credential key",
    )
    set_cred_parser.add_argument("value", help="Credential value")

    # Get credential
    get_cred_parser = credentials_subparsers.add_parser("get", help="Get a credential")
    get_cred_parser.add_argument(
        "key",
        choices=[
            "token",
            "channel_id",
            "server_id",
            "roll_command",
            "poke_roll",
            "repeat_minute",
        ],
        help="Credential key",
    )

    # Remove credential
    remove_cred_parser = credentials_subparsers.add_parser(
        "remove", help="Remove a credential"
    )
    remove_cred_parser.add_argument(
        "key",
        choices=[
            "token",
            "channel_id",
            "server_id",
            "roll_command",
            "poke_roll",
            "repeat_minute",
        ],
        help="Credential key",
    )

    # List credentials
    credentials_subparsers.add_parser("list", help="List all credentials")

    # Characters subcommand
    characters_parser = config_subparsers.add_parser(
        "characters", help="Manage desired characters", add_help=False
    )
    characters_parser.add_argument(
        "-h", "-?", "--help", action="help", help="Show this help message and exit"
    )
    characters_subparsers = characters_parser.add_subparsers(
        dest="action", help="Character actions", required=True
    )

    # Add character
    add_char_parser = characters_subparsers.add_parser(
        "add", help="Add a desired character"
    )
    add_char_parser.add_argument("character", help="Character name")

    # Remove character
    remove_char_parser = characters_subparsers.add_parser(
        "remove", help="Remove a desired character"
    )
    remove_char_parser.add_argument("character", help="Character name")

    # List characters
    characters_subparsers.add_parser("list", help="List desired characters")

    # Clear characters
    characters_subparsers.add_parser("clear", help="Clear all desired characters")

    # Reset characters
    characters_subparsers.add_parser(
        "reset", help="Reset characters to defaults (clear)"
    )

    # Series subcommand
    series_parser = config_subparsers.add_parser(
        "series", help="Manage desired series", add_help=False
    )
    series_parser.add_argument(
        "-h", "-?", "--help", action="help", help="Show this help message and exit"
    )
    series_subparsers = series_parser.add_subparsers(
        dest="action", help="Series actions", required=True
    )

    # Add series
    add_series_parser = series_subparsers.add_parser("add", help="Add a desired series")
    add_series_parser.add_argument("series", help="Series name")

    # Remove series
    remove_series_parser = series_subparsers.add_parser(
        "remove", help="Remove a desired series"
    )
    remove_series_parser.add_argument("series", help="Series name")

    # List series
    series_subparsers.add_parser("list", help="List desired series")

    # Clear series
    series_subparsers.add_parser("clear", help="Clear all desired series")

    # Reset series
    series_subparsers.add_parser("reset", help="Reset series to defaults (clear)")

    # Kakeras subcommand
    kakeras_parser = config_subparsers.add_parser(
        "kakeras", help="Manage desired kakeras", add_help=False
    )
    kakeras_parser.add_argument(
        "-h", "-?", "--help", action="help", help="Show this help message and exit"
    )
    kakeras_subparsers = kakeras_parser.add_subparsers(
        dest="action", help="Kakera actions", required=True
    )

    # Add kakera
    add_kakera_parser = kakeras_subparsers.add_parser(
        "add", help="Add a desired kakera"
    )
    add_kakera_parser.add_argument("kakera", help="Kakera type")

    # Remove kakera
    remove_kakera_parser = kakeras_subparsers.add_parser(
        "remove", help="Remove a desired kakera"
    )
    remove_kakera_parser.add_argument("kakera", help="Kakera type")

    # List kakeras
    kakeras_subparsers.add_parser("list", help="List desired kakeras")

    # Clear kakeras
    kakeras_subparsers.add_parser("clear", help="Clear all desired kakeras")

    # Reset kakeras
    kakeras_subparsers.add_parser("reset", help="Reset kakeras to defaults")

    # Run subcommand
    run_parser = subparsers.add_parser("run", help="Run the bot", add_help=False)
    run_parser.add_argument(
        "-h", "-?", "--help", action="help", help="Show this help message and exit"
    )
    run_parser.add_argument(
        "schedule", nargs="?", choices=["schedule"], help="Run in scheduled mode"
    )
    run_parser.add_argument(
        "minute",
        type=int,
        nargs="?",
        choices=range(0, 60),
        help="Minute of the hour to run (0-59)",
    )

    args = parser.parse_args()

    # Show help if no command provided
    if args.command is None:
        parser.print_help()
        return

    # Handle config commands
    if args.command == "config":
        if args.config_type is None:
            config_parser.print_help()
            return
        elif args.config_type == "credentials":
            if args.action is None:
                credentials_parser.print_help()
                return
            elif args.action == "set":
                # Convert string values to appropriate types
                if args.key in ["poke_roll"]:
                    value = args.value.lower() == "true"
                elif args.key in ["repeat_minute"]:
                    value = str(args.value)
                else:
                    value = args.value
                config.config_manager.set_credential(args.key, value)
                print(f"Set {args.key} = {value}")
            elif args.action == "get":
                value = config.config_manager.get_credential(args.key)
                if value is not None:
                    print(f"{args.key} = {value}")
                else:
                    print(f"{args.key} not set")
            elif args.action == "remove":
                credentials = config.config_manager.get_credentials()
                if args.key in credentials:
                    del credentials[args.key]
                    config.config_manager._save_json("credentials", credentials)
                    print(f"Removed {args.key}")
                else:
                    print(f"{args.key} not found")
            elif args.action == "list":
                credentials = config.config_manager.get_credentials()
                if credentials:
                    print("Credentials:")
                    for key, value in credentials.items():
                        print(f"  {key} = {value}")
                else:
                    print("No credentials set")
            elif args.action == "reset":
                # Confirm before resetting credentials
                response = (
                    input("⚠️  This will clear ALL credentials. Are you sure? (y/N): ")
                    .strip()
                    .lower()
                )
                if response == "y" or response == "yes":
                    config.config_manager.reset_credentials()
                    print("Reset all credentials")
                else:
                    print("Reset cancelled")

        elif args.config_type == "characters":
            if args.action == "add":
                if config.config_manager.add_character(args.character):
                    print(f"Added character: {args.character}")
                else:
                    print(f"Character already exists: {args.character}")
            elif args.action == "remove":
                if config.config_manager.remove_character(args.character):
                    print(f"Removed character: {args.character}")
                else:
                    print(f"Character not found: {args.character}")
            elif args.action == "list":
                characters = config.config_manager.get_characters()
                print("Desired Characters:")
                for char in characters:
                    print(f"  - {char}")
                if not characters:
                    print("  (none)")
            elif args.action == "clear":
                config.config_manager.clear_characters()
                print("Cleared all desired characters")
            elif args.action == "reset":
                # Confirm before resetting characters
                response = (
                    input("⚠️  This will clear ALL characters. Are you sure? (y/N): ")
                    .strip()
                    .lower()
                )
                if response == "y" or response == "yes":
                    config.config_manager.reset_characters()
                    print("Reset all characters")
                else:
                    print("Reset cancelled")

        elif args.config_type == "series":
            if args.action == "add":
                if config.config_manager.add_series(args.series):
                    print(f"Added series: {args.series}")
                else:
                    print(f"Series already exists: {args.series}")
            elif args.action == "remove":
                if config.config_manager.remove_series(args.series):
                    print(f"Removed series: {args.series}")
                else:
                    print(f"Series not found: {args.series}")
            elif args.action == "list":
                series = config.config_manager.get_series()
                print("Desired Series:")
                for s in series:
                    print(f"  - {s}")
                if not series:
                    print("  (none)")
            elif args.action == "clear":
                config.config_manager.clear_series()
                print("Cleared all desired series")
            elif args.action == "reset":
                # Confirm before resetting series
                response = (
                    input("⚠️  This will clear ALL series. Are you sure? (y/N): ")
                    .strip()
                    .lower()
                )
                if response == "y" or response == "yes":
                    config.config_manager.reset_series()
                    print("Reset all series")
                else:
                    print("Reset cancelled")

        elif args.config_type == "kakeras":
            if args.action == "add":
                if config.config_manager.add_kakera(args.kakera):
                    print(f"Added kakera: {args.kakera}")
                else:
                    print(f"Kakera already exists: {args.kakera}")
            elif args.action == "remove":
                if config.config_manager.remove_kakera(args.kakera):
                    print(f"Removed kakera: {args.kakera}")
                else:
                    print(f"Kakera not found: {args.kakera}")
            elif args.action == "list":
                kakeras = config.config_manager.get_kakeras()
                print("Desired Kakeras:")
                for k in kakeras:
                    print(f"  - {k}")
                if not kakeras:
                    print("  (none)")
            elif args.action == "clear":
                config.config_manager.clear_kakeras()
                print("Cleared all desired kakeras")
            elif args.action == "reset":
                # Reset kakeras to defaults (no confirmation needed)
                config.config_manager.reset_kakeras()
                print("Reset kakeras to defaults")

    # Handle run commands
    elif args.command == "run":
        # Validate credentials before running
        if not validate_credentials():
            sys.exit(1)

        if args.schedule == "schedule":
            # Scheduled run
            if args.minute is not None:
                minute_str = f"{args.minute:02d}"
                print(
                    f"Scheduled to run every hour at {args.minute} minutes past the hour"
                )
                time_string = ":" + minute_str
            else:
                print(
                    f"Scheduled to run every hour at {config.repeat_minute} minutes past the hour"
                )
                time_string = ":" + config.repeat_minute

            # Wait for the scheduled time to run
            schedule.every().hour.at(time_string).do(simpleRoll)

            try:
                while True:
                    schedule.run_pending()
                    time.sleep(1)
            except KeyboardInterrupt:
                print("\nBot stopped by user.")
                sys.exit(0)
        else:
            # Immediate run
            print("Running immediately...")
            simpleRoll()


if __name__ == "__main__":
    main()
