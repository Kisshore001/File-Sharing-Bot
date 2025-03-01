#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>👨‍💻 Developer : <a href='https://t.me/Satorux_Gojo'>Satoru Gojo</a>\n📑 Language : <a href='https://python.org/'>Python3</a>\n📚 Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n🌐 Server : <a href='https://heroku.com/'>Heroku</a>\n📣 Channel : <a href='https://t.me/+DAa8VkOygMdhZWRl'>Anime in Tamil</a>\n🏅Owner : <a href='https://t.me/Mrsasuke07'>Mr Sasuke</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
