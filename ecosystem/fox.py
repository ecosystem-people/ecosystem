from ecosystem import animal

class Fox(animal.Animal):
    
    def __init__(self):
        super().__init__()
        self.diet.append('rabbit')
        self.diet.append('badger')

    def __str__(self):
        return 'fox'