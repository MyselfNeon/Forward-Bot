
import os
import re 
import sys
import asyncio 
import logging 
from database import Db, db
from config import Config, temp
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, Message 
from pyrogram.errors.exceptions.bad_request_400 import AccessTokenExpired, AccessTokenInvalid
from pyrogram.errors import FloodWait
from config import Config
from script import Script
from typing import Union, Optional, AsyncGenerator
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

BTN_URL_REGEX = re.compile(r"(\[([^\[]+?)]\[buttonurl:/{0,2}(.+?)(:same)?])")
BOT_TOKEN_TEXT = "<b><i>1) Create a Bot using @BotFather\n2) Then you will get a message with Bot token\n3) Forward that message to me</i></b>"
SESSION_STRING_SIZE = 351

class CLIENT: 
  def __init__(self):
     self.api_id = Config.API_ID
     self.api_hash = Config.API_HASH

  def user_session(self, data):
      return Client("USERBOT", self.api_id, self.api_hash, session_string=data)
     
  async def add_bot(self, bot, message):
     user_id = int(message.from_user.id)
     msg = await bot.ask(chat_id=user_id, text=BOT_TOKEN_TEXT)
     if msg.text=='/cancel':
        return await msg.reply('<b>__Process cancelled !__</b>')
     elif not msg.forward_date:
       return await msg.reply_text("<b>__This is not a forward message__</b>")
     elif str(msg.forward_from.id) != "93372553":
       return await msg.reply_text("<b>__This message was not forward from BotFather__</b>")
     bot_token = re.findall(r'\d[0-9]{8,10}:[0-9A-Za-z_-]{35}', msg.text, re.IGNORECASE)
     bot_token = bot_token[0] if bot_token else None
     if not bot_token:
       return await msg.reply_text("<b>__There is no Bot token in message__</b>")
     try:
       _client = Client("BOT", Config.API_ID, Config.API_HASH, bot_token=bot_token, in_memory=True)
       client = await _client.start()
     except Exception as e:
       await msg.reply_text(f"<b>BOT ERROR:</b> `{e}`")
       return
     _bot = _client.me
     details = {
       'id': _bot.id,
       'is_bot': True,
       'user_id': user_id,
       'name': _bot.first_name,
       'token': bot_token,
       'username': _bot.username 
     }
     await db.add_bot(details)
     return True

  async def add_session(self, bot, message):
     user_id = int(message.from_user.id)
     text = "<b>⚠️ DISCLAIMER ⚠️</b>\n\n<code>__you can use your session for forward message from private chat to another chat.\nPlease add your pyrogram session with your own risk. Their is a chance to ban your account. My developer is not responsible if your account may get banned.__</code>"
     await bot.send_message(user_id, text=text)
     phone_number_msg = await bot.ask(chat_id=user_id, text="<b>__Please send your phone number which includes country code__</b>\n<b>Example:</b> <code>+13124562345</code>")
     if phone_number_msg.text=='/cancel':
        return await phone_number_msg.reply('<b>__Process cancelled !__</b>')
     phone_number = phone_number_msg.text
     client = Client(":memory:", Config.API_ID, Config.API_HASH)
     await client.connect()
     await phone_number_msg.reply("__Sending OTP...__ 👀")
     try:
        code = await client.send_code(phone_number)
        phone_code_msg = await bot.ask(user_id, "**__Please check for an OTP in official telegram account. If you got it, send OTP here after reading the below format__**. \n\n**__If OTP is__** `12345`, **__please send it as__** `1 2 3 4 5`.\n\n**__Enter__ /cancel __to cancel The Procces__**", filters=filters.text, timeout=600)
     except PhoneNumberInvalid:
        await phone_number_msg.reply('`PHONE_NUMBER` **is invalid.**')
        return
     if phone_code_msg.text=='/cancel':
        return await phone_code_msg.reply('<b>__Process cancelled !__</b>')
     try:
        phone_code = phone_code_msg.text.replace(" ", "")
        await client.sign_in(phone_number, code.phone_code_hash, phone_code)
     except PhoneCodeInvalid:
        await phone_code_msg.reply('**OTP __is invalid.__**')
        return
     except PhoneCodeExpired:
        await phone_code_msg.reply('**OTP __is expired__.**')
        return
     except SessionPasswordNeeded:
        two_step_msg = await bot.ask(user_id, '**__Your account has enabled two-step verification. Please provide the password.\n\nEnter__ /cancel __to cancel The Procces__**', filters=filters.text, timeout=300)
        if two_step_msg.text=='/cancel':
            return await two_step_msg.reply('<b>__Process cancelled !__</b>')
        try:
           password = two_step_msg.text
           await client.check_password(password=password)
        except PasswordHashInvalid:
           await two_step_msg.reply('**__Invalid Password Provided__**')
           return
     string_session = await client.export_session_string()
     await client.disconnect()
     if len(string_session) < SESSION_STRING_SIZE:
        return await msg.reply('<b>__invalid session sring__</b>')
     try:
       _client = Client("USERBOT", self.api_id, self.api_hash, session_string=string_session)
       client = await _client.start()
     except Exception as e:
       return await msg.reply_text(f"<b>USER BOT ERROR:</b> `{e}`")
     user = _client.me
     details = {
       'id': user.id,
       'is_bot': False,
       'user_id': user_id,
       'name': user.first_name,
       'session': string_session,
       'username': user.username
     }
     await db.add_userbot(details)
     return True

