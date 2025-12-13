# Installation & Setup Guide

## Installation

Using `pip`:

```bash
pip install automudae
```

Using `pipx`:

```bash
pipx install automudae
```

> [!TIP]
> After installation, you can use either `mudae` or `automudae` commands - both work the same way.

## Initial Setup

### Discord Credentials

Set your Discord bot credentials using the unified config system:

```bash
mudae config credentials set token your_discord_token_here
mudae config credentials set channel_id your_channel_id_here
mudae config credentials set server_id your_server_id_here
```

> [!IMPORTANT]
> These credentials are required for the bot to function. The bot cannot run without them.

### Optional Settings

Configure additional bot settings:

```bash
mudae config credentials set roll_command "wa"        # Default roll command
mudae config credentials set poke_roll true           # Enable poke rolls
mudae config credentials set repeat_minute "25"       # Default schedule minute
```

### Preferences Configuration

Configure what characters, series, and kakeras you want to collect:

```bash
# Add desired characters (highest priority)
mudae config characters add "Ciri"
mudae config characters add "Luffy"
mudae config characters add "Goku"

# Add desired series (secondary priority)
mudae config series add "The Witcher"
mudae config series add "One Piece"
mudae config series add "Dragon Ball Z"

# Add desired kakeras (optional - defaults to most valuable types)
mudae config kakeras add "kakeraP"
mudae config kakeras add "kakeraY"
mudae config kakeras add "kakeraO"

# Or reset to defaults: kakeraP, kakeraY, kakeraO, kakeraR, kakeraW, kakeraL
mudae config kakeras reset
```

> [!TIP]
> If you don't configure any kakeras, the bot automatically uses the most valuable types by default.
