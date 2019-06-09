class Controller():
    
    def __init__(self):
        self.day = 0
        self.ecosystem = []

    def cycle(self):
        self.day += 1

    def headcount(self):
        headcount = {}
        for lifeform in self.ecosystem:
            headcount[str(lifeform)] = headcount[str(lifeform)] + 1 if str(lifeform) in list(headcount.keys()) else 1
        return headcount