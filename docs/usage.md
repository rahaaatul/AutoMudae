## Help Screen

Show the main help screen:

```bash
mudae
```

## Immediate Run

Run the bot once immediately:

```bash
mudae run
```

or

```bash
automudae run
```

## Scheduled Runs

Run every hour at a specific minute:

```bash
# Run at 25 minutes past each hour
mudae run schedule 25

# Use saved default time
mudae run schedule
```

> [!IMPORTANT]
> - All bot commands run indefinitely.
> - Use `Ctrl+C` to stop them.
> - The bot will automatically stop when Mudae's hourly roll limit is reached.

## Configuration Commands

### Managing Preferences

```bash
# Characters
mudae config characters add "Character Name"
mudae config characters remove "Character Name"
mudae config characters list
mudae config characters clear
mudae config characters reset  # Clear all (with confirmation)

# Series
mudae config series add "Series Name"
mudae config series remove "Series Name"
mudae config series list
mudae config series clear
mudae config series reset  # Clear all (with confirmation)

# Kakeras
mudae config kakeras add "kakeraP"
mudae config kakeras remove "kakeraP"
mudae config kakeras list
mudae config kakeras clear
mudae config kakeras reset  # Reset to defaults
```

### Managing Credentials

```bash
mudae config credentials set token "your_token"
mudae config credentials set channel_id "123456"
mudae config credentials set server_id "789012"
mudae config credentials list
mudae config credentials reset  # Clear all (with confirmation)
```
