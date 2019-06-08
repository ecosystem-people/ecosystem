from ecosystem import animal

class Rabbit(animal.Animal):

    def __str__(self):
        return 'rabbit'

    def __init__(self):
        super().__init__()