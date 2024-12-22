import asyncio
from pyrogram import Client
from BADMUSIC import app
from pyrogram.types import ChatMemberUpdated


# Event triggered when the bot is added to a group
@app.on_chat_member_updated()
async def on_bot_added(client: Client, chat_member_update: ChatMemberUpdated):
    # Check if the bot was added to the group
    if chat_member_update.new_chat_member and chat_member_update.new_chat_member.user.id == client.me.id:
        chat_id = chat_member_update.chat.id
        
        # Wait for 10 seconds before sending the command
        await asyncio.sleep(10)
        
        # Send the /userbotjoin command in the group
        await client.send_message(chat_id, "/userbotjoin")
