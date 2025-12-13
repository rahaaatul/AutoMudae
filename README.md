# AutoMudae

Claim waifus with and react to kakeras automatically.

## Installation

```bash
pip install automudae
```

### Setup

> [!NOTE]
> Need a Discord bot token and channel, server IDs to use this bot.

Set your Discord bot credentials:

```bash
mudae config credentials set token your_discord_token_here
mudae config credentials set channel_id your_channel_id_here
mudae config credentials set server_id your_server_id_here
```

> [!TIP]
> Credentials are stored securely in OS-specific config directories and persist across installations.

### Usage

> [!TIP]
> Can run with `mudae` or `automudae`

> [!IMPORTANT]
> - All bot commands run indefinitely.
> - Use `Ctrl+C` to stop them.

```bash
mudae                    # Show help screen
mudae run               # Run bot immediately once
mudae run schedule      # Run bot every hour at default time
mudae run schedule 25   # Run bot every hour at minute 25
```

---

## Todo

- [ ] **Optimized Kakera react**: The bot will use an algorithm to prioritize higher Kakera values without losing any efficiency
- [ ] **Optimized claiming**: In order to not losing the claim, it will get the max value card in case it doesn't match any desired series or cards
- [ ] **Optimized $dk use**: The bot will perfectly use and take into account the DK command to get even more effective kakera reactions
- [ ] **Optimized $rt use**: In case of not having an available claim, the Bot will use the $rt command to be able to claim
- [ ] **Optimized $daily use**: Use the daily command each time it is available
- [ ] **Optimized $rolls use**: Use the rolls command to get better claims or kakera reactions
- [ ] **Multi-Bot**: Add as many Discord Accounts as you want to do everything menctioned above to multiply your profits
- [x] **Desired Characters**: AutoClaim the exact characters when they appear with priority over all!
