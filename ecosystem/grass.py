from ecosystem import lifeform

class Grass(lifeform.LifeForm):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return 'grass'