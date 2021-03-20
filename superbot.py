import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Toyota motors
bot = [
    {"context": "", "message": "car", "to_context": "car", "reply": "Which car do you want to buy? Camry or Corolla?"},
    {"context": "", "message": "air", "to_context": "airplane", "reply": "Which airplane do you want to buy? Boeing or Airbus?"},
    {"context": "car", "message": "Camr", "to_context": "buy_camry", "reply": "Camry costs $15000. And we have it in stock. Do you want to purchase it?"},
    {"context": "car", "message": "Coro", "to_context": "", "reply": "Corolla costs $12000"},
    {"context": "airplane", "message": "Airbus", "to_context": "", "reply": "Airbus costs $1 200 000"},
    {"context": "airplane", "message": "Boeing", "to_context": "", "reply": "Boeing costs $1 500 000"},
    {"context": "buy_camry", "message": "yes", "to_context": "buy_camry_cassa", "reply": "Great! Please enter your credit card number."},
    {"context": "buy_camry_cassa", "message": "", "to_context": "", "reply": "Purchased. Please wait at your door."},
]


class Client:
    def __init__(self,update):
        self.username = update.message.chat.username
        self.name = ""
        self.context = "ask_name"
        print("Found new user", self.username)


clients = dict()

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(stupid_bot(update))


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def stupid_bot(update):
    msg = update.message.text
    result = "I don't know"
    if update.message.chat.username not in clients:
        clients[update.message.chat.username] = Client(update)
        result = "Hello, new user! What is your name?"
    else:
        client = clients[update.message.chat.username]
        if client.context == "ask_name":
            client.name = msg
            print("Stored name: ", msg)
            client.context = ""
            result = f"Thanks for your name, {client.name}! What do you want to buy?"
        else:
            for command in bot:
                if command["context"] == client.context and command["message"].lower() in msg.lower():
                    client.context = command["to_context"]
                    result = command["reply"]
                    break

    if "how" in msg.lower() and "you" in msg.lower():
        return "Great! And you?"

    return result


def echo(update, context):
    """Echo the user message."""
    msg = update.message.text
    print(msg)
    print(update)
    update.message.reply_text(stupid_bot(update))


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("1795368391:AAE3FjNhf7JvBGqTx8HUwuvbkSF2oT_klmA", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
