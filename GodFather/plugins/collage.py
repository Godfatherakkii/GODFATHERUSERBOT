# collage plugin for godfatherUserBot by @godfather_K_BOY

# Copyright (C) 2020 Alfiananda P.A
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.import os

import os

from GodFather import godfather

from ..core.managers import eod, eor
from ..helpers import reply_id
from ..helpers.utils import _godfatherutils
from . import make_gif

menu_category = "utils"


@godfather.godfather_cmd(
    pattern="collage(?:\s|$)([\s\S]*)",
    command=("collage", menu_category),
    info={
        "header": "To create collage from still images extracted from video/gif.",
        "description": "Shows you the grid image of images extracted from video/gif. you can customize the Grid size by giving integer between 1 to 9 to cmd by default it is 3",
        "usage": "{tr}collage <1-9> <reply to  ani sticker/mp4.",
    },
)
async def collage(event):
    "To create collage from still images extracted from video/gif."
    godfatherinput = event.pattern_match.group(1)
    reply = await event.get_reply_message()
    godfatherid = await reply_id(event)
    event = await eor(event, "```Wait A Minute Its Collaging😁```")
    if not (reply and (reply.media)):
        await event.edit("`Media not found...`")
        return
    if not os.path.isdir("./temp/"):
        os.mkdir("./temp/")
    godfathersticker = await reply.download_media(file="./temp/")
    if not godfathersticker.endswith((".mp4", ".mkv", ".tgs")):
        os.remove(godfathersticker)
        await event.edit("`Media format is not supported...`")
        return
    if godfatherinput:
        if not godfatherinput.isdigit():
            os.remove(godfathersticker)
            await event.edit("`You input is invalid, check help`")
            return
        godfatherinput = int(godfatherinput)
        if not 0 < godfatherinput < 10:
            os.remove(godfathersticker)
            await event.edit(
                "`Why too big grid you cant see images, use size of grid between 1 to 9`"
            )
            return
    else:
        godfatherinput = 3
    if godfathersticker.endswith(".tgs"):
        hmm = await make_gif(event, godfathersticker)
        if hmm.endswith(("@tgstogifbot")):
            os.remove(godfathersticker)
            return await event.edit(hmm)
        collagefile = hmm
    else:
        collagefile = godfathersticker
    endfile = "./temp/collage.png"
    godfathercmd = f"vcsi -g {godfatherinput}x{godfatherinput} '{collagefile}' -o {endfile}"
    stdout, stderr = (await _godfatherutils.runcmd(godfathercmd))[:2]
    if not os.path.exists(endfile):
        for files in (godfathersticker, collagefile):
            if files and os.path.exists(files):
                os.remove(files)
        return await eod(
            event, "`media is not supported or try with smaller grid size`", 5
        )

    await event.client.send_file(
        event.chat_id,
        endfile,
        reply_to=godfatherid,
    )
    await event.delete()
    for files in (godfathersticker, collagefile, endfile):
        if files and os.path.exists(files):
            os.remove(files)
