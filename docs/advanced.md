# Advanced Usage Guide

## Custom Roll Commands

You can modify the roll command to use different Mudae commands:

```bash
# Default waifu command
mudae config credentials set roll_command "wa"

# Other available commands
mudae config credentials set roll_command "ha"  # Husbando
mudae config credentials set roll_command "ma"  # Mixed (both waifu and husbando)
```

## Poke Rolls

The bot automatically attempts poke rolls after each rolling session if enabled (default: enabled).

### Enable Poke Rolls
```bash
mudae config credentials set poke_roll true
```

### Disable Poke Rolls
```bash
mudae config credentials set poke_roll false
```

### What are Poke Rolls?
Poke rolls (`$p`) are special Mudae rolls that can give bonus rolls or other rewards. The bot will automatically attempt these after completing a normal rolling session.

## Advanced Configuration

### Custom Schedule Times

Set specific minutes for scheduled runs:

```bash
# Run at 15 minutes past each hour
mudae config credentials set repeat_minute "15"

# Run at 45 minutes past each hour
mudae config credentials set repeat_minute "45"
```

### Batch Preference Management

For power users managing many preferences:

```bash
# Add multiple characters at once (requires multiple commands)
mudae config characters add "Character 1"
mudae config characters add "Character 2"
mudae config characters add "Character 3"

# Clear and rebuild series list
mudae config series clear
mudae config series add "New Series 1"
mudae config series add "New Series 2"
```

## Understanding Bot Behavior

### Priority System Details

The bot uses a sophisticated 3-tier claiming system:

1. **Character Priority** (Highest)
   - Exact character name matches (case-insensitive)
   - Example: If "Ciri" is in your character list, the bot will claim any card named "Ciri"

2. **Series Priority** (Medium)
   - Series name matches (case-insensitive)
   - Example: If "The Witcher" is in your series list, the bot will claim cards from that series

3. **Power Priority** (Fallback)
   - When no character or series matches are found
   - The bot will claim the highest power card available

### Kakera Hierarchy

Kakera reactions follow Mudae's value hierarchy (highest to lowest):

- **kakeral** (Light) - Highest value
- **kakeraw** (Rainbow)
- **kakerar** (Red)
- **kakerao** (Orange)
- **kakeray** (Yellow)
- **kakerag** (Green)
- **kakerat** (Teal)
- **kakerab** (Blue)
- **kakerap** (Purple) - Lowest value

The bot will prioritize reacting to higher-value kakeras first.

## Security Considerations

### Credential Storage

- Credentials are stored securely in OS-specific directories
- Files are created with appropriate permissions
- No sensitive data is transmitted except to Discord's official API
