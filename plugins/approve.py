from pyrogram import Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserIsBlocked, PeerIdInvalid


@Client.on_chat_join_request()
async def accept_request(client, r):

    rm = InlineKeyboardMarkup([[
        InlineKeyboardButton("❤️‍🔥 DevilServers ❤️‍🔥", url=f"https://t.me/DevilServers"),
        InlineKeyboardButton("⚡DevilServers ⚡", url=f"https://t.me/DevilServers")
    ]])
    
    try:
        await client.send_photo(
            r.from_user.id,
            'https://te.legra.ph/file/94bc067909902a02eaf20.jpg',
            f"**𝖧𝖾𝗅𝗅𝗈 {r.from_user.mention} 👻, 𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝖳𝗈 {r.chat.title}\n𝖸𝗈𝗎𝗋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 𝖧𝖺𝗌 𝖡𝖾𝖾𝗇 𝖠𝗉𝗉𝗋𝗈𝗏𝖾𝖽...!!!**",
            reply_markup=rm)

    except UserIsBlocked:
        print("User blocked the bot")
    except PeerIdInvalid:
        print("Err")
    except Exception as e:
        print(f"#Error\n{str(e)}")

    await r.approve()
