class Reflector:
    def __init__(self, wiring):
        self.left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.right = wiring

    def reflect(self, signal):
        letter = self.right[signal]
        return self.left.find(letter)

REFLECTOR_A = Reflector("EJMZALYXVBWFCRQUONTSPIKHGD")
REFLECTOR_B = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
REFLECTOR_C = Reflector("FVPJIAOYEDRZXWGCTKUQSBNMHL")
REFLECTOR_B_THIN = Reflector("ENKQAUYWJICOPBLMDXZVFTHRGS")
REFLECTOR_C_THIN = Reflector("RDOBJNTKVEHMLFCWZAXGYIPSUQ")