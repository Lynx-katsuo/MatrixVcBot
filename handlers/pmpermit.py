from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Hi there, This is a music assistant service of @Heroic_Association .\n\n ❗️ Rules:\n   - No chatting allowed\n   - No spam allowed   - Don't add this bot to your group if your group isn't connected to Heroic Association \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n ⚠️ Disclamer: If you are sending a message here it means admin from @Heroic_Association will see your message and join chat\n    - Don't add this user to secret groups.\n   - Don't Share private info here\n\n **FEEL FREE TO CONTACT US @Zoro_Support_group**")
  return                        
