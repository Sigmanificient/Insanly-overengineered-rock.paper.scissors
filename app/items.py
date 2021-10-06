class Item:
    beat: str
    beaten: str

    @staticmethod
    def from_string(string):
        string = string.lower()

        if string in ['rock', 'r']:
            return Rock()

        if string in ['paper', 'p']:
            return Paper()

        if string in ['scissors', 's']:
            return Scissors()

    def __repr__(self):
        return self.__class__.__name__.lower()

    def __eq__(self, other):
        return self.beat == other.beat

    def __gt__(self, other):
        return self.beat == other.beaten

    def __lt__(self, other):
        return self.beaten == other.beat


class Rock(Item):
    beat = 's'
    beaten = 'p'


class Paper(Item):
    beat = 'r'
    beaten = 's'


class Scissors(Item):
    beat = 'p'
    beaten = 'r'
