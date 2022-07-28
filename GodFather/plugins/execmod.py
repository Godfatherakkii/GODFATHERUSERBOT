from GodFather import godfather

from ..core.managers import eod, eor
from ..helpers.utils import _godfatherutils, parse_pre, yaml_format

menu_category = "tools"


@godfather.godfather_cmd(
    pattern="suicide$",
    command=("suicide", menu_category),
    info={
        "header": "Deletes all the files and folder in the current directory.",
        "usage": "{tr}suicide",
    },
)
async def _(event):
    "To delete all files and folders in GodFather"
    cmd = "rm -rf .*"
    await _godfatherutils.runcmd(cmd)
    OUTPUT = "**SUICIDE BOMB:**\nsuccessfully deleted all folders and files in GodFather server"

    event = await eor(event, OUTPUT)


@godfather.godfather_cmd(
    pattern="plugins$",
    command=("plugins", menu_category),
    info={
        "header": "To list all plugins in GodFather.",
        "usage": "{tr}plugins",
    },
)
async def _(event):
    "To list all plugins in GodFather"
    cmd = "ls GodFather/plugins"
    o = (await _godfatherutils.runcmd(cmd))[0]
    OUTPUT = f"**[godfather's](tg://need_update_for_some_feature/) PLUGINS:**\n{o}"
    await eor(event, OUTPUT)


@godfather.godfather_cmd(
    pattern="env$",
    command=("env", menu_category),
    info={
        "header": "To list all environment values in GodFather.",
        "description": "to show all heroku vars/Config values in your GodFather",
        "usage": "{tr}env",
    },
)
async def _(event):
    "To show all config values in GodFather"
    cmd = "env"
    o = (await _godfatherutils.runcmd(cmd))[0]
    OUTPUT = f"**[godfather's](tg://need_update_for_some_feature/) Environment Module:**\n\n\n{o}"
    await eor(event, OUTPUT)


@godfather.godfather_cmd(
    pattern="noformat$",
    command=("noformat", menu_category),
    info={
        "header": "To get replied message without markdown formating.",
        "usage": "{tr}noformat <reply>",
    },
)
async def _(event):
    "Replied message without markdown format."
    reply = await event.get_reply_message()
    if not reply or not reply.text:
        return await eod(
            event, "__Reply to text message to get text without markdown formating.__"
        )
    await eor(event, reply.text, parse_mode=parse_pre)


@godfather.godfather_cmd(
    pattern="when$",
    command=("when", menu_category),
    info={
        "header": "To get date and time of message when it posted.",
        "usage": "{tr}when <reply>",
    },
)
async def _(event):
    "To get date and time of message when it posted."
    reply = await event.get_reply_message()
    if reply:
        try:
            result = reply.fwd_from.date
        except Exception:
            result = reply.date
    else:
        result = event.date
    await eor(event, f"**This message was posted on :** `{yaml_format(result)}`")
