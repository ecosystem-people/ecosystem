from ecosystem import lifeform

class Rabbit(lifeform.LifeForm):

    def __init__(self):
        super().__init__()
        self.diet.append('grass')
    
    def __str__(self):
        return 'rabbit'

    