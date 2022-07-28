from faker import Faker

from . import eor, godfather

menu_category = "useless"


@godfather.godfather_cmd(
    pattern="gencc(?:\s|$)([\s\S]*)",
    command=("gencc", menu_category),
    info={
        "header": "To Make Fake Credit Card in short help u to generate fake cc",
        "usage": [
            "{tr}gencc",
        ],
    },
)
async def _(godfatherevent):
    if godfatherevent.fwd_from:
        return
    godfathercc = Faker()
    godfathername = godfathercc.name()
    godfatheradre = godfathercc.address()
    godfathercard = godfathercc.credit_card_full()

    await eor(
        godfatherevent,
        f"__**👤 NAME :- **__\n`{godfathername}`\n\n__**🏡 ADDRESS :- **__\n`{godfatheradre}`\n\n__**💸 CARD :- **__\n`{godfathercard}`",
    )
