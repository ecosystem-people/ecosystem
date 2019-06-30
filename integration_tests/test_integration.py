import unittest
from ecosystem import controller, grass, rabbit, badger, fox, lifeform

class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.controller = controller.Controller()
        self.lifeform = lifeform.LifeForm()

    def test_lifeform_starves_after_some_time_without_food(self):
        self.controller.ecosystem = [self.lifeform]
        for i in range(20):
            self.controller.cycle()
        self.assertFalse(self.lifeform in self.controller.ecosystem)