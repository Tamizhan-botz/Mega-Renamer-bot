"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
	Daily  Upload limit 1.2GB
	Price 0
	
	**🥉 Bʀᴏɴᴢᴇ  Tier 🥉** 
	Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 𝟷𝟶GB
    Pʀɪᴄᴇ Rs 15  ɪɴᴅ /🌎 𝟶.𝟼$  ᴘᴇʀ Mᴏɴᴛʜ
	
	**🥈 Sɪʟᴠᴇʀ Tier 🥈**
	Dᴀɪʟʏ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟻𝟶GB
   Pʀɪᴄᴇ Rs 35  ɪɴᴅ /🌎 𝟶.𝟿$  ᴘᴇʀ Mᴏɴᴛʜ
	
	**🥇 Gᴏʟᴅ Tɪᴇʀ 🥇**
	Dᴀɪʟʏ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟷𝟶𝟶GB
   Pʀɪᴄᴇ Rs 60  ɪɴᴅ /🌎 𝟷.𝟺$  ᴘᴇʀ Mᴏɴᴛʜ
	
	After Payment Send Screenshots Of 
        Payment To Admin @praxxsh"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("📞 ADMIN 📞",url = "https://t.me/Praxxsh")], 
        			[InlineKeyboardButton("❌ Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	Daily  Upload limit 2GB
	Price 0
	
	**🥉 Bʀᴏɴᴢᴇ Tier 🥉** 
	Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 𝟷𝟶GB
   Pʀɪᴄᴇ Rs 15  ɪɴᴅ /🌎 𝟶.𝟼$  ᴘᴇʀ Mᴏɴᴛʜ
	
	**🥈 Sɪʟᴠᴇʀ Tier 🥈**
	 Dᴀɪʟʏ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟻𝟶GB
   Pʀɪᴄᴇ Rs 35  ɪɴᴅ /🌎 𝟶.𝟿$  ᴘᴇʀ Mᴏɴᴛʜ
	
	**🥇 Gᴏʟᴅ Tɪᴇʀ 🥇**
	Dᴀɪʟʏ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟷𝟶𝟶GB
   Pʀɪᴄᴇ Rs 60  ɪɴᴅ /🌎 𝟷.𝟺$  ᴘᴇʀ Mᴏɴᴛʜ
	
	
	After Payment Send Screenshots Of 
        Payment To Admin @Praxxsh"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("📞 ADMIN 📞",url = "https://t.me/praxxsh")], 
        			[InlineKeyboardButton("❌Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
