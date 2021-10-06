class Cli:

    @classmethod
    def get_action(cls):
        return cls.input_while(
            'Action [r/p/s]:\n>>> ',
            'Please choose a valid action (r/p/s)',
            ('r', 'p', 's', 'rock', 'paper', 'scissors')
        )

    @staticmethod
    def input_while(prompt, error, values):
        value = input(prompt)

        while value not in values:
            print(error)
            value = input(prompt)

        return value
