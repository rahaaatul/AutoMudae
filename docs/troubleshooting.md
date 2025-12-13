# Troubleshooting Guide

## Bot Not Claiming Characters

1. **Check your preferences are set:**
   ```bash
   mudae config characters list
   mudae config series list
   ```

2. **Verify character/series names match:**
   - Case-insensitive matching is supported
   - Check for typos in character/series names
   - Ensure you're using the exact names as they appear in Mudae

3. **Check bot permissions:**
   - Bot must have proper permissions in the Discord channel
   - Ensure the bot can send messages and reactions

## Preferences Not Saving

1. **Check write permissions:**
   - Ensure you have write permissions to the config directory

2. **Verify config directory exists:**
   - **Windows**: `%APPDATA%/automudae/`
   - **macOS**: `~/Library/Application Support/automudae/`
   - **Linux**: `~/.config/automudae/`

3. **Check available disk space:**
   - Ensure there's sufficient disk space for configuration files

## Bot Won't Start

1. **Verify required credentials:**
   ```bash
   mudae config credentials list
   ```
   Should show: `token`, `channel_id`, `server_id`

2. **Check Discord bot token validity:**
   - Ensure your Discord bot token is correct and active
   - Verify the bot is invited to your server

3. **Check channel and server IDs:**
   - Ensure the channel ID and server ID are correct
   - Verify the bot has access to the specified channel

## Roll Limits

The bot automatically stops when Mudae's hourly roll limit is reached. This is normal behavior:

- Wait for the next hour to continue rolling
- The bot will display "⚠️ Roll limit reached" when this happens
- Scheduled runs will resume automatically at the next hour

## Connection Issues

1. **Check internet connection:**
   - Ensure stable internet connection
   - Discord API may be temporarily unavailable

2. **Verify Mudae bot status:**
   - Check if Mudae bot is online

## Command Errors

1. **Use help for correct syntax:**
   ```bash
   mudae --help
   mudae config --help
   mudae config characters --help
   ```

2. **Check for typos:**
   - Command names are case-sensitive
   - Ensure proper spacing and quotes

## Performance Issues

1. **Check system resources:**
   - Ensure sufficient CPU and memory
   - Close other resource-intensive applications

2. **Reduce roll frequency:**
   - Consider using longer intervals between rolls
   - Monitor your system's performance

## Getting Help

If you continue to experience issues:

1. **Check the logs:** Look for error messages in the console output
2. **Verify configuration:** Double-check all settings with list commands
3. **Test incrementally:** Start with basic commands before complex operations

For additional support, visit the [GitHub repository](https://github.com/rahaaatul/automudae).
