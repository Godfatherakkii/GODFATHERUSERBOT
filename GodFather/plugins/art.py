import asyncio

from ..helpers.utils import reply_id
from . import ALIVE_NAME, eor, godfather

menu_category = "fun"


@godfather.godfather_cmd(
    pattern="ded ([\s\S]*)",
    command=("ded", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}ded <text>",
    },
)
async def ded(event):
    "fun art command"
    if name := event.text[4:]:
        return await eor(
            event,
            f"{ALIVE_NAME} --- {name}          \n　　　　　|"
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
    else:
        return await eor(event, "Give me some text")


@godfather.godfather_cmd(
    pattern="killer ([\s\S]*)",
    command=("killer", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}killer <text>",
    },
)
async def killer(event):
    "fun art command"
    if name := event.pattern_match.group(1):
        return await eor(
            event,
            f"__**Commando **__{ALIVE_NAME}          \n\n"
            "_/﹋\_\n"
            "(҂`_´)\n"
            f"<,︻╦╤─ ҉ - - - {name}\n"
            "_/﹋\_\n",
        )
    else:
        return await eor("Give me some Text")


A = (
    "▄███████▄\n"
    "█▄█████▄█\n"
    "█▼▼▼▼▼█\n"
    "██________█▌\n"
    "█▲▲▲▲▲█\n"
    "█████████\n"
    "_████\n"
)

B = (
    "┈┈┏━╮╭━┓┈╭━━━━╮\n"
    "┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ┃\n"
    "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
    "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
    "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
    "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
    "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
    "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n"
)

D = (
    "░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄\n"
    "░███████████████████████ \n"
    "░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤ \n"
    "░▀░▐▓▓▓▓▓▓▌▀█░░░█▀░\n"
    "░░░▓▓▓▓▓▓█▄▄▄▄▄█▀░░\n"
    "░░█▓▓▓▓▓▌░░░░░░░░░░\n"
    "░▐█▓▓▓▓▓░░░░░░░░░░░\n"
    "░▐██████▌░░░░░░░░░░\n"
)

E = (
    "╥━━━━━━━━╭━━╮━━┳\n"
    "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
    "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
    "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
    "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
    "╨━━┗┛┗┛━━┗┛┗┛━━┻\n"
)
F = "╔┓┏╦━╦┓╔┓╔━━╗\n" "║┗┛║┗╣┃║┃║X X║\n" "║┏┓║┏╣┗╣┗╣╰╯║\n" "╚┛┗╩━╩━╩━╩━━╝\n"
G = (
    "▬▬▬.◙.▬▬▬ \n"
    "═▂▄▄▓▄▄▂ \n"
    "◢◤ █▀▀████▄▄▄▄◢◤ \n"
    "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
    "◥█████◤ \n"
    "══╩══╩══ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ \n"
    "╬═╬ Hello, My Friend :D \n"
    "╬═╬☻/ \n"
    "╬═╬/▌ \n"
    "╬═╬/ \\n"
)

H = (
    "┳┻┳┻╭━━━━╮╱▔▔▔╲\n"
    "┻┳┻┳┃╯╯╭━┫▏╰╰╰▕\n"
    "┳┻┳┻┃╯╯┃▔╰┓▔▂▔▕╮\n"
    "┻┳┻┳╰╮╯┃┈╰┫╰━╯┏╯\n"
    "┳┻┳┻┏╯╯┃╭━╯┳━┳╯\n"
    "┻┳┻┳╰━┳╯▔╲╱▔╭╮▔╲\n"
    "┳┻┳┻┳┻┃┈╲┈╲╱╭╯╮▕\n"
    "┻┳┻┳┻┳┃┈▕╲▂╱┈╭╯╱\n"
    "┳┻┳┻┳┻┃'''┈┃┈┃┈'''╰╯\n"
    "┻┳┻┳┻┏╯▔'''╰┓┣━┳┫\n"
    "┳┻┳┻┳╰┳┳┳'''╯┃┈┃┃\n"
    "┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃\n"
    "┳┻┳┻┳┻┃┃┃'''┊┃┈┃┃\n"
    "┻┳┻┳┻┳┃┃┃┈'''┃┈┃┃.\n"
    "┳┻┳┻┳┻┣╋┫'''┊┣━╋┫\n"
    "┻┳┻┳┻╭╯╰╰-╭╯━╯.''╰╮\n"
    "Love You Forever,,,,\n"
)

