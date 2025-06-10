import logging
from telegram import Update, ForceReply
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = '6156367590:AAEIKn9oAM8r_1y41KdoanTJ8n49D0YBeB8'  # Replace with your bot's API token

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Command handler for /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hello {user.mention_html()}! 👋\n"
        "I'm Suzu, your friendly Telegram chatbot assistant.\n"
        "Type anything to chat with me!\n"
        "If you want to see the Python requirements file for deploying me, type /requirements."
    )

# Command handler for /requirements
async def requirements(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send the requirements.txt contents."""
    requirements_content = (
        "python-telegram-bot==20.7\n"
        "aiohttp\n"
        "certifi\n"
        "httpx\n"
    )
    await update.message.reply_text(
        "Here's the requirements file to run me:\n\n"
        "```text\n" + requirements_content + "\n```",
        parse_mode="Markdown",
    )

# Message handler for all text messages (the chatbot)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message as a friendly chatbot."""
    user_message = update.message.text
    # Example: simple chatbot response logic, could be replaced with AI/NLP
    if "hello" in user_message.lower():
        response = "Hello! 😊 How can I help you today?"
    elif "your name" in user_message.lower():
        response = "I'm Suzu, your smart Telegram assistant!"
    elif "requirement" in user_message.lower():
        response = "To see my requirements file, just type /requirements."
    else:
        response = f"You said: {user_message}\nHow can I assist you further?"
    await update.message.reply_text(response)

def main() -> None:
    """Run the bot."""
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("requirements", requirements))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling()

if __name__ == "__main__":
    main()