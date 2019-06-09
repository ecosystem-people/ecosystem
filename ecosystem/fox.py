from ecosystem import lifeform

class Fox(lifeform.LifeForm):
    
    def __init__(self):
        super().__init__()
        self.diet.append('rabbit')
        self.diet.append('badger')

    def __str__(self):
        return 'fox'