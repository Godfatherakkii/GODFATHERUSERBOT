#    Credts @godfather_K_BOY
from geopy.geocoders import Nominatim
from telethon.tl import types

from GodFather import godfather

from ..core.managers import eor
from ..helpers import reply_id

menu_category = "extra"


@godfather.godfather_cmd(
    pattern="gps ([\s\S]*)",
    command=("gps", menu_category),
    info={
        "header": "To send the map of the given location.",
        "usage": "{tr}gps <place>",
        "examples": "{tr}gps Hyderabad",
    },
)
async def gps(event):
    "Map of the given location."
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    godfatherevent = await eor(event, "`finding.....`")
    geolocator = Nominatim(user_agent="godfatherUserBot")
    geoloc = geolocator.geocode(input_str)
    if geoloc:
        lon = geoloc.longitude
        lat = geoloc.latitude
        await event.client.send_file(
            event.chat_id,
            file=types.InputMediaGeoPoint(types.InputGeoPoint(lat, lon)),
            caption=f"**Location : **`{input_str}`",
            reply_to=reply_to_id,
        )
        await godfatherevent.delete()
    else:
        await godfatherevent.edit("`i coudn't find it`")
