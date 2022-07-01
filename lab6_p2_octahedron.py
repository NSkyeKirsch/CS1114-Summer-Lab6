import lab6_p2_die as die
from random import randint


class Octahedron(die.Die):

    def __init__(self, initial_value=4):
        num_sides = 8
        super().__init__(num_sides, initial_value)

    def roll(self):
        self.face_value = randint(1, self.sides)
