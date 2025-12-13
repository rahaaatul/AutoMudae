# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-12-14

### Highlights
- **Smarter Configuration**: Settings now persist automatically and work across Windows, macOS, and Linux.
  - No more losing settings after updates or reinstalls
  - Same setup works on any operating system
  - Credentials stored securely in system-standard locations
- **Priority Character Claiming**: Your favorite characters get claimed first, even over series preferences.
  - Exact character matches take precedence over series matches
  - Ensures you never miss your most wanted characters
  - Case-insensitive matching for better reliability
- **Better User Experience**: Professional command-line interface with helpful validation and clear instructions.
  - Automatic checking of credentials before running
  - Comprehensive help screens with examples
  - Clear error messages when something is misconfigured
  - Easy-to-use commands for managing all settings

### Added
- **Character Priority Claiming**: Exact character name matching now takes priority over series-based claiming. [`d42d400`](https://github.com/rahaaatul/automudae/commit/d42d400)
- **Case-Insensitive Matching**: Character and series name matching is now case-insensitive for better reliability. [`d42d400`](https://github.com/rahaaatul/automudae/commit/d42d400)
- **Unified JSON Configuration System**: All settings stored in OS-specific config directories using JSON files. [`fcf163b`](https://github.com/rahaaatul/automudae/commit/fcf163b)
- **Credentials Management**: New `mudae config credentials` commands for Discord bot configuration. [`adf8c2d`](https://github.com/rahaaatul/automudae/commit/adf8c2d)
- **Configuration Validation**: Automatic validation prevents runtime errors from missing credentials. [`adf8c2d`](https://github.com/rahaaatul/automudae/commit/adf8c2d)
- **Improved CLI Help System**: Clean, professional help screens with proper --help support. [`adf8c2d`](https://github.com/rahaaatul/automudae/commit/adf8c2d)
- **Cross-platform Support**: Automatic detection of config directories for Windows, macOS, and Linux. [`fcf163b`](https://github.com/rahaaatul/automudae/commit/fcf163b)
- **Default Kakeras Configuration**: Automatic default kakeras (`kakeraP`, `kakeraY`, `kakeraO`, `kakeraR`, `kakeraW`, `kakeraL`) when no custom kakeras are set. [`fcf163b`](https://github.com/rahaaatul/automudae/commit/fcf163b)
- **Reset Commands**: New reset commands for all configuration types to restore defaults or clear settings. [`adf8c2d`](https://github.com/rahaaatul/automudae/commit/adf8c2d)
- **Documentation**: Added comprehensive user and developer documentation in `/docs` folder. [`4c02af9`](https://github.com/rahaaatul/automudae/commit/4c02af9)

### Changed
- **Complete Configuration Migration**: All settings moved from `.env` to JSON files in OS-specific directories. [`fcf163b`](https://github.com/rahaaatul/automudae/commit/fcf163b)
- **Unified Config Module**: Merged `preferences.py` into `config.py` for cleaner architecture. [`fcf163b`](https://github.com/rahaaatul/automudae/commit/fcf163b)
- **CLI Command Structure**: Replaced `mudae env` with `mudae config credentials` for bot settings. [`adf8c2d`](https://github.com/rahaaatul/automudae/commit/adf8c2d)
- **Character Priority Logic**: Character matches now checked before series matches for higher priority claiming. [`d42d400`](https://github.com/rahaaatul/automudae/commit/d42d400)

### Removed
- Environment variable support for all settings (DESIRED_* variables and bot credentials). [`adf8c2d`](https://github.com/rahaaatul/automudae/commit/adf8c2d)
- `.env` file dependency for configuration. [`adf8c2d`](https://github.com/rahaaatul/automudae/commit/adf8c2d)

### Migration Guide
Users upgrading from 0.1.0 should:

**For Bot Credentials:**
```bash
# Old way (no longer supported)
mudae env set DISCORD_TOKEN "token"

# New way
mudae config credentials set token "token"
mudae config credentials set channel_id "channel_id"
mudae config credentials set server_id "server_id"
```

**For User Preferences:**
```bash
# Old way (no longer supported)
# DESIRED_CHARACTERS="Ciri,Luffy"

# New way
mudae config characters add "Ciri"
mudae config characters add "Luffy"
mudae config series add "The Witcher"
mudae config kakeras add "kakeraP"
```

**Benefits of New System:**
- **Persistent**: Settings survive reinstalls and system moves
- **Cross-platform**: Same experience on Windows, macOS, and Linux
- **Professional**: Clean CLI with validation and comprehensive help system
- **Organized**: Separate JSON files for different setting types
- **Secure**: Credentials stored in OS-specific secure locations

## [0.1.0] - 2025-12-11

### Added
- CLI interface with commands for running, scheduling, and environment management
- Package configuration with pyproject.toml
- Environment variable management for Discord credentials
- .gitignore file for Python project
- Support for respecting Mudae's "rolls left" warnings in card footers
- Immediate stopping when Mudae's hourly roll limit is reached

### Changed
- Updated README.md with new installation and usage instructions
- Refactored `Bot.py` into `cli.py` with comprehensive command-line interface, environment variable management, and flexible scheduling options
  - cli.py (137 lines) provides full CLI with environment variable management (set/get/remove), scheduling with custom minute specification, and immediate run option
  - Compared to Bot.py (11 lines) which was a simple scheduling script, cli.py offers significantly enhanced functionality and user control
- Refactored `Vars.py` into `config.py` with dotenv support, environment variable loading, and enhanced configuration handling with defaults
- Renamed `Function.py` to `roll.py` and updated import statement from `import Vars` to `import config as Vars`
- Optimized kakera reaction system to respect hierarchy order (L > W > R > O > Y > G > T > B > P) and check each button individually for desired types, ensuring efficient collection of mixed kakera
- Updated claimed emoji from '❤' to '❤️'
- Updated all variable names to follow Python naming conventions (snake_case)

### Removed
- Old script files (`Bot.py`, `Function.py`, `Vars.py`)

### Fixed
- IndexError when accessing message components for kakera reactions on cards without interactive buttons

## [0.0.0] - 2024-09-09

### Added

- Initial release of AutoMudae Discord bot
- Automated character rolling and claiming functionality
- Kakera reaction system for Mudae bot interactions
- Support for desired series and kakera preferences

### Changed
- Simplified kakera reaction process by sequentially reacting to available kakeras

### Fixed
- Improved error handling for message parsing and reactions
- Improved error handling for message parsing and reactions
