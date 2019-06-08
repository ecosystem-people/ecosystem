from ecosystem import animal

class Badger(animal.Animal):

    def __init__(self):
        super().__init__()
        self.diet.append('rabbit')

    def __str__(self):
        return 'badger'