from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.cmd("start"))


from lib.config import USERNAME_BOT




async def start(client, message):
    await message.reply("**👋 I'm alive**")
