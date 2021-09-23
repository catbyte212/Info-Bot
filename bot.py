# Made with Python3
# (C) Vivek-TP and FayasNoushad

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

Bot = Client(
        "Info Bot",
        bot_token = os.environ["BOT_TOKEN"],
        api_id = int(os.environ["API_ID"]),
        api_hash = os.environ["API_HASH"]
)

START_TEXT = """
<b>Hai Kak {}!</b>

Aku adalah Bot Telegram sederhana untuk menampilkan INFO, Ketik /help untuk melihat daftar perintah dan cara penggunaan.
"""
HELP_TEXT = """
🤔 Penggunaan?

• Forward Pesan untuk mengetahui **Detailnya** (secara Private)

• Kirim **Media** apapun untuk mengetahui **Detailnya** (secara private)

• Balas /info dari suatu Pesan untuk mengetahui **Detail Pesan**

• Gunakan perintah /info untuk mengetahui **Detail kamu**

• Gunakan /id di Group atau Channel untuk mendapatkan **Unique Telegram ID**
"""
ABOUT_TEXT = """
- **Bot :** `Info Bot`
- **Credits :** `Everyone in this journey`
- **Source :** [Click here](https://github.com/catbyte212/Info-Bot)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""

BOT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join Group", url=f"https://t.me/rumahbotindonesia")
        ]]
    )


START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(text="Join Group", url=f"https://t.me/rumahbotindonesia")
        ]]
    )
                
@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.mention) 
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("help"))
async def help(bot, update):
    text = HELP_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )


@Bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    text = ABOUT_TEXT
    reply_markup = START_BUTTONS
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("info"))
async def info(bot, update):
    if update.from_user.last_name:
        last_name = update.from_user.last_name
    else:
        last_name = "None"
    text = f"""
**🙋🏻‍♂️ Nama Depan :** {update.from_user.first_name}

**🧖‍♂️ Nama Belakang :** {last_name}

**🧑🏻‍🎓 Username :** {update.from_user.username}

**🆔 ID Telegram :** {update.from_user.id}

**🔗 Profile Link :** {update.from_user.mention}
""" 
    reply_markup = START_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

@Bot.on_message(filters.private & filters.command("id"))
async def id(bot, update):
    text = f"""
**ID Telegram :** {update.from_user.id}
"""
    reply_markup = START_BUTTONS
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=reply_markup
    )

print(
    """
Bot Started!!!
"""
)

Bot.run()
