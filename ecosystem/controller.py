class Controller():
    
    def __init__(self):
        self.day = 0
        self.ecosystem = []

    def cycle(self):
        self.day += 1
        for lifeform in self.ecosystem:
            lifeform.hp -= 10
        self.positive_hp_lifeforms = []
        for lifeform in self.ecosystem:
            if lifeform.hp > 0:
                self.positive_hp_lifeforms.append(lifeform)
        for predator in self.positive_hp_lifeforms:
            if predator.is_alive:
                for prey in self.positive_hp_lifeforms:
                    predator.eat(prey)
        self.updated_ecosystem = []
        for lifeform in self.positive_hp_lifeforms:
            if lifeform.is_alive:
                self.updated_ecosystem.append(lifeform)
        self.ecosystem = self.updated_ecosystem
        
    def headcount(self):
        headcount = {}
        for lifeform in self.ecosystem:
            headcount[str(lifeform)] = headcount[str(lifeform)] + 1 if str(lifeform) in list(headcount.keys()) else 1
        return headcount

    def report(self):
        report = 'Day %s' % self.day
        for key in self.headcount():
            report += '\n%ss: %s' % (key.capitalize(), self.headcount()[key])
        return report

