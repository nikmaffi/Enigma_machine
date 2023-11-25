import pygame

class Lampboard:
    def __init__(self):
        self.LAMP_RADIUS = 25
        self.ROW_1_LAMPS = 9
        self.ROW_2_LAMPS = 8
        self.ROW_3_LAMPS = 9
        self.SPACE = (75, 130)
        self.PADDING = 10
        self.FONT_SIZE = 30
        self.TEXT_COLOR = (0, 0, 0)
        self.LAMP_COLOR_OFF = (50, 50, 50)
        self.LAMP_COLOR_ON = (255, 230, 0)

        self.lamps = {}

        self.font = pygame.font.Font("./res/fonts/typewriter.otf", self.FONT_SIZE)

        for count, letter in enumerate("QWERTZUIOASDFGHJKPYXCVBNML"):
            if count >= self.ROW_1_LAMPS + self.ROW_2_LAMPS:
                self.lamps[letter] = [(
                    self.SPACE[0] + self.PADDING + self.LAMP_RADIUS + (self.LAMP_RADIUS * 2 + self.PADDING) * (count - self.ROW_1_LAMPS - self.ROW_2_LAMPS),
                    self.SPACE[1] + self.PADDING * 3 + self.LAMP_RADIUS * 5
                ), self.font.render(letter, True, self.TEXT_COLOR)]
            elif count >= self.ROW_1_LAMPS:
                self.lamps[letter] = [(
                    self.SPACE[0] + self.PADDING / 2 + (self.PADDING + self.LAMP_RADIUS * 2) * (count - self.ROW_1_LAMPS + 1),
                    self.SPACE[1] + self.PADDING * 2 + self.LAMP_RADIUS * 3
                ), self.font.render(letter, True, self.TEXT_COLOR)]
            else:
                self.lamps[letter] = [(
                    self.SPACE[0] + self.PADDING + self.LAMP_RADIUS + (self.LAMP_RADIUS * 2 + self.PADDING) * (count),
                    self.SPACE[1] + self.PADDING + self.LAMP_RADIUS
                ), self.font.render(letter, True, self.TEXT_COLOR)]

    def draw(self, screen, light):
        for key, (pos, text) in self.lamps.items():
            if key == light:
                color = self.LAMP_COLOR_ON
            else:
                color = self.LAMP_COLOR_OFF

            pygame.draw.circle(screen, color, pos, self.LAMP_RADIUS)
            screen.blit(text, text.get_rect(center=pos))