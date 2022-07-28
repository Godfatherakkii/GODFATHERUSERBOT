from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from GodFather import godfather

from ..core.managers import eor

menu_category = "utils"


@godfather.godfather_cmd(
    pattern="ctg$",
    command=("ctg", menu_category),
    info={
        "header": "Reply to link To get link preview using telegrah.s.",
        "usage": "{tr}ctg",
    },
)
async def _(event):
    "To get link preview"
    reply_message = await event.get_reply_message()
    if not reply_message:
        await eor(event, "```Reply to a Link.```")
        return
    if not reply_message.text:
        await eor(event, "```Reply to a Link```")
        return
    chat = "@chotamreaderbot"
    godfatherevent = await eor(event, "```Processing```")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await godfatherevent.edit(
                "`RIP Check Your Blacklist Boss and unblock @chotamreaderbot`"
            )
            return
        if response.text.startswith(""):
            await godfatherevent.edit("Am I Dumb Or Am I Dumb?")
        else:
            await godfatherevent.delete()
            await event.client.send_message(event.chat_id, response.message)
