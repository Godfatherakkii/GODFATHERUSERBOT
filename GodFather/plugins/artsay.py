"""
Created by  godfather.  tg @godfather_K_Boy
Plugin for godfatherUserBot
"""
import asyncio
from collections import deque

from . import eor, godfather, mention

menu_category = "fun"


@godfather.godfather_cmd(
    pattern="carry ([\s\S]*)",
    command=("carry", menu_category),
    info={
        "header": "Fun art try yourself to know more",
        "usage": "{tr}carry <text>",
    },
)
async def _(event):
    "art command"
    name = event.pattern_match.group(1)
    await eor(
        event,
        f"**Carry ➥ {name} .**\n\n                     ⣤⣶⣶⣶⣦⣤⣄⡀\n⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀\n⠀⠀⠀⢀⣾⣿⣿⣿⠿⠿⠟⠻⠿⢿⣿⣿⣿⡆\n⠀⠀⠀⢰⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀ ⠈⠉⢻⡇ \n⠀⠀⠀⠈⠿⣿⣇⣠⠤⠤⠤⢤⣀⣤⠤⠤⣺⡏ \n⠀⠀⠀⠀⠐⢉⣯⠹⣀⣀⣢⡸⠉⢏⡄⣀⣯⠁ \n⠀⠀⠀⠀⠡⠀⢹⣆⠀⠀⠀⣀⡀⡰⠀⢠⠖⠂ \n⠀⠀⠀⠀⠀⠈⠙⣿⣿⠀⠠⠚⢋⡁⠀⡜ \n⠀⠀⠀⠀⠀⠀⢸⠈⠙⠦⣤⣀⣤⣤⡼⠁  \n⠀⠀⠀ ⠀⢀⡌⠀⠀⠀⠀ ⠉⢏⡉  \n⠀⠀⠀⣀⣴⣿⣷⣶⣤⣤⣤⣴⣾⣷⣶⣦⡀ \n⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄ \n⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛",
    )


@godfather.godfather_cmd(
    pattern="🤬$",
    command=("🤬", menu_category),
    info={
        "header": "To Show Ur Angry In Angry Mode",
        "usage": "{tr}🤬",
    },
)
async def _(event):
    event = await eor(event, "𝙸 𝚊𝚖 𝚊𝚗𝚐𝚛𝚢 ")
    deq = deque(list("😡🔥🤬🔥😡🔥🤬🔥😡🔥"))
    for _ in range(20):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)


@godfather.godfather_cmd(
    pattern="🤣$",
    command=("🤣", menu_category),
    info={
        "header": "To Show Ur Laugh In Laugh Rotate Mode",
        "usage": "{tr}🤣",
    },
)
async def _(event):
    event = await eor(event, "Lots Of Laugh")
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(20):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)


@godfather.godfather_cmd(
    pattern="✅$",
    command=("✅", menu_category),
    info={
        "header": "To Confuse True Or False",
        "usage": "{tr}✅",
    },
)
async def _(event):
    event = await eor(event, "Confusion")
    deq = deque(list("✅❌✅❌✅❌✅❌"))
    for _ in range(20):
        await asyncio.sleep(0.5)
        await event.edit("".join(deq))
        deq.rotate(1)


@godfather.godfather_cmd(
    pattern="bakwas$",
    command=("bakwas", menu_category),
    info={
        "header": "To Make Joke",
        "usage": "{tr}bakwas ",
    },
)
async def gn(event):
    await event.edit("Your message has been read and Ignored successfully ┐(´∀｀)┌ 😂😂😂")


