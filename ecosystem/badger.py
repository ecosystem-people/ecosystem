from ecosystem import lifeform

class Badger(lifeform.LifeForm):

    def __init__(self):
        super().__init__()
        self.diet.append('rabbit')

    def __str__(self):
        return 'badger'