I = (
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠋⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⣠⣾⣿⡿⠋⠀⠀⠉⠻⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⠃⠀⠀⣀⡀⠀⢹⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡄⠀⠙⠻⠋⠀⠀⣸⣿⣿⠀⠀⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⣰⣿⣿⠟⠀⢠⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠛⠛⠒⠶⠾⢿⣿⣿⣷⣄⣾⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢰⣿⣿⣷⣶⣦⣼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡀⠀⠙⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⢿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⠀⠀⠀⠉⠉⠛⠛⠛⠶⢶⣤⣼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⣾⣿⣷⡄⠀⢼⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⡿⠀⠈⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣇⠀⠀⠉⠋⠁⠀⢠⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠿⢷⣤⣀⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠀⠈⠉⠉⠛⢻⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣶⣦⣤⣤⣀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡿⠛⠉⠉⠙⠻⣀⣀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠁⠀⣀⡀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣷⡀⠘⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡄⠈⢻⡇⠀⡿⠃⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣷⣄⢸⡇⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠉⠉⠑⠒⠲⠿⢿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣤⣄⣀⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢺⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠉⠉⠙⠋⠀⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣤⣤⣀⣀⡀⠀⠀⣰⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⠀⢹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⠉⠉⠀⠀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣶⣤⣤⣀⣀⣀⣀⣰⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡟⠉⠀⠀⠈⠙⢿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢀⣤⡄⠀⡀⠀⢹⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠀⢸⣿⡇⠀⣿⡄⠈⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡆⠀⢹⡇⠀⠟⠁⢀⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣦⣸⡇⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
)

J = (
    "⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n"
    "⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n"
    "⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n"
    "⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n"
    "⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n"
    "⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
    "⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
)

K = (
    "───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n"
    "───█▒▒░░░░░░░░░▒▒█───\n"
    "────█░░█░░░░░█░░█────\n"
    "─▄▄──█░░░▀█▀░░░█──▄▄─\n"
    "█░░█─▀▄░░░░░░░▄▀─█░░█\n"
    "█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n"
    "█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n"
    "█░░║║║╠─║─║─║║║║║╠─░░█\n"
    "█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n"
    "█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n"
)

L = (
    "░░░░▓\n"
    "░░░▓▓\n"
    "░░█▓▓█\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░░░██▓▓██\n"
    "░░░░██▓▓██\n"
    "░░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░██▓▓██\n"
    "░░░██▓▓███\n"
    "░░░░██▓▓████\n"
    "░░░░░██▓▓█████\n"
    "░░░░░░██▓▓██████\n"
    "░░░░░░███▓▓███████\n"
    "░░░░░████▓▓████████\n"
    "░░░░█████▓▓█████████\n"
    "░░░█████░░░█████●███\n"
    "░░████░░░░░░░███████\n"
    "░░███░░░░░░░░░██████\n"
    "░░██░░░░░░░░░░░████\n"
    "░░░░░░░░░░░░░░░░███\n"
    "░░░░░░░░░░░░░░░░░░░\n"
)


P = (
    "╭━━━┳╮╱╱╭╮╱╭━━━┳━━━╮\n"
    "┃╭━╮┃┃╱╭╯╰╮┃╭━╮┃╭━╮┃\n"
    "┃╰━━┫╰━╋╮╭╯┃┃╱┃┃╰━━╮\n"
    "╰━━╮┃╭╮┣┫┃╱┃┃╱┃┣━━╮┃\n"
    "┃╰━╯┃┃┃┃┃╰╮┃╰━╯┃╰━╯┃\n"
    "╰━━━┻╯╰┻┻━╯╰━━━┻━━━╯\n"
)


R = (
    "███████▄▄███████████▄\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n"
    "▓▓▓▓▓▓███░░░░░░░░░░░░█\n"
    "██████▀░░█░░░░██████▀\n"
    "░░░░░░░░░█░░░░█\n"
    "░░░░░░░░░░█░░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░█░░█\n"
    "░░░░░░░░░░░░▀▀\n"
)


XZ = (
    "┈┈┈┈╱▔▔▔▔▔╲┈╱▔╲\n"
    "┈┈┈┈▏┈┈▏╭╮▕┈▏╳▕\n"
    "┈┈┈┈▏┈┈▏┈┈▕┈╲▂╱\n"
    "┈╱▔▔╲▂╱╲▂▂┈╲▂▏▏\n"
    "╭▏┈┈┈┈┈┈┈▏╲▂▂╱┈\n"
    "┃▏┈┈┈┈▏┈┈▏┈┈┈┈┈\n"
    "╯▏┈╲╱▔╲▅▅▏┈┈┈┈\n"
    "┈╲▅▅▏▕▔▔▔▔▏┈┈┈┈\n"
)

