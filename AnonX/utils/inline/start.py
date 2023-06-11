from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="✯ ᴍᴀᴋᴇ ᴍᴇ ʏᴏᴜʀ ɢғ ✯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="✯ sᴇᴛᴛɪɴɢs ✯",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="✯ ᴄᴏᴍᴍᴀɴᴅs ✯", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="✯ ᴜᴘᴅᴀᴛᴇs ᴄʜᴀɴɴᴇʟ ✯", url=f"https://t.me/NOOBXCREATOR"),
            InlineKeyboardButton(
                text="✯ sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ ✯", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = "https://t.me/pirokid"):
    buttons = [
        [
            InlineKeyboardButton(
                text="🔎 ʜᴏᴡ ᴛᴏ ᴜsᴇ? ᴄᴏᴍᴍᴀɴᴅs ᴍᴇɴᴜ", callback_data="settings_back_helper"   
            ),
        ],
        [
           InlineKeyboardButton(text="📨 ᴜᴘᴅᴀᴛᴇs", url=f"https://t.me/NOOBXCREATOR"),
            InlineKeyboardButton(
                text="📨 sᴜᴘᴘᴏʀᴛ", url=f"{config.SUPPORT_GROUP}"   
            ),
        ],
        [
            InlineKeyboardButton(
                text="💡 ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                    text="👤 ʙᴏᴛ ᴏᴡɴᴇʀ", url=f"https://t.me/pirokid"
                )
        ],
     ]
    return buttons
