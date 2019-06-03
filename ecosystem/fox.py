from ecosystem import animal

class Fox(animal.Animal):
    
    def diet(self):
        return ['badger', 'rabbit']

    def __str__(self):
        return 'fox'