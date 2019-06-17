class LifeForm:
    STARTING_HP = 100

    def __init__(self):
        self.is_alive = True
        self.diet = []
        self.hp = self.STARTING_HP

    def eat(self, prey):
        if str(prey) in self.diet:
            prey.is_alive = False
            self.hp += 5
            if self.hp > self.STARTING_HP:
                self.hp = self.STARTING_HP
