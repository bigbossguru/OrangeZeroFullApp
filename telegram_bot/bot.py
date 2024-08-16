import os
import logging
from pathlib import Path

import aiohttp
import telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from dotenv import load_dotenv


load_dotenv()

logs_dir_path = Path(__file__).parent / "logs"
logs_dir_path.mkdir(exist_ok=True)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.FileHandler(logs_dir_path / "telegabot.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)


async def fetch(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            return data


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Welcome to the Human being Telegram Bot!\n",
        parse_mode=telegram.constants.ParseMode.HTML,
    )


async def magic_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    urls_info = "Debug Mode"
    if not bool(os.environ["DEBUG"]):
        data = await fetch("http://localhost:4040/api/tunnels")
        urls_info = "\n".join(
            f"{url['name']}: {url['public_url']}" for url in data["tunnels"]
        )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=urls_info,
    )


if __name__ == "__main__":
    application = ApplicationBuilder().token(os.environ["TELEGRAM_BOT_TOKEN"]).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("url", magic_url))
    application.run_polling()
