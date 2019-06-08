class Animal:

    def __init__(self):
        self.is_alive = True
        self.diet = []

    def eat(self, prey):
        if str(prey) in self.diet:
            prey.is_alive = False
