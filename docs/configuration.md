# Configuration Guide

## Preferences System

### Storage Location

Preferences are stored in OS-specific config directories:

- **Windows**: `%APPDATA%/automudae/`
- **macOS**: `~/Library/Application Support/automudae/`
- **Linux**: `~/.config/automudae/`

Files created:
- `characters.json` - Your desired characters
- `series.json` - Your desired series
- `kakeras.json` - Your desired kakeras

### Claiming Priority

The bot uses a 3-tier priority system:

1. **Character Priority** (Highest) - Case-insensitive character name matches
2. **Series Priority** (Medium) - Case-insensitive series name matches
3. **Power Priority** (Fallback) - Highest power cards when no matches

### Managing Preferences

#### Adding Preferences

```bash
# Add individual items
mudae config characters add "Naruto"
mudae config series add "Naruto"
mudae config kakeras add "kakeraR"
```

#### Listing Preferences

```bash
# List specific types
mudae config characters list
mudae config series list
mudae config kakeras list
```

#### Removing Preferences

```bash
# Remove individual items
mudae config characters remove "Naruto"
mudae config series remove "Naruto"
mudae config kakeras remove "kakeraR"
```

#### Clearing Preferences

```bash
# Clear all of a type
mudae config characters clear
mudae config series clear
mudae config kakeras clear
```

#### Resetting to Defaults

```bash
# Reset kakeras to default set (kakeraP, kakeraY, kakeraO, kakeraR, kakeraW, kakeraL)
mudae config kakeras reset

# Reset other preferences (clears them completely)
mudae config characters reset
mudae config series reset
mudae config credentials reset
```

> [!NOTE]
> Kakeras automatically default to the most valuable types (kakeraP, kakeraY, kakeraO, kakeraR, kakeraW, kakeraL) when no custom kakeras are configured. Other preferences have no defaults and will be empty when first used.

### Credentials Management

Manage all bot settings:

```bash
# Set credentials and settings
mudae config credentials set token "your_token"
mudae config credentials set channel_id "123456789"
mudae config credentials set server_id "987654321"
mudae config credentials set repeat_minute "30"
mudae config credentials set roll_command "wa"
mudae config credentials set poke_roll true

# View settings
mudae config credentials get repeat_minute
mudae config credentials list

# Remove settings
mudae config credentials remove repeat_minute
