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

- [ ] **Library migration**: Migrate from outdated discum library to [`discord.py-self`](https://github.com/dolfies/discord.py-self) for better reliability and roll logging [`#21`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/21)
- [ ] **Public wish card reading**: Fix inability to read and process cards with public wishes/mentions above them [`#35`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/35)
- [ ] **Optimized Kakera react**: The bot will use an algorithm to prioritize higher Kakera values without losing any efficiency
- [ ] **Optimized claiming**: In order to not losing the claim, it will get the max value card in case it doesn't match any desired series or cards
- [ ] **Optimized $dk use**: The bot will perfectly use and take into account the DK command to get even more effective kakera reactions [`#3`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/3)
- [ ] **Optimized $rt use**: In case of not having an available claim, the Bot will use the $rt command to be able to claim
- [ ] **Optimized $daily use**: Use the daily command each time it is available, check for green emoji reaction to determine if bonus rolls are available, and execute $wa/$rolls/$wa sequence accordingly [`#3`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/3)
- [ ] **Optimized $rolls use**: Use the rolls command to get better claims or kakera reactions [`#3`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/3)
- [ ] **Kakera threshold claiming**: Add function to claim characters equal to or above a specified kakera amount [`#5`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/5)
- [ ] **Claim by ranking/importance**: Prioritize wishlist and claim by character ranking/importance [`#36`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/36)
- [ ] **Character-specific checking**: Check for specific characters instead of just series [`#36`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/36)
- [ ] **Highest value fallback toggle**: Option to claim highest value character if no desired characters are found [`#36`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/36)
- [ ] **Last claimed character tracking**: Input responsive system for saving and tracking last claimed character [`#36`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/36)
- [ ] **Multi-Bot**: Add as many Discord Accounts as you want to do everything menctioned above to multiply your profits [`#3`](https://github.com/GuilleDiazFentanes/AutoClaim-AutoRoll-AutoReact-MudaeBot-2025/issues/3)
- [x] **Desired Characters**: AutoClaim the exact characters when they appear with priority over all!
