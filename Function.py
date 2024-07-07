import json
import time

import discum
import requests
from discum.utils.slash import SlashCommander

import Vars
from libs import utils

botID = "432610292342587392"
auth = {"authorization": Vars.token}
bot = discum.Client(token=Vars.token, log=False)
url = f"https://discord.com/api/v8/channels/{Vars.channelId}/messages"


def simpleRoll():
    print(time.strftime("Rolling at %H:%M - %d/%m/%y", time.localtime()))
    i = 1
    claimed = "❤️"
    unclaimed = "🤍"
    rollCommand = SlashCommander(bot.getSlashCommands(botID).json()).get([Vars.rollCommand])
    continueRolling = True

    while continueRolling is True:
        bot.triggerSlashCommand(botID, Vars.channelId, Vars.serverId, data=rollCommand)
        time.sleep(1)
        r = requests.get(url, headers=auth)
        jsonCard = json.loads(r.text)
        idMessage = jsonCard[0]["id"]

        if len(jsonCard[0]["content"]) != 0:
            continueRolling = False
            break

        try:
            cardName = jsonCard[0]["embeds"][0]["author"]["name"]
        except Exception as e:
            print(f"Error: {e}")
            cardName = "null"
        try:
            cardSeries = (jsonCard[0]["embeds"][0]["description"]).replace("\n", "**").split("**")[0]
        except Exception as e:
            print(f"Error: {e}")
            cardName = "null"
        try:
            cardPower = int((jsonCard[0]["embeds"][0]["description"]).split("**")[1])
        except Exception as e:
            print(f"Error: {e}")
            cardPower = 0

        if "footer" not in jsonCard[0]["embeds"][0] or "icon_url" not in jsonCard[0]["embeds"][0]["footer"]:
            print(f"{i:02} - {unclaimed} --- {cardPower} - {cardName} - {cardSeries}")
            if cardSeries in Vars.desiredSeries:
                print("Trying to Claim " + cardName)
                r = requests.put(f"https://discord.com/api/v8/channels/{Vars.channelId}/messages/{idMessage}/reactions/❤️/%40me", headers=auth)
        else:
            print(f"{i:02} - {claimed} --- {cardPower} - {cardName} - {cardSeries}")

        # KAKERA REACTION
        if "components" in jsonCard[0] and len(jsonCard[0]["components"]) > 0:
            try:
                components = jsonCard[0]["components"][0]["components"]
                for component in components:
                    cardsKakera = component["emoji"]["name"]
                    if cardsKakera in Vars.desiredKakeras:
                        bot.click(
                            jsonCard[0]["author"]["id"],
                            channelID=jsonCard[0]["channel_id"],
                            guildID=Vars.serverId,
                            messageID=jsonCard[0]["id"],
                            messageFlags=jsonCard[0]["flags"],
                            data={"component_type": 2, "custom_id": component["custom_id"]},
                        )

                        print(f"{i:02} - {utils.get_kakera_emoji(cardsKakera)} --- {cardsKakera} - Reacted to {utils.get_kakera_name(cardsKakera)}")

            except (KeyError, IndexError):
                cardsKakera = "null"

            except Exception as e:
                print(f"Error: {e}")
                cardsKakera = "null"

        i += 1

    print("Rolling ended")

    if Vars.pokeRoll:
        print("\nTrying to roll Pokeslot")
        requests.post(url=url, headers=auth, data={"content": "$p"})


simpleRoll()
