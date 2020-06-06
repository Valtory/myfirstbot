#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Hi! I'm Val. This is a simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('holi holi')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def dan(update, context):
    if "DaugherName" in update.message.text.casefold():
        update.message.reply_text("ohh si, es una genia!! que nena tan talentosa con sus dibujos no?")
    elif "como estas"in update.message.text.casefold():
        update.message.reply_text("bien, vos?")
    elif "SonName"in update.message.text.casefold():
        update.message.reply_text("querras decir SonName? ja! ese niño es un peligro, casi hackea mi cerebro!")
    elif "bueno"in update.message.text.casefold():
        update.message.reply_text("bueno bueno, queres preguntarme algo mas?")
    elif "mami" in update.message.text.casefold():
        update.message.reply_text("ohh ella tambien es mi mami, ella me creo :3. Tambien cuida de mis pequeños archivos virtuales :)")
    elif "chiste" in update.message.text.casefold():
        update.message.reply_text("soy muy malo para contar chistes xD, pero que le dijo un bot a otro bot? jajaja le dijo 1010010100010101001 --- aah jajaja, es gracioso no?")
    elif "gracias" in update.message.text.casefold():
        update.message.reply_text("de nada :)")
    elif "no" in update.message.text.casefold():
        update.message.reply_text("ufaaaa :c , que dificil que es leer un no")
    elif "chau" in update.message.text.casefold():
        update.message.reply_text("ufa :c , chau!")
    elif "si" in update.message.text.casefold():
        update.message.reply_text(":D")
    elif "jaja" in update.message.text.casefold():
        update.message.reply_text("jajaja (khe, no entiendo)")
    else:
        update.message.reply_text("hey no intentes romper mi cerebro, estoy aprendiendo, soy solo un pobre bot")


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    
    updater = Updater("TOKEN", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    
    dp.add_handler(MessageHandler(Filters.text, dan))

    #dp.add_handler(conv_handler)

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
    
