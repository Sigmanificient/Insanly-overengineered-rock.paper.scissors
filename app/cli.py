from app.items import Item
from app.bot import Bot


class Cli:
    is_running = True

    @classmethod
    def get_action(cls):
        return input('Action:\n> ')

