from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start") & filters.private)
async def start_with_param(client, message: Message):
    args = message.text.split(" ")
    
    if len(args) > 1:
        param = args[1]
        # TODO: Lookup your file or link by `param`
        # Example: send a dummy file or link
        await message.reply_text(f"You requested: `{param}`\nProcessing your movie...")

        # Example: Send a file from local (optional)
        # await message.reply_document(document=f"downloads/{param}.mp4")

    else:
        await message.reply_text("Hey! Send me a valid deep link to receive your movie.")
