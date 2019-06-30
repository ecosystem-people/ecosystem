from ecosystem import rabbit, fox, grass, badger, controller

class ManualTestingScript():

    def setup(self):
        self.r = rabbit.Rabbit()
        self.b = badger.Badger()
        self.f = fox.Fox()
        self.c = controller.Controller()
        self.c.ecosystem = [self.r, self.b, self.f]
        print(self.c.report())
        self.c.cycle()
