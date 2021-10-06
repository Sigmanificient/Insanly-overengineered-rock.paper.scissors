from app.items import Item


class Cli:
    is_running = True

    @classmethod
    def run(cls):
        while cls.is_running:
            action = input('Action:\n> ')
            print(Item.from_string(action))
