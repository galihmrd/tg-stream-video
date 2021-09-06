from pyrogram import Client, filters, idle
from lib.config import API_ID, API_HASH, BOT_TOKEN, PREFIXES
from lib.driver.stream import app

bot = Client(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="lib.driver"),
)

def filter_cmd(command, *args, **kwargs):
    prefixes = ''.join(PREFIXES)
    prefix = f"^[{re.escape(prefixes)}]"
    return filters.regex(prefix + command, *args, **kwargs)

filters.cmd = filter_cmd

bot.start()
app.start()
idle()
