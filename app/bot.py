import secrets

from app.items import Rock, Paper, Scissors


class Bot:

    @staticmethod
    def choose():
        return secrets.choice(
            (Rock, Paper, Scissors)
        )()
