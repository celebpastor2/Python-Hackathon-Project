from django.core.management.base import BaseCommand
from telegram_bot.bot import main

class Command(BaseCommand) :
    def handle(self, *args, **kwargs) :
        main()