@godfather.godfather_cmd(
    pattern="ded(?:\s|$)([\s\S]*)",
    command=("ded", menu_category),
    info={
        "header": "Fun art try yourself to know more",
        "usage": "{tr}ded <text>",
    },
)
async def _(event):
    "art command"
    name = event.pattern_match.group(1)
    if not name:
        name = "dead"
    await eor(
        event,
        f"{mention} --- {name}          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )


@godfather.godfather_cmd(
    pattern="killer(?:\s|$)([\s\S]*)",
    command=("killer", menu_category),
    info={
        "header": "Fun art try yourself to know more",
        "usage": "{tr}killer <text>",
    },
)
async def _(event):
    "art command"
    name = event.pattern_match.group(1)
    if not name:
        name = "die"
    await eor(
        event,
        f"__**Commando **__{mention}          \n\n"
        "_/﹋\_\n"
        "(҂`_´)\n"
        f"<,︻╦╤─ ҉ - - - {name}\n"
        "_/﹋\_\n",
    )


G = (
    "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⠟⠀⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣷⣄⠀⠀⠀⠀⠀\n"
    "⠀⠀⠀⠀⣴⣶⣿⡆⠀⠀⠉⠉⠀⠈⣶⡆⠀\n"
    "⠀⠀⠀⢠⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢻⣷⠀\n"
    "⠀⠀⠀⣼⣿⡿⠟⠀⠀⠀⠀⠀⠀⠀⣸⣿⡄\n"
    "⠀⠀⠀⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣷\n"
    "⠀⠀⠘⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⢰⣾⣿⠏\n"
    "⠀⢠⣧⡔⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠟⠁⠀\n"
    "⠀⢸⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ Ah\n shit, here we go again.\n"
)


@godfather.godfather_cmd(
    pattern="sthink ([\s\S]*)",
    command=("sthink", menu_category),
    info={
        "header": "Fun art try yourself to know more",
        "usage": "{tr}sthink <text>",
    },
)
async def kakashi(think):
    "art command"
    name = think.pattern_match.group(1)
    A = (
        f"**{mention} ➥ {name} .\n\n**"
        "⠀⠀⠀⠀⢀⣀⣀⣀\n"
        "⠀⠀⠀⠰⡿⠿⠛⠛⠻⠿⣷\n"
        "⠀⠀⠀⠀⠀⠀⣀⣄⡀⠀⠀⠀⠀⢀⣀⣀⣤⣄⣀⡀\n"
        "⠀⠀⠀⠀⠀⢸⣿⣿⣷⠀⠀⠀⠀⠛⠛⣿⣿⣿⡛⠿⠷\n"
        "⠀⠀⠀⠀⠀⠘⠿⠿⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⠇\n"
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁\n"
        "⠀\n"
        "⠀⠀⠀⠀⣿⣷⣄⠀⢶⣶⣷⣶⣶⣤⣀\n"
        "⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠈⠙⠻⠗\n"
        "⠀⠀⠀⣰⣿⣿⣿⠀⠀⠀⠀⢀⣀⣠⣤⣴⣶⡄\n"
        "⠀⣠⣾⣿⣿⣿⣥⣶⣶⣿⣿⣿⣿⣿⠿⠿⠛⠃\n"
        "⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄\n"
        "⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡁\n"
        "⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁\n"
        "⠀⠀⠛⢿⣿⣿⣿⣿⣿⣿⡿⠟\n"
    )
    await eor(think, A)


@godfather.godfather_cmd(
    pattern="sfrog ([\s\S]*)",
    command=("sfrog", menu_category),
    info={
        "header": "Fun art try yourself to know more",
        "usage": "{tr}sfrog <text>",
    },
)
async def kakashi(frogsay):
    "art command"
    name = frogsay.pattern_match.group(1)
    C = (
        f"**{mention} ➥ {name} .\n\n**"
        "⠄⠄⠄⠄⠄⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣶⣦⣄⠄\n"
        "⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
        "⢠⠾⣋⣭⣄⡀⠄⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿\n"
        "⡎⡟⢻⣿⣷⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿\n"
        "⡇⣷⣾⣿⠟⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼\n"
        "⣦⣭⣭⣄⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿\n"
        "⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿\n"
        "⡿⠛⠛⠛⠛⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⠈⣆⠄⠄⢿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿\n"
        "⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿\n"
        "⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿\n"
        "⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿\n"
        "⠄⣿⠁⠄⠐⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⠄⠻⣦⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋\n"
    )
    await eor(frogsay, C)


@godfather.godfather_cmd(
    pattern="sputin ([\s\S]*)",
    command=("sputin", menu_category),
    info={
        "header": "Fun art try yourself to know more",
        "usage": "{tr}sputin <text>",
    },
)
async def kakashi(putinsay):
    "art command"
    name = putinsay.pattern_match.group(1)
    D = (
        f"**Vladimir Putin ➥ {name} .\n\n**"
        "⣿⣿⣿⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣵⣿⣿⣿⠿⡟⣛⣧⣿⣯⣿⣝⡻⢿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⠋⠁⣴⣶⣿⣿⣿⣿⣿⣿⣿⣦⣍⢿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⢷⠄⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⢼⣿⣿⣿⣿\n"
        "⢹⣿⣿⢻⠎⠔⣛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⣿⣿⣿⣿\n"
        "⢸⣿⣿⠇⡶⠄⣿⣿⠿⠟⡛⠛⠻⣿⡿⠿⠿⣿⣗⢣⣿⣿⣿⣿\n"
        "⠐⣿⣿⡿⣷⣾⣿⣿⣿⣾⣶⣶⣶⣿⣁⣔⣤⣀⣼⢲⣿⣿⣿⣿\n"
        "⠄⣿⣿⣿⣿⣾⣟⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⢟⣾⣿⣿⣿⣿\n"
        "⠄⣟⣿⣿⣿⡷⣿⣿⣿⣿⣿⣮⣽⠛⢻⣽⣿⡇⣾⣿⣿⣿⣿⣿\n"
        "⠄⢻⣿⣿⣿⡷⠻⢻⡻⣯⣝⢿⣟⣛⣛⣛⠝⢻⣿⣿⣿⣿⣿⣿\n"
        "⠄⠸⣿⣿⡟⣹⣦⠄⠋⠻⢿⣶⣶⣶⡾⠃⡂⢾⣿⣿⣿⣿⣿⣿\n"
        "⠄⠄⠟⠋⠄⢻⣿⣧⣲⡀⡀⠄⠉⠱⣠⣾⡇⠄⠉⠛⢿⣿⣿⣿\n"
        "⠄⠄⠄⠄⠄⠈⣿⣿⣿⣷⣿⣿⢾⣾⣿⣿⣇⠄⠄⠄⠄⠄⠉⠉\n"
        "⠄⠄⠄⠄⠄⠄⠸⣿⣿⠟⠃⠄⠄⢈⣻⣿⣿⠄⠄⠄⠄⠄⠄⠄\n"
        "⠄⠄⠄⠄⠄⠄⠄⢿⣿⣾⣷⡄⠄⢾⣿⣿⣿⡄⠄⠄⠄⠄⠄⠄\n"
        "⠄⠄⠄⠄⠄⠄⠄⠸⣿⣿⣿⠃⠄⠈⢿⣿⣿⠄⠄⠄⠄⠄⠄⠄\n"
    )
    await eor(putinsay, D)


@godfather.godfather_cmd(
    pattern="sdead ([\s\S]*)",
    command=("sdead", menu_category),
    info={
        "header": "Fun art try yourself to know more",
        "usage": "{tr}sdead <text>",
    },
)
async def kakashi(deadfrog):
    "art command"
    name = deadfrog.pattern_match.group(1)
    E = (
        f"**{mention} ➥ {name} .\n\n**"
        "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⠄⣿⣿⣿⡿⠋⣉⣉⣉⡙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⠃⠄⠹⠟⣡⣶⢟⣛⣛⡻⢿⣦⣩⣤⣬⡉⢻⣿⣿⣿⣿\n"
        "⣿⣿⣿⠄⢀⢤⣾⣿⣿⣿⡿⠿⠿⠿⢮⡃⣛⡻⢿⠈⣿⣿⣿⣿\n"
        "⣿⡟⢡⣴⣯⣿⣿⣿⠤⣤⣭⣶⣶⣶⣮⣔⡈⠛⢓⠦⠈⢻⣿⣿\n"
        "⠏⣠⣿⣿⣿⣿⣿⣿⣯⡪⢛⠿⢿⣿⣿⣿⡿⣼⣿⣿⣮⣄⠙⣿\n"
        "⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⡭⠴⣶⣶⣽⣽⣛⡿⠿⠿⠇⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣷⣝⣛⢛⢋⣥⣴⣿⣿\n"
        "⣿⣿⣿⣿⣿⢿⠱⣿⣛⠾⣭⣛⡿⢿⣿⣿⣿⣿⣿⡀⣿⣿⣿⣿\n"
        "⠑⠽⡻⢿⣮⣽⣷⣶⣯⣽⣳⠮⣽⣟⣲⠯⢭⣿⣛⡇⣿⣿⣿⣿\n"
        "⠄⠄⠈⠑⠊⠉⠟⣻⠿⣿⣿⣿⣷⣾⣭⣿⠷⠶⠂⣴⣿⣿⣿⣿\n"
        "⠄⠄⠄⠄⠄⠄⠄⠁⠙⠒⠙⠯⠍⠙⢉⣡⣶⣿⣿⣿⣿⣿⣿⣿\n"
        "⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    )
    await eor(deadfrog, E)


@godfather.godfather_cmd(
    pattern="strump ([\s\S]*)",
    command=("strump", menu_category),
    info={
        "header": "Fun art try yourself to know more",
        "usage": "{tr}strump <text>",
    },
)
async def kakashi(trumpsay):
    "art command"
    name = trumpsay.pattern_match.group(1)
    J = (
        f"**Donald Trump ➥ {name} .\n\n**"
        "⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠉⡉⣉⡛⣛⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡿⠋⠁⠄⠄⠄⠄⠄⢀⣸⣿⣿⡿⠿⡯⢙⠿⣿⣿⣿⣿\n"
        "⣿⣿⡿⠄⠄⠄⠄⠄⡀⡀⠄⢀⣀⣉⣉⣉⠁⠐⣶⣶⣿⣿⣿⣿\n"
        "⣿⣿⡇⠄⠄⠄⠄⠁⣿⣿⣀⠈⠿⢟⡛⠛⣿⠛⠛⣿⣿⣿⣿⣿\n"
        "⣿⣿⡆⠄⠄⠄⠄⠄⠈⠁⠰⣄⣴⡬⢵⣴⣿⣤⣽⣿⣿⣿⣿⣿\n"
        "⣿⣿⡇⠄⢀⢄⡀⠄⠄⠄⠄⡉⠻⣿⡿⠁⠘⠛⡿⣿⣿⣿⣿⣿\n"
        "⣿⡿⠃⠄⠄⠈⠻⠄⠄⠄⠄⢘⣧⣀⠾⠿⠶⠦⢳⣿⣿⣿⣿⣿\n"
        "⣿⣶⣤⡀⢀⡀⠄⠄⠄⠄⠄⠄⠻⢣⣶⡒⠶⢤⢾⣿⣿⣿⣿⣿\n"
        "⣿⡿⠋⠄⢘⣿⣦⡀⠄⠄⠄⠄⠄⠉⠛⠻⠻⠺⣼⣿⠟⠛⠿⣿\n"
        "⠋⠁⠄⠄⠄⢻⣿⣿⣶⣄⡀⠄⠄⠄⠄⢀⣤⣾⣿⡀⠄⠄⠄⢹\n"
        "⠄⠄⠄⠄⠄⠄⢻⣿⣿⣿⣷⡤⠄⠰⡆⠄⠄⠈⠛⢦⣀⡀⡀⠄\n"
        "⠄⠄⠄⠄⠄⠄⠈⢿⣿⠟⡋⠄⠄⠄⢣⠄⠄⠄⠄⠄⠈⠹⣿⣀\n"
        "⠄⠄⠄⠄⠄⠄⠄⠘⣷⣿⣿⣷⠄⠄⢺⣇⠄⠄⠄⠄⠄⠄⠸⣿\n"
        "⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⡇⠄⠄⠸⣿⡄⠄⠈⠁⠄⠄⠄⣿\n"
        "⠄⠄⠄⠄⠄⠄⠄⠄⠄⢻⣿⡇⠄⠄⠄⢹⣧⠄⠄⠄⠄⠄⠄⠘\n"
    )
    await eor(trumpsay, J)


@godfather.godfather_cmd(
    pattern="schina ([\s\S]*)",
    command=("schina", menu_category),
    info={
        "header": "Fun art try yourself to know more",
        "usage": "{tr}schina <text>",
    },
)
async def kakashi(ckmkb):
    "art command"
    name = ckmkb.pattern_match.group(1)
    K = (
        f"**🅲🅺🅼🅺🅱 ➥ {name} .\n\n**"
        "⣿⣿⣿⣿⠟⠋⢁⢁⢁⢁⢁⢁⢁⢁⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⡀⠭⢿⣿⣿⣿⣿\n"
        "⣿⣿⣿⡟⠄⢀⣾⣿⣿⣿⣷⣶⣿⣷⣶⣶⡆⠄⠄⠄⣿⣿⣿⣿\n"
        "⣿⣿⣿⡇⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠄⠄⢸⣿⣿⣿⣿\n"
        "⣿⣿⣿⣇⣼⣿⣿⠿⠶⠙⣿⡟⠡⣴⣿⣽⣿⣧⠄⢸⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣾⣿⣿⣟⣭⣾⣿⣷⣶⣶⣴⣶⣿⣿⢄⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣿⡟⣩⣿⣿⣿⡏⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣹⡋⠘⠷⣦⣀⣠⡶⠁⠈⠁⠄⣿⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣍⠃⣴⣶⡔⠒⠄⣠⢀⠄⠄⠄⡨⣿⣿⣿⣿⣿⣿\n"
        "⣿⣿⣿⣿⣿⣿⣦⡘⠿⣷⣿⠿⠟⠃⠄⠄⣠⡇⠈⠻⣿⣿⣿⣿\n"
        "⣿⣿⣿⡿⠟⠋⢁⣷⣠⠄⠄⠄⠄⣀⣠⣾⡟⠄⠄⠄⠄⠉⠙⠻\n"
        "⡿⠟⠁⠄⠄⠄⢸⣿⣿⡯⢓⣴⣾⣿⣿⡟⠄⠄⠄⠄⠄⠄⠄⠄\n"
        "⠄⠄⠄⠄⠄⠄⣿⡟⣷⠄⠹⣿⣿⣿⡿⠁⠄⠄⠄⠄⠄⠄⠄⠄\n"
        "⠄⠄⠄⠄⠄⣸⣿⡷⡇⠄⣴⣾⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
        "⠄⠄⠄⠄⠄⣿⣿⠃⣦⣄⣿⣿⣿⠇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
        "⠄⠄⠄⠄⢸⣿⠗⢈⡶⣷⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\n"
    )
    await eor(ckmkb, K)


@godfather.godfather_cmd(
    pattern="sshit$",
    command=("sshit", menu_category),
    info={
        "header": "Fun art try yourself to know more",
        "usage": "{tr}sshit <text>",
    },
)
async def kakashi(shit):
    "art command"
    await eor(shit, G)
