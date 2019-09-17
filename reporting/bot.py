#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple Bot to reply to Telegram messages.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logger = logging.getLogger(__name__)


class Bot:
    def __init__(self):

        self.context = None
        self.last_status = None
        self.last_screen = None
        self.chat_id = None

        """Start the bot."""
        # Create the Updater and pass it your bot's token.
        # Make sure to set use_context=True to use the new context based callbacks
        # Post version 12 this will no longer be necessary
        self.updater = Updater("903430086:AAFZuKG0QMh1sxRclGkMgZIuC2y7wHlOwTM", use_context=True)

        # Get the dispatcher to register handlers
        self.dp = self.updater.dispatcher

        # on different commands - answer in Telegram
        self.dp.add_handler(CommandHandler("status", self._status))
        self.dp.add_handler(CommandHandler("subscribe", self._subscribe))
        self.dp.add_handler(CommandHandler("unsubscribe", self._unsubscribe))

        # on noncommand i.e message - echo the message on Telegram
        self.dp.add_handler(MessageHandler(Filters.text, self.echo))

        # log all errors
        self.dp.add_error_handler(self.error)

        # Start the Bot
        self.updater.start_polling()

    def new_status(self, data, image):
        self.last_status = data
        self.last_screen = image
        if self.context:
            self.context.bot.send_photo(chat_id=self.chat_id,
                                        photo=open(self.last_screen, 'rb'),
                                        caption=f'{data}')

    def _subscribe(self, update, context):
        self.context = context
        self.chat_id = update.message.chat_id
        update.message.reply_text('Will keep you posted...')

    def _unsubscribe(self, update, context):
        self.context = None
        update.message.reply_text('Bye!')

    def _status(self, update, context):
        if self.last_screen:
            update.message.reply_photo(photo=open(self.last_screen, 'rb'), caption=f'{self.last_status}')

    def echo(self, update, context):
        """Echo the user message."""
        update.message.reply_text(update.message.text)

    def error(self, update, context):
        """Log Errors caused by Updates."""
        logger.warning('Update "%s" caused error "%s"', update, context.error)

    def wait(self):
        self.updater.idle()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.updater.stop()


if __name__ == '__main__':
    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    Bot().wait()
