import unittest
from ecosystem import controller, grass, rabbit, badger, fox, lifeform

class ControllerTest(unittest.TestCase):

    def setUp(self):
        self.fluffy = rabbit.Rabbit()
        self.bodger = badger.Badger()
        self.foxy = fox.Fox()
        self.lifeform = lifeform.LifeForm()
        self.grass = grass.Grass()
        self.controller = controller.Controller()
        self.controller.ecosystem = [self.fluffy, self.foxy, fox.Fox(), self.bodger, self.grass]

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

    def test_cycle_removes_starved_rabbit(self):
        fluffy = rabbit.Rabbit()
        self.controller.ecosystem.append(fluffy)
        fluffy.hp = 0
        self.controller.cycle()
        self.assertFalse(fluffy in self.controller.ecosystem)

    def test_rabbit_dies_when_it_gets_eaten(self):
        self.assertEqual(self.lifeform.hp, 100)
        self.bodger.eat(self.fluffy)
        self.controller.cycle()
        self.assertFalse(self.fluffy in self.controller.ecosystem)

    def test_lifeforms_automatically_eat_when_prey_available(self):
        rex = rabbit.Rabbit()
        self.controller.ecosystem = [rex, grass.Grass()]
        self.controller.cycle()
        self.assertEqual(self.controller.ecosystem, [rex])

    def test_predator_will_not_eat_when_it_has_been_eaten(self):
        self.controller.ecosystem = [self.bodger, self.fluffy]
        self.foxy.eat(self.bodger)
        self.controller.cycle()
        self.assertTrue(self.fluffy.is_alive)

    def test_if_lifeform_hp_is_zero_then_lifeform_dies(self):
        self.controller.ecosystem = [self.fluffy]
        self.fluffy.hp = 0
        self.controller.cycle()
        self.assertFalse(self.fluffy in self.controller.ecosystem)