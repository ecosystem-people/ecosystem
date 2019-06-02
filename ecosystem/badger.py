from ecosystem import animal

class Badger(animal.Animal):

    def diet(self):
        return ['rabbit']

    def __str__(self):
        return 'badger'