from abc import ABC, abstractmethod


class Die(ABC):

    def __init__(self, num_sides, initial_value=4):
        self.sides = num_sides
        self.face_value = initial_value

    def __str__(self):
        return 'number of sides: {}, face value: {}'.format(self.sides, self.face_value)

    @property
    def get_face(self):
        return self.face_value

    @abstractmethod
    def roll(self):
        pass



