from Keyboard import Keyboard
from Plugboard import Plugboard
from Lampboard import Lampboard

class Enigma:
    def __init__(self, reflector, left_rotor, central_rotor, right_rotor):
        self.keyboard = Keyboard()
        self.plugboard = Plugboard()
        self.reflector = reflector
        self.left_rotor = left_rotor
        self.central_rotor = central_rotor
        self.right_rotor = right_rotor
        self.lampboard = Lampboard()

    def set_rings(self, rings):
        self.left_rotor.set_ring(rings[0])
        self.central_rotor.set_ring(rings[1])
        self.right_rotor.set_ring(rings[2])

    def encypher(self, letter):
        if self.central_rotor.left[0] in self.central_rotor.notches and self.right_rotor.left[0] in self.right_rotor.notches:
            self.right_rotor.rotate()
            self.central_rotor.rotate()
            self.left_rotor.rotate()
        elif self.central_rotor.left[0] in self.central_rotor.notches:
            self.right_rotor.rotate()
            self.central_rotor.rotate()
            self.left_rotor.rotate()
        elif self.right_rotor.left[0] in self.right_rotor.notches:
            self.right_rotor.rotate()
            self.central_rotor.rotate()
        else:
            self.right_rotor.rotate()

        signal = self.keyboard.input(letter)
        signal = self.plugboard.input(signal)
        signal = self.right_rotor.input(signal)
        signal = self.central_rotor.input(signal)
        signal = self.left_rotor.input(signal)
        signal = self.reflector.reflect(signal)
        signal = self.left_rotor.output(signal)
        signal = self.central_rotor.output(signal)
        signal = self.right_rotor.output(signal)
        signal = self.plugboard.output(signal)
        letter = self.keyboard.output(signal)

        return letter
    
    def set_rotors_xy(self, window_size):
        self.left_rotor.set_xy(window_size[0] // 2 - 30, 30)
        self.central_rotor.set_xy(window_size[0] // 2, 30)
        self.right_rotor.set_xy(window_size[0] // 2 + 30, 30)

    def update(self, mouse):
        self.left_rotor.update(mouse)
        self.central_rotor.update(mouse)
        self.right_rotor.update(mouse)
        self.plugboard.update(mouse)

    def draw(self, screen, light):
        self.left_rotor.draw(screen)
        self.central_rotor.draw(screen)
        self.right_rotor.draw(screen)
        self.lampboard.draw(screen, light)
        self.plugboard.draw(screen)