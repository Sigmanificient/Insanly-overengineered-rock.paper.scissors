import colorama
from termcolor import colored

colorama.init()


class Cli:
    INPUT_LINE = colored('\n>>> ', 'magenta')

    @classmethod
    def get_action(cls):
        return cls.input_while(
            'Action [r/p/s]:',
            'Please choose a valid action (r/p/s)',
            ('r', 'p', 's', 'rock', 'paper', 'scissors')
        )

    @classmethod
    def input_while(cls, prompt, error, values):
        value = input(colored(prompt, 'blue') + cls.INPUT_LINE)

        while value not in values:
            print(colored(error, 'red') + cls.INPUT_LINE)
            value = input(colored(prompt, 'blue'))

        return value
