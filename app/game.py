from app import Cli
from app.bot import Bot
from app.items import Item


class Game:

    def __init__(self):
        self.is_running = False
        self.cli = Cli()

    def run(self):
        self.is_running = True

        while self.is_running:
            self.play_round()

    def play_round(self):
        action = self.cli.get_action()

        player_item = Item.from_string(action)
        bot_item = Bot.choose()

        self.resolve(player_item, bot_item)

    @staticmethod
    def resolve(player_item, bot_item):
        if player_item == bot_item:
            print("Tie!")
            return

        players = ("Bot", "Player")
        print(players[player_item > bot_item], "wins!")
