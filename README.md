# AutoMudae

Run **Mudae** 24/7 without any human input. Automatically claims waifus/husbandos and reacts to kakeras every hour.

## Installation

```bash
pip install git+https://github.com/rahaaatul/automudae.git
```

> [!TIP]
> After installation, you can use either `mudae` or `automudae` commands - both work the same way.

### Setup

> [!NOTE]
> Need a Discord bot token and channel, server IDs to use this bot.

Set your Discord bot credentials:

```bash
mudae env set DISCORD_TOKEN your_token_here
mudae env set CHANNEL_ID your_channel_id_here
mudae env set SERVER_ID your_server_id_here
```

### Usage

> [!TIP]
> Can run with `mudae` or `automudae`

```bash
mudae
```

#### Schedule Runs

> [!NOTE]
> Runs once immediately, then every hour at the default time.

```bash
mudae schedule 25    # Wait for 25 min past hour, then run every hour
mudae schedule       # Use saved default time, then run every hour
```

> [!IMPORTANT]
> - All bot commands run indefinitely. 
> - Use `Ctrl+C` to stop them.

#### Environment Management

##### Change default schedule time

```bash
mudae env set REPEAT_MINUTE 30
```

##### View current settings

```
mudae env get REPEAT_MINUTE       
```

---

## Todo

- [ ] **Desired Characters**: AutoClaim the exact characters when they appear with priority over all!
- [ ] **Optimized Kakera react**: The bot will use an algorithm to prioritize higher Kakera values without losing any efficiency
- [ ] **Optimized claiming**: In order to not losing the claim, it will get the max value card in case it doesn't match any desired series or cards
- [ ] **Optimized $dk use**: The bot will perfectly use and take into account the DK command to get even more effective kakera reactions
- [ ] **Optimized $rt use**: In case of not having an available claim, the Bot will use the $rt command to be able to claim
- [ ] **Optimized $daily use**: Use the daily command each time it is available
- [ ] **Optimized $rolls use**: Use the rolls command to get better claims or kakera reactions
- [ ] **Multi-Bot**: Add as many Discord Accounts as you want to do everything menctioned above to multiply your profits
