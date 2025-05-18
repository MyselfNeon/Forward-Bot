import os
from config import Config

class  Script(object):
  START_TXT = """<b><i>Hello</i> {}\n\n<i>I am Advanced Forward Bot.\nDeveloped by <a href='https://t.me/MyselfNeon'>NeonAnurag</a>.\n\nI can Forward all Messages from one Channel to another Channel !</i></b>"""
  HELP_TXT = """<u>⁉️ **HELP** ⁉️</u>

<u>** __AVAILABLE COMMANDS__ ⚡**</u>
<b>\n⏣ __/start - Check I'm Alive__ 
⏣ __/forward - Forward Messages__
⏣ __/settings - Configure your Settings__
⏣ __ /unequify - Delete duplicate Media messages in Chats__
⏣ __ /stop - Stop your Ongoing tasks__
⏣ __ /reset - Reset your Settings__</b>

<b><u> __FEATURES__ 🎊</b></u>
<b>\n⪼ __Forward message from Public channel to your channel without Admin permission.\nIf the channel is private need Admin permission, if you can't give Admin permission then use Userbot, but in Userbot there is a chance to get your Account Ban so use fake Account__
⪼ __Custom Caption__
⪼ __Custom Button__
⪼ __Skip Duplicate Messages__
⪼ __Filter type of Messages__</b>
"""
  
  HOW_USE_TXT = """<b><u>__BEFORE FORWARDING__ ‼️</b></u>
<b>\n⪼ __Add a Bot or Userbot__
⪼ __Sdd atleast One to channel__ `(__your bot/userbot must be admin in there__)`
⪼ __You can add chats or bots by using /settings__
⪼ __If the **From Channel** is private your Userbot must be member in there or your Bot must need Admin permission in there also__
⪼ __Then use /forward to Forward messages__</b>"""
  
  ABOUT_TXT = """<b>
╭━━━━━━━━━━━━━━━➣
┣⪼🤖 Bᴏᴛ : <a href=https://t.me/ForwardKsBot><b><i>ForwardKsBot</i></b></a>
┣⪼👨‍💻 Cʀᴇᴀᴛᴏʀ : <a href=https://t.me/MyselfNeon><b><i>MyselfNeon</i></b></a>
┣⪼📢 Uᴘᴅᴀᴛᴇ : [NeonFiles](https://t.me/neonfiles)
┣⪼🚀 Hᴏsᴛᴇᴅ Oɴ : [Heroku](https://heroku.com)
┣⪼📝 Lᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org><b><i>Python 3</i></b></a>
┣⪼📚 Lɪʙʀᴀʀʏ : Pyrogram 2.11.0 
┣⪼🗒️ Vᴇʀsɪᴏɴ : 0.18.3
╰━━━━━━━━━━━━━━━➣
</b>"""
  STATUS_TXT = """
  °• ❰ **Bᴏᴛ Sᴛᴀᴛᴜs** ❱ •°
╭━━━━━━━━━━━━━━━➣
┣⪼**⏳ Bᴏᴛ Uᴘᴛɪᴍᴇ:**`{}`
┃
┣⪼**👱 Tᴏᴛᴀʟ Usᴇʀs:** `{}`
┃
┣⪼**🤖 Tᴏᴛᴀʟ Bᴏᴛ:** `{}`
┃
┣⪼**🔃 Fᴏʀᴡᴀʀᴅɪɴɢs:** `{}`
╰━━━━━━━━━━━━━━━➣
"""
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"
  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
  SKIP_MSG = "<b>❪ SET MESSAGE SKIPING NUMBER ❫</b>\n\n<b>Skip the message as much as you enter the number and the rest of the message will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 message skiped\n You enter 5 = 5 message skiped</code>\n/cancel <b>- cancel this process</b>"
  CANCEL = "<b>Process Cancelled Succefully !</b>"
  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """
  °• ❰ **Fᴏʀᴡᴀʀᴅ Sᴛᴀᴛᴜs** ❱ •°
╭━━━━━━━━━━━━━━━➣
┣⪼<b>🕵 Fᴇᴄʜᴇᴅ Msɢ :</b> <code>{}</code>
┃
┣⪼<b>✅ Sᴜᴄᴄᴇғᴜʟʟʏ Fᴡᴅ :</b> <code>{}</code>
┃
┣⪼<b>👥 Dᴜᴘʟɪᴄᴀᴛᴇ Msɢ :</b> <code>{}</code>
┃
┣⪼<b>🗑 Dᴇʟᴇᴛᴇᴅ Msɢ :</b> <code>{}</code>
┃
┣⪼<b>🪆 Sᴋɪᴘᴘᴇᴅ Msɢ :</b> <code>{}</code>
┃
┣⪼<b>🔁 Fɪʟᴛᴇʀᴇᴅ Msɢ :</b> <code>{}</code>
┃
┣⪼<b>📊 Cᴜʀʀᴇɴᴛ Sᴛᴀᴛᴜs:</b> <code>{}</code>
┃
┣⪼<b>𖨠 Pᴇʀᴄᴇɴᴛᴀɢᴇ:</b> <code>{}</code> %
╰━━━━━━━━━━━━━━━➣ 
"""
  DUPLICATE_TEXT = """
  °• ❰ **Uɴᴇǫᴜɪғʏ Sᴛᴀᴛᴜs** ❱ •°
╭━━━━━━━━━━━━━━━➣
┣⪼ <b>Fᴇᴛᴄʜᴇᴅ Fɪʟᴇs:</b> <code>{}</code>
┃
┣⪼ <b>Dᴜᴘʟɪᴄᴀᴛᴇ Dᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
╰━━━━━━━━━━━━━━━➣
"""
  DOUBLE_CHECK = """<b><u>__DOUBLE CHECKING__ 🫡</b></u>
<code>Before forwarding the messages Click the Yes button only after checking the following</code>

<b>★ YOUR BOT:</b> [{botname}](t.me/{botuname})
<b>★ FROM CHANNEL:</b> `{from_chat}`
<b>★ TO CHANNEL:</b> `{to_chat}`
<b>★ SKIP MESSAGES:</b> `{skip}`

<i>° [{botname}](t.me/{botuname}) must be Admin in **TARGET CHAT**</i> (`{to_chat}`)
<i>° If the **SOURCE CHAT** is private your Userbot must be member or your Bot must be Admin in there also</b></i>

<b>If the above is checked then the YES button can be clicked</b>"""
  
SETTINGS_TXT = """<b>Change your Settings as your Wish</b>"""
