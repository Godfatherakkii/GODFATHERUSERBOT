import sys

import GodFather
from GodFather import BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from .Config import Config
from .core.logger import logging
from .core.session import godfather
from .start import killer
from .utils import (
    add_bot_to_logger_group,
    hekp,
    install_extrarepo,
    load_plugins,
    setup_bot,
    startupmessage,
    verifyLoggerGroup,
)

LOGS = logging.getLogger("godfatherUserBot")

print(GodFather.__copyright__)
print("Licensed under the terms of the " + GodFather.__license__)

cmdhr = Config.HANDLER


async def extrarepo():
    if Config.EXTRA_REPO:
        await install_extrarepo(
            Config.EXTRA_REPO, Config.EXTRA_REPOBRANCH, "xtraplugins"
        )


try:
    LOGS.info("Starting Userbot")
    godfather.loop.run_until_complete(setup_bot())
    LOGS.info("TG Bot Startup Completed")
except Exception as e:
    LOGS.error(f"{e}")
    sys.exit()


async def startup_process():
    try:
        await verifyLoggerGroup()
        await load_plugins("plugins")
        await load_plugins("assistant")
        await killer()
        print(f"""『🔱GODFATHER-BOT🔱』➙𖤍࿐ IS ON!!! GODFATHER VERSION :- {godfatherversion}
              TYPE :- " .gpromote @Godfatherakki" OR .help OR .ping CHECK IF I'M ON!
                  ╔════❰GODFATHER-BOT❱═❍⊱❁۪۪
                  ║┣⪼ OWNER - GODFATHER-AKKII
                  ║┣⪼{godfather_PIC}
                  ║┣⪼ CREATOR -@Godfatherakki
                  ║┣⪼ TELETHON - 1.2.0
                  ║┣⪼ ✨ 『🔱G O D F A T H E R🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
                  ║╰━━━━━━━━━━━━━━━➣
                  ╚══════════════════❍⊱""")
        await verifyLoggerGroup()
        await add_bot_to_logger_group(BOTLOG_CHATID)
        if PM_LOGGER_GROUP_ID != -100:
            await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)
        await startupmessage()
        await extrarepo()
        await hekp()
    except Exception as e:
        LOGS.error(f"{str(e)}")
        sys.exit()


godfather.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):
    godfather.disconnect()
else:
    try:
        godfather.run_until_disconnected()
    except ConnectionError:
        pass