XYX = (
    "┈┈┈╭━━━━━╮┈┈┈┈┈\n"
    "┈┈┈┃┊┊┊┊┊┃┈┈┈┈┈\n"
    "┈┈┈┃┊┊╭━╮┻╮┈┈┈┈\n"
    "┈┈┈╱╲┊┃▋┃▋┃┈┈┈┈\n"
    "┈┈╭┻┊┊╰━┻━╮┈┈┈┈\n"
    "┈┈╰┳┊╭━━━┳╯┈┈┈┈\n"
    "┈┈┈┃┊┃╰━━┫┈HOMER\n"
    "┈┈┈┈┈┈┏━┓┈┈┈┈┈┈\n"
)


@godfather.godfather_cmd(
    pattern="homer$",
    command=("homer", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}homer",
    },
)
async def bluedevilmonster(homer):
    "fun art command"
    await eor(homer, XYX)


@godfather.godfather_cmd(
    pattern="elephant$",
    command=("elephant", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}elephant",
    },
)
async def bluedmonster(elephant):
    "fun art command"
    await eor(elephant, XZ)


@godfather.godfather_cmd(
    pattern="monster$",
    command=("monster", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}monster",
    },
)
async def bluilmonster(monster):
    "fun art command"
    await eor(monster, A)


@godfather.godfather_cmd(
    pattern="pig$",
    command=("pig", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}pig",
    },
)
async def bevilpig(pig):
    "fun art command"
    await eor(pig, B)


@godfather.godfather_cmd(
    pattern="gun$",
    command=("gun", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}gun",
    },
)
async def blueilgun(gun):
    "fun art command"
    await eor(gun, D)


@godfather.godfather_cmd(
    pattern="dog$",
    command=("dog", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}dog",
    },
)
async def blueldog(dog):
    "fun art command"
    await eor(dog, E)


@godfather.godfather_cmd(
    pattern="hello$",
    command=("hello", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hello",
    },
)
async def viello(event):
    "fun art command"
    reply_to_id = await reply_id(event)
    event = await eor(event, "**(❛ Hi ❜!**")
    HELL_PIC = "https://te.legra.ph/file/b86eff074051b0b2d4513.jpg"
    K_PIC = "https://te.legra.ph/file/a679e3d061ac6b349cd60.jpg"
    L_PIC = "https://te.legra.ph/file/96c2b61d6361f112ceac5.jpg"
    M_PIC = "https://te.legra.ph/file/4d0c641e085f7ed15dfec.jpg"
    if HELL_PIC:
        HELLO = f"╔┓┏╦━╦┓╔┓╔━━╗\n"
        HELLO += f"║┗┛║┗╣┃║┃║X X ║\n"
        HELLO += f"║┏┓║┏╣┗╣┗╣╰╯║\n"
        HELLO += f"╚┛┗╩━╩━╩━╩━━╝\n"
        on = await event.client.send_file(
            event.chat_id, file=HELL_PIC, caption=HELLO, reply_to=reply_to_id
        )
        await asyncio.sleep(3)
        ok = await event.client.edit_message(event.chat_id, on, file=K_PIC)
        await asyncio.sleep(3)
        ok1 = await event.client.edit_message(event.chat_id, on, file=L_PIC)
        await asyncio.sleep(3)
        ok2 = await event.client.edit_message(event.chat_id, ok1, file=M_PIC)
        await asyncio.sleep(5)
        ok3 = await event.client.edit_message(event.chat_id, ok2, file=L_PIC)
        await asyncio.sleep(5)
        ok4 = await event.client.edit_message(event.chat_id, ok3, file=K_PIC)
        await asyncio.sleep(5)
        ok5 = await event.client.edit_message(event.chat_id, ok4, file=HELL_PIC)
        await event.delete()


@godfather.godfather_cmd(
    pattern="hmf$",
    command=("hmf", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}hmf",
    },
)
async def blueilhmf(hmf):
    "fun art command"
    await eor(hmf, G)


@godfather.godfather_cmd(
    pattern="couple$",
    command=("couple", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}couple",
    },
)
async def bluedecouple(couple):
    "fun art command"
    await eor(couple, H)


@godfather.godfather_cmd(
    pattern="sup$",
    command=("sup", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}sup",
    },
)
async def bluedevilreme(supreme):
    "fun art command"
    await eor(supreme, I)


