class Help:
    def __init__(self):
        commands = open('help.txt', 'r')
        if commands.mode == 'r':
            self.list = commands.read()
        assert self.list

    def display(self):
        return self.list