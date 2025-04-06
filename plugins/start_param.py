from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start") & filters.private)
async def start_deeplink(client, message: Message):
    args = message.text.split(" ")
    if len(args) > 1:
        param = args[1]

        # Case: shortened param
        if param.startswith("notcopy_"):
            try:
                parts = param.split("_")
                file_id = "_".join(parts[-3:])  # Extract the final part like BAADBQA...
                chat_id = int("-100" + parts[2])  # Build full chat ID
                await client.send_cached_media(
                    chat_id=message.chat.id,
                    media=file_id
                )
                return
            except Exception as e:
                await message.reply_text("Failed to send the movie. Please try again.")
                return

        # Case: direct link
        if param.startswith("file_"):
            try:
                param = param.replace("file_", "")
                parts = param.split("_")
                chat_id = int(parts[0])
                file_id = "_".join(parts[1:])
                await client.send_cached_media(
                    chat_id=message.chat.id,
                    media=file_id
                )
                return
            except Exception as e:
                await message.reply_text("Movie not found or invalid link.")
                return

    await message.reply_text("Welcome to Movie Bot! Send me a valid link to get started.")
