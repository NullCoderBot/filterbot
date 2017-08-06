import logging

import os
from telegram.ext import Updater

from tg_bot.config import Development as Configuration

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

if os.environ.get('HEROKU', False):
    TOKEN = os.environ.get('TOKEN', None)
else:
    TOKEN = Configuration.API_KEY

updater = Updater(TOKEN)

dispatcher = updater.dispatcher