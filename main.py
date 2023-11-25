import pygame

pygame.init()

from Enigma import Enigma
from Rotor import *
from Reflector import *

WINDOW_SIZE = (700, 600)
FPS = 60

def main():
    screen = pygame.display.set_mode(WINDOW_SIZE)
    done = False
    key_pressed = -1

    #Enigma
    ENIGMA = Enigma(REFLECTOR_B, ROTOR_VIII, ROTOR_III, ROTOR_VI)
    ENIGMA.set_rotors_xy(WINDOW_SIZE)
    ENIGMA.set_rings("NIK")

    pygame.display.set_caption("ENIGMA Machine")

    while not done:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if key_pressed == -1 and event.key >= ord('a') and event.key <= ord('z'):
                    letter = chr(event.key - (ord('a') - ord('A')))
                    key_pressed = ENIGMA.encypher(letter)
            elif event.type == pygame.KEYUP:
                if key_pressed != -1:
                    key_pressed = -1
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == pygame.BUTTON_LEFT:
                ENIGMA.update(event.pos)

        screen.fill((0, 0, 0))

        ENIGMA.draw(screen, key_pressed)

        pygame.display.flip()

if __name__ == "__main__":
    main()