class Keyboard:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def input(self, letter):
        return self.alphabet.find(letter)

    def output(self, signal):
        return self.alphabet[signal]