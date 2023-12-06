import pygame

class Rotor:
    def __init__(self, wiring, notches):
        self.FONT_SIZE = 25
        self.TEXT_COLOR = (110, 110, 110)
        self.PADDING = 30
        self.ACTION_RADIUS = 10
        
        self.ring = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring
        self.notches = notches

        self.x = 0
        self.y = 0

        self.font = pygame.font.Font("./res/fonts/typewriter.otf", self.FONT_SIZE)
        self.rotate_sound = pygame.mixer.Sound("./res/audio/rotor.wav")

    def input(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)

    def output(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)

    def rotate(self, n=1, forward=True, ring=True):
        for _ in range(n):
            if forward:
                self.left = self.left[1:] + self.left[0]
                self.right = self.right[1:] + self.right[0]

                if ring:
                    self.ring = self.ring[1:] + self.ring[0]
            else:
                self.left = self.left[-1] + self.left[:-1]
                self.right = self.right[-1] + self.right[:-1]

                if ring:
                    self.ring = self.ring[-1] + self.ring[:-1]
    
    def set_rotor(self, letter):
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n)

    def set_ring(self, letter):        
        n = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(letter)
        self.rotate(n, forward=False, ring=False)

        new_notches = ""

        for notch in self.notches:
            n_notch = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".find(notch)
            new_notches += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[(n_notch - n) % 26]
        
        self.notches = new_notches

    def set_xy(self, x, y):
        self.x = x
        self.y = y

    def update(self, mouse):
        if ((mouse[0] - self.x)**2 + (mouse[1] - self.y)**2)**0.5 <= self.ACTION_RADIUS:
            self.rotate(forward=False)
            self.rotate_sound.play()
        elif ((mouse[0] - self.x)**2 + (mouse[1] - (self.y + self.PADDING * 2))**2)**0.5 <= self.ACTION_RADIUS:
            self.rotate()
            self.rotate_sound.play()

    def draw(self, screen):
        previous = self.font.render(self.ring[-1], True, self.TEXT_COLOR)
        current = self.font.render(self.ring[0], True, self.TEXT_COLOR)
        next = self.font.render(self.ring[1], True, self.TEXT_COLOR)

        screen.blit(next, next.get_rect(center=(self.x, self.y)))
        screen.blit(current, current.get_rect(center=(self.x, self.y + self.PADDING)))
        screen.blit(previous, previous.get_rect(center=(self.x, self.y + self.PADDING * 2)))

ROTOR_I = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")
ROTOR_II = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E")
ROTOR_III = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
ROTOR_IV = Rotor("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J")
ROTOR_V = Rotor("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
ROTOR_VI = Rotor("JPGVOUMFYQBENHZRDKASXLICTW", "ZM")
ROTOR_VII = Rotor("NZJHGRCXMYSWBOUFAIVLPEKQDT", "ZM")
ROTOR_VIII = Rotor("FKQHTLXOCBJSPDZRAMEWNIUYGV", "ZM")