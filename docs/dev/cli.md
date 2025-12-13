# cli

Command-line interface for AutoMudae Discord Bot.

> [!INFO]
> This module provides a comprehensive CLI tool for managing AutoMudae bot configuration and running automated Mudae character rolling, claiming, and kakera reactions.

The CLI supports:
- Bot credential management (Discord token, channel/server IDs)
- User preference management (desired characters, series, kakeras)
- Configuration reset commands for all setting types
- Immediate and scheduled bot execution
- Professional help system with setup guidance

Example usage:
    mudae config credentials set token "your_token"
    mudae config characters add "Ciri"
    mudae config kakeras reset  # Reset to defaults
    mudae run schedule 25

## get_version

Get version from installed package or pyproject.toml.

Returns:
    str: Version string, or "unknown" if not found.

## validate_credentials

Validate that all required Discord credentials are configured.

- Checks for the presence of essential bot credentials needed for Discord API access.
- If any credentials are missing, provides helpful setup instructions.

Returns:
    bool: True if all required credentials are present, False otherwise.

## main

Main entry point for the CLI application.

- Sets up the complete argument parser hierarchy with subcommands for config management.
- Supports configuration commands for credentials, characters, series, and kakeras.
- Includes reset functionality with confirmation prompts for destructive operations.
- Handles bot execution with validation and scheduling options.
- Supports graceful error handling with helpful messages for incomplete commands.

The CLI structure includes:
- `mudae config credentials` - Manage bot credentials
- `mudae config characters` - Manage desired characters
- `mudae config series` - Manage desired series
- `mudae config kakeras` - Manage desired kakeras
- `mudae run` - Execute the bot
