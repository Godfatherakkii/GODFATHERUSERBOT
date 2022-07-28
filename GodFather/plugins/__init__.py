import math
import os
import re
import time

import heroku3
import lottie
import requests
import spamwatch as spam_watch
from validators.url import url

from .. import *
from ..Config import Config
from ..core.logger import logging
from ..core.managers import eod, eor
from ..core.session import godfather
from ..helpers import *
from ..helpers.utils import _format, _godfathertools, _godfatherutils, install_pip, reply_id
from ..sql_helper.globals import gvarstatus

# =================== CONSTANT ===================
bot = godfather
LOGS = logging.getLogger(__name__)
USERID = godfather.uid if Config.OWNER_ID == 0 else Config.OWNER_ID
ALIVE_NAME = Config.ALIVE_NAME
AUTONAME = Config.AUTONAME
DEFAULT_BIO = Config.DEFAULT_BIO


Heroku = heroku3.from_key(Config.API_KEY)
heroku_api = "https://api.heroku.com"
APP_NAME = Config.APP_NAME
API_KEY = Config.API_KEY

thumb_image_path = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, "thumb_image.jpg")


# mention user
mention = f"[{Config.ALIVE_NAME}](tg://user?id={USERID})"
hmention = f"<a href = tg://user?id={USERID}>{Config.ALIVE_NAME}</a>"


godfather_USER = godfather.me.first_name
godfather_Boy = godfather.uid
godfather_mention = f"[{godfather_USER}](tg://user?id={godfather_Boy})"


# pic
gban_pic = "./GodFather/helpers/resources/pics/gban.mp4"
main_pic = "./GodFather/helpers/resources/pics/main.jpg"
core_pic = "./GodFather/helpers/resources/pics/core.jpg"
chup_pic = "./GodFather/helpers/resources/pics/chup.mp4"
bsdk_pic = "./GodFather/helpers/resources/pics/bsdk.jpg"
bsdkwale_pic = "./GodFather/helpers/resources/pics/bsdk_wale.jpg"
chutiya_pic = "./GodFather/helpers/resources/pics/chutiya.jpg"
promote_pic = "./GodFather/helpers/resources/pics/promote.jpg"
demote_pic = "./GodFather/helpers/resources/pics/demote.jpg"
mute_pic = "./GodFather/helpers/resources/pics/mute.jpg"
ban_pic = "./GodFather/helpers/resources/pics/ban.jpg"


# channel
my_channel = Config.YOUR_CHANNEL or "GodFather_OP"
my_group = Config.YOUR_GROUP or "GodFather_AI"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

# My Channel
chnl_link = "https://t.me/GodFather_AI"
godfather_channel = f"[Lêɠêɳ̃dẞø† ]({chnl_link})"
grp_link = "https://t.me/GodFather_OP"
godfather_grp = f"[Lêɠêɳ̃dẞø† ]({grp_link})"


PM_START = []
PMMESSAGE_CACHE = {}
PMMENU = "pmpermit_menu" not in Config.NO_LOAD


TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY

# spamwatch support
if Config.SPAMWATCH_API:
    token = Config.SPAMWATCH_API
    spamwatch = spam_watch.Client(token)
else:
    spamwatch = None


# ================================================

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


# thumb image
if Config.THUMB_IMAGE is not None:
    check = url(Config.THUMB_IMAGE)
    if check:
        try:
            with open(thumb_image_path, "wb") as f:
                f.write(requests.get(Config.THUMB_IMAGE).content)
        except Exception as e:
            LOGS.info(str(e))


def set_key(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = value
    elif isinstance(dictionary[key], list):
        if value in dictionary[key]:
            return
        dictionary[key].append(value)
    else:
        dictionary[key] = [dictionary[key], value]


async def make_gif(event, reply, quality=None, fps=None):
    fps = fps or 1
    quality = quality or 256
    result_p = os.path.join("temp", "animation.gif")
    animation = lottie.parsers.tgs.parse_tgs(reply)
    with open(result_p, "wb") as result:
        await _godfatherutils.run_sync(
            lottie.exporters.gif.export_gif, animation, result, quality, fps
        )
    return result_p
