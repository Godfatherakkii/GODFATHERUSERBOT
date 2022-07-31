import sys

from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
from telethon.sessions import StringSession

from ..Config import Config
from .client import godfatherClient

__version__ = "1.10.6"

loop = None

if Config.GODFATHERBOT_STRING:
    session = StringSession(str(Config.GODFATHERBOT_STRING))
else:
    session = "godfatherUserBot"

try:
    godfather = godfatherClient(
        session=session,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        loop=loop,
        app_version=__version__,
        connection=ConnectionTcpAbridged,
        auto_reconnect=True,
        connection_retries=None,
    )
except Exception as e:
    print(f"GODFATHERBOT_STRING - {e}")
    sys.exit()

godfather.tgbot = tgbot = godfatherClient(
    session="godfatherTgbot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    loop=loop,
    app_version=__version__,
    connection=ConnectionTcpAbridged,
    auto_reconnect=True,
    connection_retries=None,
).start(bot_token=Config.BOT_TOKEN)