@godfather.godfather_cmd(
    pattern="india$",
    command=("india", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}india",
    },
)
async def bluedindia(india):
    "fun art command"
    await eor(india, J)


@godfather.godfather_cmd(
    pattern="wc$",
    command=("wc", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}wc",
    },
)
async def bdevilwelcome(welcome):
    "fun art command"
    await eor(welcome, K)


@godfather.godfather_cmd(
    pattern="snk$",
    command=("snk", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}snk",
    },
)
async def bluvilsnake(snake):
    "fun art command"
    await eor(snake, L)


@godfather.godfather_cmd(
    pattern="carry$",
    command=("carry", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}carry <name> ",
    },
)
async def lnd(event):
    "Just a art command try out yourself to see"
    if name := event.pattern_match.group(1):
        return await eor(
            event,
            f"**Carry ~> {name} .**\n\n                     ⣤⣶⣶⣶⣦⣤⣄⡀\n⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀\n⠀⠀⠀⢀⣾⣿⣿⣿⠿⠿⠟⠻⠿⢿⣿⣿⣿⡆\n⠀⠀⠀⢰⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀ ⠈⠉⢻⡇ \n⠀⠀⠀⠈⠿⣿⣇⣠⠤⠤⠤⢤⣀⣤⠤⠤⣺⡏ \n⠀⠀⠀⠀⠐⢉⣯⠹⣀⣀⣢⡸⠉⢏⡄⣀⣯⠁ \n⠀⠀⠀⠀⠡⠀⢹⣆⠀⠀⠀⣀⡀⡰⠀⢠⠖⠂ \n⠀⠀⠀⠀⠀⠈⠙⣿⣿⠀⠠⠚⢋⡁⠀⡜ \n⠀⠀⠀⠀⠀⠀⢸⠈⠙⠦⣤⣀⣤⣤⡼⠁  \n⠀⠀⠀ ⠀⢀⡌⠀⠀⠀⠀ ⠉⢏⡉  \n⠀⠀⠀⣀⣴⣿⣷⣶⣤⣤⣤⣴⣾⣷⣶⣦⡀ \n⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄ \n⠚⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛",
        )
    else:
        return await eod(event, "Give Me Some Text")


@godfather.godfather_cmd(
    pattern="dead$",
    command=("dead", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}dead",
    },
)
async def lon(frog):
    "Just a art command try out yourself to see"
    name = frog.pattern_match.group(1)
    D = (
        f"**{ALIVE_NAME} ~> {name} .\n\n**"
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
    if name:
        await eor(frog, D)
    else:
        await eor(frog, "Give me Some Text")


@godfather.godfather_cmd(
    pattern="shitos$",
    command=("shitos", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}shitos",
    },
)
async def blueilshitos(shitos):
    "fun art command"
    await eor(shitos, P)


@godfather.godfather_cmd(
    pattern="dislike$",
    command=("dislike", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}dislike",
    },
)
async def bluslike(dislike):
    "fun art command"
    await eor(dislike, R)


@godfather.godfather_cmd(
    pattern="sthink$",
    command=("sthink", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}sthink <text>",
    },
)
async def gend(think):
    "Just a art command try out yourself to see"
    B = (
        f"**{ALIVE_NAME} ~> {name} .\n\n**"
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
    if name := think.pattern_match.group(1):
        return await eor(think, B)
    else:
        return await eor(think, "Give Me Some Text")


@godfather.godfather_cmd(
    pattern="frog$",
    command=("frog", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}frog <text>",
    },
)
async def lj(frogsay):
    "Just a art command try out yourself to see"
    C = (
        f"**{ALIVE_NAME} ~> {name} .\n\n**"
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
    if name := frogsay.pattern_match.group(1):
        return await eor(frogsay, C)
    else:
        return await eor(frogsay, "Give Me Some Text")


@godfather.godfather_cmd(
    pattern="bye$",
    command=("bye", menu_category),
    info={
        "header": "Just a art command try out yourself to see",
        "usage": "{tr}bye",
    },
)
async def blilbye(event):
    "fun art command"
    reply_to_id = await reply_id(event)
    if BYE_PIC := "https://te.legra.ph/file/aa16cad62645045062c0f.jpg":
        godfatherevent = await eor(event, "**❛ Bye ❜!**")
        lol = "Bye Friends"
        await event.client.send_file(
            event.chat_id, BYE_PIC, caption=lol, reply_to=reply_to_id
        )
        await godfatherevent.delete()
