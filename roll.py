import discum
import json
import re
import time
import requests
import config
from discum.utils.slash import SlashCommander

bot_id = "432610292342587392"
auth = {"authorization": config.token}
bot = discum.Client(token=config.token, log=False)
url = f"https://discord.com/api/v8/channels/{config.channel_id}/messages"


def simpleRoll():
    print(time.strftime("Rolling at %H:%M - %d/%m/%y", time.localtime()))
    roll_count = 1
    failed_rolls = 0
    rolls_left = 999  # High number to allow unlimited rolls by default
    claimed = "❤️"
    unclaimed = "🤍"
    kakera = "💎"
    emoji = "👍"
    roll_command = SlashCommander(bot.getSlashCommands(bot_id).json()).get(
        [config.roll_command]
    )
    continue_rolling = True

    try:
        while (continue_rolling or failed_rolls < 4) and rolls_left > 0:
            bot.triggerSlashCommand(bot_id, config.channel_id, config.server_id, data=roll_command)
            time.sleep(1.8)
            r = requests.get(url, headers=auth)
            jsonCard = json.loads(r.text)

            if len(jsonCard[0]["content"]) != 0:
                # Check for roll limit message
                if "roulette is limited" in jsonCard[0]["content"].lower():
                    print("⚠️ Roll limit reached - stopping immediately")
                    break
                failed_rolls += 1
                continue_rolling = False
                continue
            message_id = jsonCard[0]["id"]
            card_name = "null"
            card_series = "null"
            card_power = 0
            try:
                card_name = jsonCard[0]["embeds"][0]["author"]["name"]
                card_series = (
                    (jsonCard[0]["embeds"][0]["description"])
                    .replace("\n", "**")
                    .split("**")[0]
                )
                card_power = int((jsonCard[0]["embeds"][0]["description"]).split("**")[1])
            except IndexError:
                pass
            except KeyError:
                pass
            except ValueError:
                pass

            # Check footer for rolls left warning
            if "embeds" in jsonCard[0] and len(jsonCard[0]["embeds"]) > 0 and "footer" in jsonCard[0]["embeds"][0]:
                footer_text = jsonCard[0]["embeds"][0]["footer"].get("text", "")
                if "ROLLS LEFT" in footer_text:
                    match = re.search(r'(\d+)\s+ROLLS LEFT', footer_text)
                    if match:
                        rolls_left = int(match.group(1))
                        print(f"⚠️ {rolls_left} rolls left")

            if (
                "footer" not in jsonCard[0]["embeds"][0]
                or "icon_url" not in jsonCard[0]["embeds"][0]["footer"]
            ):
                print(
                    roll_count,
                    " - " + unclaimed + " ---- ",
                    card_power,
                    " - " + card_name + " - " + card_series,
                )
                if card_series in config.desired_series:
                    print("Trying to Claim " + card_name)
                    r = requests.put(
                        f"https://discord.com/api/v8/channels/{config.channel_id}/messages/{message_id}/reactions/{emoji}/%40me",
                        headers=auth,
                    )
            else:
                print(
                    roll_count,
                    " - " + claimed + " ---- ",
                    card_power,
                    " - " + card_name + " - " + card_series,
                )

            # Check if components exist for kakera reactions
            if (
                "components" in jsonCard[0]
                and len(jsonCard[0]["components"]) > 0
                and "components" in jsonCard[0]["components"][0]
                and len(jsonCard[0]["components"][0]["components"]) > 0
            ):
                try:
                    components = jsonCard[0]["components"][0]["components"]
                    hierarchy = ['kakeral', 'kakeraw', 'kakerar', 'kakerao', 'kakeray', 'kakerag', 'kakerat', 'kakerab', 'kakerap']
                    desired_buttons = []
                    for index, comp in enumerate(components):
                        try:
                            emoji_name = comp['emoji']['name'].lower()
                            if emoji_name in [d.lower() for d in config.desired_kakeras]:
                                h_index = hierarchy.index(emoji_name) if emoji_name in hierarchy else len(hierarchy)
                                desired_buttons.append((h_index, index, emoji_name))
                        except KeyError:
                            pass
                    if desired_buttons:
                        failed_rolls -= 1
                    desired_buttons.sort(key=lambda x: (x[0], x[1]))
                    for h_index, index, emoji_name in desired_buttons:
                        print(
                            kakera
                            + " - "
                            + kakera
                            + " - Trying to react to "
                            + emoji_name
                            + " of "
                            + card_name
                        )
                        bot.click(
                            jsonCard[0]["author"]["id"],
                            channelID=jsonCard[0]["channel_id"],
                            guildID=config.server_id,
                            messageID=jsonCard[0]["id"],
                            messageFlags=jsonCard[0]["flags"],
                            data={
                                "component_type": 2,
                                "custom_id": components[index]["custom_id"],
                            },
                        )
                        time.sleep(0.5)
                except (IndexError, KeyError):
                    pass  # Skip kakera reactions if structure is unexpected

            roll_count += 1
    except KeyboardInterrupt:
        print("\nRolling stopped by user.")
        return
    print("Rolling ended")

    if config.poke_roll:
        print("\nTrying to roll Pokeslot")
        requests.post(url=url, headers=auth, data={"content": "$p"})
