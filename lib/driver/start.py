from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.cmd("start"))
async def start(client, message):
    await message.reply("**👋 I'm alive**")
