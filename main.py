from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Replace 'YOUR_TOKEN' with your actual bot token from BotFather
TOKEN = '7465723607:AAGw0JGtHxQrTTU9u4ivlSjgshr4I-ZvDcw'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This Bot won't work now.\n\nUse this Bot - @Shenhemusicbot instead.")

def play(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("This Bot won't work now.\n\nUse this Bot - @Shenhemusicbot instead.")

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    # Add handlers for /start and /play commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("play", play))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
  
