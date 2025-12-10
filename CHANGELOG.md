# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
