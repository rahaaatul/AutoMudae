# config

Configuration management module for AutoMudae Discord Bot.

> [!INFO]
> This module provides a unified configuration system using OS-specific JSON files for storing bot credentials and user preferences. It supports cross-platform compatibility and provides a clean API for configuration management.

Features:
- OS-specific config directories (Windows/macOS/Linux)
- JSON-based storage for credentials and preferences
- Type-safe configuration access
- Automatic directory creation
- Error handling for file operations

Configuration files are stored in:
- Windows: %APPDATA%/automudae/
- macOS: ~/Library/Application Support/automudae/
- Linux: ~/.config/automudae/

## ConfigManager

Unified configuration manager for AutoMudae Discord bot.

Provides a centralized interface for managing bot credentials and user preferences
using OS-specific JSON file storage. Handles cross-platform compatibility and
provides error-resistant file operations.

Attributes:
    config_dir (Path): OS-specific configuration directory path

### __init__

Initialize the configuration manager.

Creates the configuration directory if it doesn't exist and sets up
the config_dir attribute for the current platform.

### _get_config_dir

Get the OS-specific configuration directory.

Returns:
    Path: Platform-appropriate configuration directory path

### _get_file_path

Get the file path for a specific configuration type.

Args:
    config_type: Name of the configuration file (without .json extension)

Returns:
    Path: Full path to the configuration file

### _load_json

Load configuration data from a JSON file.

Args:
    config_type: Name of the configuration file to load

Returns:
    Dict[str, Any]: Configuration data as a dictionary, or empty dict if file
                   doesn't exist or is invalid

### _save_json

Save configuration data to a JSON file.

Args:
    config_type: Name of the configuration file to save
    data: Configuration data to save

Raises:
    Exception: If the file cannot be written

### get_credentials

Get all bot credentials as a dictionary.

Returns:
    Dict[str, Any]: Dictionary containing all stored credentials

### set_credential

Set a bot credential value.

Args:
    key: Credential name (e.g., 'token', 'channel_id', 'server_id')
    value: Credential value to store

### get_credential

Get a specific bot credential value.

Args:
    key: Credential name to retrieve
    default: Default value if credential is not found

Returns:
    The credential value, or default if not found

### _load_preferences

Load preferences list from JSON file.

Args:
    preference_type: Type of preferences ('characters', 'series', 'kakeras')

Returns:
    List[str]: List of preference items, or empty list if file doesn't exist

### _save_preferences

Save preferences list to JSON file.

Args:
    preference_type: Type of preferences ('characters', 'series', 'kakeras')
    items: List of preference items to save

Raises:
    Exception: If the file cannot be written

### get_characters

Get the list of desired characters.

Returns:
    List[str]: List of character names the bot should prioritize

### add_character

Add a character to the desired characters list.

Args:
    character: Character name to add

Returns:
    bool: True if added successfully, False if already exists

### remove_character

Remove a character from the desired characters list.

Args:
    character: Character name to remove

Returns:
    bool: True if removed successfully, False if not found

### clear_characters

Clear all desired characters from the list.

### get_series

Get the list of desired series.

Returns:
    List[str]: List of series names the bot should prioritize

### add_series

Add a series to the desired series list.

Args:
    series: Series name to add

Returns:
    bool: True if added successfully, False if already exists

### remove_series

Remove a series from the desired series list.

Args:
    series: Series name to remove

Returns:
    bool: True if removed successfully, False if not found

### clear_series

Clear all desired series from the list.

### get_kakeras

Get the list of desired kakeras.

Returns:
    List[str]: List of kakera types the bot should prioritize

### add_kakera

Add a kakera type to the desired kakeras list.

Args:
    kakera: Kakera type to add (e.g., 'kakeraP', 'kakeraY')

Returns:
    bool: True if added successfully, False if already exists

### remove_kakera

Remove a kakera type from the desired kakeras list.

Args:
    kakera: Kakera type to remove

Returns:
    bool: True if removed successfully, False if not found

### clear_kakeras

Clear all desired kakeras from the list.
