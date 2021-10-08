'''
tg-stream-video, An Telegram Bot Project
Copyright (c) 2021 GalihMrd <https://github.com/Imszy17>
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
'''

import asyncio
from datetime import datetime

from pyrogram import Client, filters
from pyrogram.types import Message

from lib.config import USERNAME_BOT
from lib.helpers.filters import public_filters

VIDEO_CALL = {}
PAUSE = {}
RESUME = {}


@Client.on_message(filters.command(["stop",
                                    "stop@{USERNAME_BOT}"]) & public_filters)
async def stopvideo(client, m: Message):
    chat_id = m.chat.id
    channel_id = m.chat.title
    flags = " ".join(m.command[1:])
    user = m.from_user.mention
    if flags == "channel":
        try:
            await VIDEO_CALL[channel_id].stop()
            await m.reply(f"**Channel Stream**\n**Stopped by {user}!**")
        except Exception as e:
            await m.reply(f"**Error:** {str(e)}")
    else:
        try:
            await VIDEO_CALL[chat_id].stop()
            await m.reply(f"**Stopped by {user}**")
        except Exception as e:
            await m.reply(f"{str(e)}")


@Client.on_message(filters.command(["ping", "ping@{USERNAME_BOT}"]))
async def ping_(client: Client, message: Message):
    start = datetime.now()
    msg = await message.reply_text('`Latensi`')
    end = datetime.now()
    latency = (end - start).microseconds / 1000
    await msg.edit(f"**Latency:** `{latency} ms`")


@Client.on_message(filters.command(["repo", "repo@{USERNAME_BOT}"]))
async def repo(client, message):
    repo = "https://github.com/galihmrd/tg-stream-video"
    await message.reply(f"**Source code:** [Here]({repo})")


@Client.on_message(filters.command(["schedule",
                                    "schedule@{USERNAME_BOT}"]) & public_filters)
async def sch(client, message):
    if len(message.command) >= 2:
        pass
    else:
        await message.reply("Please enter value in seconds")
        return
    chat_id = message.chat.id
    chid = message.chat.title
    user = message.from_user.mention
    input = message.command[1]
    txt = await message.reply(f"**Stopped in** `{input}s`")
    await asyncio.sleep(int(input))
    try:
        await txt.edit(f"**Stopped by {user}!**")
        await VIDEO_CALL[chat_id].stop()
    except Exception:
        return
    try:
        await CHANNEL_VIDEO[chid].stop()
    except Exception:
        pass


@Client.on_message(filters.command(["pause", "pause@{USERNAME_BOT}"]))
async def pause(client, message):
    chat_id = message.chat.id
    channel_id = message.chat.title
    flags = " ".join(message.command[1:])
    if flags == "channel":
        try:
            await PAUSE[channel_id].set_pause(True)
            await message.reply("**Pause Channel stream!**")
        except Exception as e:
            await message.reply(f"{str(e)}")
    else:
        try:
            await PAUSE[chat_id].set_pause(True)
            await message.reply("**Pause stream!**")
        except Exception as e:
            await message.reply(f"{str(e)}")


@Client.on_message(filters.command(["resume", "resume@{USERNAME_BOT}"]))
async def resume(client, message):
    chat_id = message.chat.id
    channel_id = message.chat.title
    flags = " ".join(message.command[1:])
    if flags == "channel":
        try:
            await RESUME[channel_id].set_pause(False)
            await message.reply("**Resume channel stream!**")
        except Exception as e:
            await message.reply(f"{str(e)}")
    else:
        try:
            await RESUME[chat_id].set_pause(False)
            await message.reply("**Resume stream!**")
        except Exception as e:
            await message.reply(f"{str(e)}")
