# roll

Mudae character rolling and claiming module for AutoMudae Discord Bot.

> [!INFO]
> This module handles the core bot functionality for automated Mudae interactions:
> - Rolling for new characters using slash commands
> - Intelligent character claiming based on user preferences
> - Kakera reaction automation with priority hierarchy
> - Roll limit detection and graceful stopping

The bot implements a 3-tier claiming priority system:
1. Character Priority: Case-insensitive character name matches (highest priority)
2. Series Priority: Case-insensitive series name matches (medium priority)
3. Power Priority: Highest power cards when no matches (fallback)

Kakera reactions follow Mudae's hierarchy: `kakeral` > `kakeraw` > `kakerar` > `kakerao` > `kakeray` > `kakerag` > `kakerat` > `kakerab` > `kakerap`

## simpleRoll

Execute the main Mudae rolling and claiming loop.

This function implements the core bot logic:
1. Sends roll commands to Mudae bot
2. Parses character card information
3. Applies claiming priorities based on user preferences
4. Handles kakera reactions with proper hierarchy
5. Monitors roll limits and stops gracefully

The function runs continuously until:
- Roll limit is reached
- Too many failed rolls occur
- User interrupts with Ctrl+C
- No rolls left (based on footer warnings)
