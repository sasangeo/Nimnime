# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from pyrogram.types import InlineKeyboardButton

class Data:
    HELP = """
<b> ❏ Perintah untuk Pengguna BOT
 ├ /start - Mulai Bot
 ├ /about - Tentang Bot ini
 ├ /help - Bantuan Perintah Bot ini
 ├ /ping - Untuk mengecek bot hidup
 └ /uptime - Untuk melihat status bot 
 
 ❏ Perintah Untuk Admin BOT
 ├ /logs - Untuk melihat logs bot
 ├ /setvar - Untuk mengatur var dengan command dibot
 ├ /delvar - Untuk menghapus var dengan command dibot
 ├ /getvar - Untuk melihat salah satu var dengan command dibot
 ├ /users - Untuk melihat statistik pengguna bot
 ├ /batch - Untuk membuat link lebih dari satu file
 ├ /speedtest - Untuk Mengetes kecepatan server bot
 └ /broadcast - Untuk mengirim pesan broadcast ke pengguna bot.
 
 • Creator : @{}
 • Channel : <a href='https://t.me/Anime_Bahasa_Indonesia'>Klik Disini!</a>
 • Group : <a href='https://t.me/group_anime_indonesia'>Klik Disini!</a>
 • Meme Receh : <a href='https://t.me/Central_Dark_World'>Klik Disini!</a>
 
 
 </b>
"""

    close = [
        [InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")]
    ]

    mbuttons = [
        [
            InlineKeyboardButton("ʜᴇʟᴘ & ᴄᴏᴍᴍᴀɴᴅs", callback_data="help"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    buttons = [
        [
            InlineKeyboardButton("ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ", callback_data="about"),
            InlineKeyboardButton("ᴛᴜᴛᴜᴘ", callback_data="close")
        ],
    ]

    ABOUT = """
<b>Tentang Bot ini:

@{} adalah Bot Telegram untuk menyimpan File Anime yang dapat Diakses melalui Link Khusus.

 • Creator : @{}
 • Channel : <a href='https://t.me/Anime_Bahasa_Indonesia'>Klik Disini!</a>
 • Group : <a href='https://t.me/group_anime_indonesia'>Klik Disini!</a>
 • Meme Receh : <a href='https://t.me/Central_Dark_World'>Klik Disini!</a>

</b>
"""
