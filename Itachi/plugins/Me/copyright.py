from Itachi import app
from pyrogram import Client, filters

async def delete_links(message):
    if any(link in message.text for link in ["http", "https", "www."]):
        await message.delete()

keywords_to_delete = ["NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

@app.on_message(filters.group & filters.text & ~filters.me)
async def handle_messages(client, message):
    if any(keyword in message.text for keyword in keywords_to_delete) and len(message.text.split()) > 20:
        await message.delete()
    elif len(message.text.split()) >= 20:
        await message.delete()
    else:
        await delete_links(message)

@app.on_edited_message(filters.group & filters.text & ~filters.me)
async def handle_edited_messages(client, edited_message):
    if any(keyword in edited_message.text for keyword in keywords_to_delete) and len(edited_message.text.split()) > 20:
        await edited_message.delete()
    elif len(edited_message.text.split()) >= 20:
        await edited_message.delete()
    else:
        await delete_links(edited_message)