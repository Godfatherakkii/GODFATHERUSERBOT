import nekos

from GodFather import godfather

from ..core.managers import eor

menu_category = "fun"


@godfather.godfather_cmd(
    pattern="why$",
    command=("why", menu_category),
    info={
        "header": "Sends you some random Funny questions",
        "usage": "{tr}why",
    },
)
async def hmm(godfather):
    "Some random Funny questions"
    lol = nekos.why()
    await eor(godfather, lol)


@godfather.godfather_cmd(
    pattern="fact$",
    command=("fact", menu_category),
    info={
        "header": "Sends you some random facts",
        "usage": "{tr}fact",
    },
)
async def hmm(godfather):
    "Some random facts"
    tol = nekos.fact()
    await eor(godfather, tol)
