import pygame

class Plugboard:
    def __init__(self):
        self.SWITCH_RADIUS = 30
        self.ROW_1_SWITCHES = 9
        self.ROW_2_SWITCHES = 8
        self.ROW_3_SWITCHES = 9
        self.SPACE = (30, 360)
        self.PADDING = 10
        self.FONT_SIZE = 20
        self.TEXT_COLOR = (150, 150, 150)
        self.SWITCH_COLOR = (100, 100, 100)
        self.PLUG_SIZE = (20, 30)
        self.PLUG_COLOR = (20, 20, 20)
        self.WIRE_THICKNESS = 4
        self.WIRE_COLOR = (50, 50, 50)
        self.HOLE_RADIUS = 5
        
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.pairs = []

        self.switches = {}
        self.wiring = False
        self.wires_starts = []
        self.wires_ends = []

        self.font = pygame.font.Font("./res/fonts/typewriter.otf", self.FONT_SIZE)

        for count, letter in enumerate("QWERTZUIOASDFGHJKPYXCVBNML"):
            if count >= self.ROW_1_SWITCHES + self.ROW_2_SWITCHES:
                self.switches[letter] = {"pos": (
                    self.SPACE[0] + self.PADDING + self.SWITCH_RADIUS + (self.SWITCH_RADIUS * 2 + self.PADDING) * (count - self.ROW_1_SWITCHES - self.ROW_2_SWITCHES),
                    self.SPACE[1] + self.PADDING * 3 + self.SWITCH_RADIUS * 5
                ), "font": self.font.render(letter, True, self.TEXT_COLOR), "busy": False}
            elif count >= self.ROW_1_SWITCHES:
                self.switches[letter] = {"pos": (
                    self.SPACE[0] + self.PADDING / 2 + (self.PADDING + self.SWITCH_RADIUS * 2) * (count - self.ROW_1_SWITCHES + 1),
                    self.SPACE[1] + self.PADDING * 2 + self.SWITCH_RADIUS * 3
                ), "font": self.font.render(letter, True, self.TEXT_COLOR), "busy": False}
            else:
                self.switches[letter] = {"pos": (
                    self.SPACE[0] + self.PADDING + self.SWITCH_RADIUS + (self.SWITCH_RADIUS * 2 + self.PADDING) * (count),
                    self.SPACE[1] + self.PADDING + self.SWITCH_RADIUS
                ), "font": self.font.render(letter, True, self.TEXT_COLOR), "busy": False}

    def set_pairs(self):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for pair in self.pairs:
            pos_a = self.left.find(pair[0])
            pos_b = self.left.find(pair[1])

            self.left = self.left[:pos_a] + pair[1] + self.left[pos_a + 1:]
            self.left = self.left[:pos_b] + pair[0] + self.left[pos_b + 1:]

    def input(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)

    def output(self, signal):
        letter = self.left[signal]
        return self.right.find(letter)
    
    def free(self, index):
        self.switches[self.pairs[index][0]]["busy"] = False
        self.switches[self.pairs[index][1]]["busy"] = False

        del self.pairs[index]

        del self.wires_starts[index]
        del self.wires_ends[index]
    
    def update(self, mouse):
        for key, data in self.switches.items():
            pos = data["pos"]
            busy = data["busy"]

            dist = ((mouse[0] - pos[0])**2 + (mouse[1] - pos[1])**2)**0.5

            if dist <= self.SWITCH_RADIUS:
                self.switches[key]["busy"] = True
                break
            else:
                key = pos = busy = None

        if key is not None:
            if not self.wiring and not busy:
                self.wires_starts.append(pos)
                self.wires_ends.append((-1, -1))

                self.pairs.append(key)

                self.wiring = True
            elif self.wiring and not busy:
                self.wires_ends[-1] = pos

                self.pairs[-1] += key

                self.set_pairs()

                self.wiring = False
            elif not self.wiring and busy:
                if pos in self.wires_starts:
                    index = self.wires_starts.index(pos)
                else:
                    index = self.wires_ends.index(pos)

                self.free(index)

                self.set_pairs()
    
    def draw(self, screen):
        for _, data in self.switches.items():
            pos = data["pos"]
            text = data["font"]

            pygame.draw.circle(screen, self.SWITCH_COLOR, pos, self.HOLE_RADIUS)
            pygame.draw.circle(screen, self.SWITCH_COLOR, (pos[0], pos[1] + self.PADDING * 2), self.HOLE_RADIUS)
            screen.blit(text, text.get_rect(center=(pos[0], pos[1] - self.PADDING * 2)))

        for ps, pe in zip(self.wires_starts, self.wires_ends):
            if pe == (-1, -1):
                pe = pygame.mouse.get_pos()
            
            pygame.draw.rect(screen, self.PLUG_COLOR, pygame.Rect(ps[0] - self.PLUG_SIZE[0] // 2, ps[1] - self.HOLE_RADIUS, self.PLUG_SIZE[0], self.PLUG_SIZE[1]))
            pygame.draw.rect(screen, self.PLUG_COLOR, pygame.Rect(pe[0] - self.PLUG_SIZE[0] // 2, pe[1] - self.HOLE_RADIUS, self.PLUG_SIZE[0], self.PLUG_SIZE[1]))
            pygame.draw.line(screen, self.WIRE_COLOR, (ps[0], ps[1] + self.PLUG_SIZE[1] // 4), (pe[0], pe[1] + self.PLUG_SIZE[1] // 4), width=self.WIRE_THICKNESS)