@Client.on_message(filters.private & filters.command('reset'))
async def forward_tag(bot, m):
   default = await db.get_configs("01")
   await db.update_configs(m.from_user.id, default)
   await m.reply("__Successfully settings Reseted ✔️__")

@Client.on_message(filters.command('resetall') & filters.user(Config.BOT_OWNER))
async def resetall(bot, message):
  users = await db.get_all_users()
  sts = await message.reply("**__Processing__**")
  TEXT = "total: {}\nsuccess: {}\nfailed: {}\nexcept: {}"
  total = success = failed = already = 0
  ERRORS = []
  async for user in users:
      user_id = user['id']
      default = await get_configs(user_id)
      default['db_uri'] = None
      total += 1
      if total %10 == 0:
         await sts.edit(TEXT.format(total, success, failed, already))
      try: 
         await db.update_configs(user_id, default)
         success += 1
      except Exception as e:
         ERRORS.append(e)
         failed += 1
  if ERRORS:
     await message.reply(ERRORS[:100])
  await sts.edit("completed\n" + TEXT.format(total, success, failed, already))


async def get_configs(user_id):
  configs = await db.get_configs(user_id)
  return configs

async def update_configs(user_id, key, value):
  current = await db.get_configs(user_id)
  if key in ['caption', 'duplicate', 'db_uri', 'forward_tag', 'protect', 'min_size', 'max_size', 'extension', 'keywords', 'button']:
     current[key] = value
  else: 
     current['filters'][key] = value
  await db.update_configs(user_id, current)

async def iter_messages(
    self,
    chat_id: Union[int, str],
    limit: int,
    offset: int = 0,
    filters: dict = None,
    max_size: int = None,
) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        dup_files = []
        while True:
            new_diff = min(200, limit - current)
            if new_diff <= 0:
                return

            messages = await self.get_messages(chat_id, list(range(current, current + new_diff + 1)))
            for message in messages:
                if any(getattr(message, media_type, False) for media_type in filters):
                    yield "FILTERED"
                else:
                    yield message
                    
                current += 1

async def get_client(bot_token, is_bot=True):
  if is_bot:
    return Client("BOT", Config.API_ID, Config.API_HASH, bot_token=bot_token, in_memory=True)
  else:
    return Client("USERBOT", Config.API_ID, Config.API_HASH, session_string=bot_token)

def parse_buttons(text, markup=True):
    buttons = []
    for match in BTN_URL_REGEX.finditer(text):
        n_escapes = 0
        to_check = match.start(1) - 1
        while to_check > 0 and text[to_check] == "\\":
            n_escapes += 1
            to_check -= 1

        if n_escapes % 2 == 0:
            if bool(match.group(4)) and buttons:
                buttons[-1].append(InlineKeyboardButton(
                    text=match.group(2),
                    url=match.group(3).replace(" ", "")))
            else:
                buttons.append([InlineKeyboardButton(
                    text=match.group(2),
                    url=match.group(3).replace(" ", ""))])
    if markup and buttons:
       buttons = InlineKeyboardMarkup(buttons)
    return buttons if buttons else None

# Don't Remove Credit @MyselfNeon
