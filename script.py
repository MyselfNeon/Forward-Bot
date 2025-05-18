import os
from config import Config

class  Script(object):
  START_TXT = """<b><i>Hello</i> {}\n\n<i>I am Advanced Forward Bot.\nDeveloped by <a href='https://t.me/MyselfNeon'>NeonAnurag</a>.\n\nI can Forward all Messages from one Channel to another Channel !</i></b>"""
  HELP_TXT = """<u>⁉️ **HELP** ⁉️</u>

<u>**AVAILABLE COMMANDS 🖱️**</u>
<b>\n⏣ __/start - Check I'm Alive__ 
⏣ __/forward - Forward Messages__
⏣ __/settings - Configure your Settings__
⏣ __ /unequify - Delete duplicate Media messages in Chats__
⏣ __ /stop - Stop your Ongoing tasks__
⏣ __ /reset - Reset your Settings__</b>

<b><u>💢 FEATURES 💢</b></u>
<b>\n⪼ __Forward message from Public channel to your channel without Admin permission.\nIf the channel is private need Admin permission, if you can't give Admin permission then use Userbot, but in Userbot there is a chance to get your Account Ban so use fake Account__
⪼ __Custom Caption__
⪼ __Custom Button__
⪼ __Skip Duplicate Messages__
⪼ __Filter type of Messages__</b>
"""
  
  HOW_USE_TXT = """<b><u>BEFORE FORWARDING ⚠️</b></u>
<b>⪼ __Add a Bot or Userbot__
⪼ __Sdd atleast One to channel__ `(your bot/userbot must be admin in there)`
⪼ __You can add chats or bots by using /settings__
⪼ __If the **From Channel** is private your Userbot must be member in there or your Bot must need Admin permission in there also__
⪼ __Then use /forward to Forward messages__</b>"""
  
  ABOUT_TXT = """<b>
╔════❰ Fᴏʀᴡᴀʀᴅ Bᴏᴛ ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖 Bᴏᴛ : [Fᴏʀᴡᴀᴅ Bᴏᴛ](https://t.me/VJForwardBot)
║┣⪼👨‍💻 Cʀᴇᴀᴛᴏʀ : [Kɪɴɢ VJ 👑](https://t.me/kingvj01)
║┣⪼📢 Uᴘᴅᴀᴛᴇ : [VJ Bᴏᴛ](https://t.me/vj_botz)
║┣⪼🚀 Hᴏsᴛᴇᴅ Oɴ : [Hᴇʀᴏᴋᴜ](https://heroku.com)
║┣⪼📝 Lᴀɴɢᴜᴀɢᴇ : Pʏᴛʜᴏɴ3
║┣⪼📚 Lɪʙʀᴀʀʏ : Pʏʀᴏɢʀᴀᴍ 2.11.0 
║┣⪼🗒️ Vᴇʀsɪᴏɴ : 0.18.3
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
</b>"""
  STATUS_TXT = """
╔════❰ ʙᴏᴛ sᴛᴀᴛᴜs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼**⏳ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ:**`{}`
║┃
║┣⪼**👱 Tᴏᴛᴀʟ Usᴇʀs:** `{}`
║┃
║┣⪼**🤖 Tᴏᴛᴀʟ Bᴏᴛ:** `{}`
║┃
║┣⪼**🔃 Fᴏʀᴡᴀʀᴅɪɴɢs:** `{}`
║┃
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱❁۪۪
"""
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - cancel this process</b>"
  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
  SKIP_MSG = "<b>❪ SET MESSAGE SKIPING NUMBER ❫</b>\n\n<b>Skip the message as much as you enter the number and the rest of the message will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 message skiped\n You enter 5 = 5 message skiped</code>\n/cancel <b>- cancel this process</b>"
  CANCEL = "<b>Process Cancelled Succefully !</b>"
  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """
╔════❰ ғᴏʀᴡᴀʀᴅ sᴛᴀᴛᴜs  ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼<b>🕵 ғᴇᴄʜᴇᴅ Msɢ :</b> <code>{}</code>
║┃
║┣⪼<b>✅ sᴜᴄᴄᴇғᴜʟʟʏ Fᴡᴅ :</b> <code>{}</code>
║┃
║┣⪼<b>👥 ᴅᴜᴘʟɪᴄᴀᴛᴇ Msɢ :</b> <code>{}</code>
║┃
║┣⪼<b>🗑 ᴅᴇʟᴇᴛᴇᴅ Msɢ :</b> <code>{}</code>
║┃
║┣⪼<b>🪆 Sᴋɪᴘᴘᴇᴅ Msɢ :</b> <code>{}</code>
║┃
║┣⪼<b>🔁 Fɪʟᴛᴇʀᴇᴅ Msɢ :</b> <code>{}</code>
║┃
║┣⪼<b>📊 Cᴜʀʀᴇɴᴛ Sᴛᴀᴛᴜs:</b> <code>{}</code>
║┃
║┣⪼<b>𖨠 Pᴇʀᴄᴇɴᴛᴀɢᴇ:</b> <code>{}</code> %
║╰━━━━━━━━━━━━━━━➣ 
╚════❰ {} ❱══❍⊱❁۪۪
"""
  DUPLICATE_TEXT = """
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱═❍⊱❁۪۪
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ {} ❱══❍⊱❁۪۪
"""
  DOUBLE_CHECK = """<b><u>DOUBLE CHECKING ⚠️</b></u>
<code>Before forwarding the messages Click the Yes button only after checking the following</code>

<b>★ YOUR BOT:</b> [{botname}](t.me/{botuname})
<b>★ FROM CHANNEL:</b> `{from_chat}`
<b>★ TO CHANNEL:</b> `{to_chat}`
<b>★ SKIP MESSAGES:</b> `{skip}`

<i>° [{botname}](t.me/{botuname}) must be admin in **TARGET CHAT**</i> (`{to_chat}`)
<i>° If the **SOURCE CHAT** is private your userbot must be member or your bot must be admin in there also</b></i>

<b>If the above is checked then the yes button can be clicked</b>"""
  
SETTINGS_TXT = """<b>change your settings as your wish</b>"""
