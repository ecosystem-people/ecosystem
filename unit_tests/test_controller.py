import unittest
from ecosystem import controller, grass, rabbit, badger, fox 

class ControllerTest(unittest.TestCase):

    def setUp(self):
        self.controller = controller.Controller()
        self.controller.ecosystem = [rabbit.Rabbit(), fox.Fox(), fox.Fox(), badger.Badger(), grass.Grass()]

    def test_ecosystem_exists(self):
        self.assertTrue(isinstance(self.controller.ecosystem, list))

    def test_can_do_headcount(self):
        headcount = self.controller.headcount()
        self.assertEqual(headcount['rabbit'], 1)
        self.assertEqual(headcount['fox'], 2)
        self.assertEqual(headcount['badger'], 1)
        self.assertEqual(headcount['grass'], 1)

    def test_days_increase(self):
        self.assertEqual(self.controller.day, 0)
        self.controller.cycle()
        self.assertEqual(self.controller.day, 1)

    def test_report(self):
        report = self.controller.report()
        self.assertTrue('Day' in report)
        self.assertTrue('Rabbits: 1' in report)