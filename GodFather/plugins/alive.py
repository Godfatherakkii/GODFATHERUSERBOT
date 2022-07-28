import asyncio
import random
import re
import time
from datetime import datetime
from platform import python_version

from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from GodFather import StartTime, godfather, godfatherversion

from ..Config import Config
from ..core.managers import eor
from ..helpers.functions import check_data_base_heal_th, get_readable_time, godfatheralive
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

menu_category = "utils"


@godfather.godfather_cmd(
    pattern="godfather$",
    command=("godfather", menu_category),
    info={
        "header": "To check bot's alive status",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}godfather",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    godfatherevent = await eor(event, "`Checking...`")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    _, check_sgnirts = check_data_base_heal_th()
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT")
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✥"
    lal = list(EMOJI.split())
    EMOTES = random.choice(lal)
    sweetie_caption = (
        "**⚜ GodFather Is Online ⚜**\n\n" + f"{gvarstatus('ALIVE_TEMPLATE')}"
    )
    caption = sweetie_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        EMOTES=EMOTES,
        mention=mention,
        uptime=uptime,
        telever=version.__version__,
        godfatherver=godfatherversion,
        pyver=python_version(),
        dbhealth=check_sgnirts,
        ping=ms,
    )
    try:
        results = await event.client.inline_query(Config.BOT_USERNAME, caption)
        await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
        await event.delete()
    except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
        return await eor(
            godfatherevent,
            f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{godfather_IMG}`",
        )


"""
temp = {ALIVE_TEXT}
**{EMOTES} Master:** {mention}
**{EMOTES} Uptime :** `{uptime}`
**{EMOTES} Telethon Version :** `{telever}`
**{EMOTES} godfatheruserbot Version :** `{godfatherver}`
**{EMOTES} Python Version :** `{pyver}`
**{EMOTES} Database :** `{dbhealth}`
"""


@godfather.godfather_cmd(
    pattern="alive$",
    command=("alive", menu_category),
    info={
        "header": "To check bot's alive status via inline mode",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}alive",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details by your inline bot"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    a = gvarstatus("ALIVE_EMOJI") or "✥"
    kiss = list(a.split())
    EMOJI = random.choice(kiss)
    godfather_caption = "**GodFather Is Online**\n\n"
    godfather_caption += f"**{EMOJI} Telethon version :** `{version.__version__}\n`"
    godfather_caption += f"**{EMOJI} godfatheruserbot Version :** `{godfatherversion}`\n"
    godfather_caption += f"**{EMOJI} Python Version :** `{python_version()}\n`"
    godfather_caption += f"**{EMOJI} Uptime :** {uptime}\n"
    godfather_caption += f"**{EMOJI} Master:** {mention}\n"
    results = await event.client.inline_query(Config.BOT_USERNAME, godfather_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


edit_time = 12
""" =======================CONSTANTS====================== """
file1 = "https://te.legra.ph/file/2426eab17330c6e6310ea.mp4"
file2 = "https://te.legra.ph/file/11ec9dd576ee5536125b2.jpg"
file3 = "https://te.legra.ph/file/d2a5265abdc4e73af1f94.jpg"
file4 = "https://telegra.ph/file/b6f0c65a337b1f2609d07.jpg"
file5 = "https://telegra.ph/file/af51de2749a4506d3eb43.jpg"
""" =======================CONSTANTS====================== """
pm_caption = f"**GodFather Is Up**\n"
pm_caption += f"**╭────────────**\n"
pm_caption += f"┣»»»『{mention}』«««\n"
pm_caption += f"┣Lêɠêɳ̃dẞø† ~ {godfatherversion}\n"
pm_caption += f"┣Lêɠêɳ̃d  ~ [Owner](https://t.me/godfather_K_Boy)\n"
pm_caption += f"┣Support ~ [G𝖗ουρ](https://t.me/GodFather_OP)\n"
pm_caption += f"┣Řepô    ~ [Rєρο](https://github.com/godfather-AI/GodFather)\n"
pm_caption += f"**╰────────────**\n"


@godfather.godfather_cmd(
    pattern="about$",
    command=("about", menu_category),
    info={
        "header": "To check bot's alive status ",
        "options": "Random Media Automatically Get It",
        "usage": [
            "{tr}about",
        ],
    },
)
async def amireallyalive(yes):
    await yes.get_chat()
    on = await borg.send_file(yes.chat_id, file=file1, caption=pm_caption)
    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2)
    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file4)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file3)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file2)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file1)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file2)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(yes.chat_id, ok9, file=file3)

    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(yes.chat_id, ok10, file=file4)

    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(yes.chat_id, ok11, file=file5)

    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(yes.chat_id, ok12, file=file1)

    await yes.delete()
    await borg.send_file(yes.chat_id, PM_IMG, caption=pm_caption)
    await yes.delete()


@godfather.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await godfatheralive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
