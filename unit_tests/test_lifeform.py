import unittest
from ecosystem import rabbit, badger, fox, lifeform, grass

class LifeFormTests(unittest.TestCase):

    def setUp(self):
        self.fluffy = rabbit.Rabbit()
        self.bodger = badger.Badger()
        self.foxy = fox.Fox()
        self.lifeform = lifeform.LifeForm()
        self.grass = grass.Grass()

    def tearDown(self):
        pass

    def test_lifeforms_initialize_alive_with_empty_diet(self):
        self.assertTrue(self.lifeform.is_alive)
        self.assertEqual(self.lifeform.diet, [])

    def test_rabbits_initialize_alive(self):
        self.assertTrue(self.fluffy.is_alive)

    def test_badgers_initialize_alive(self):
        self.assertTrue(self.bodger.is_alive)

    def test_foxes_initialize_alive(self):
        self.assertTrue(self.foxy.is_alive)

    def test_rabbit_can_eat_grass(self):
        self.fluffy.eat(self.grass)
        self.assertFalse(self.grass.is_alive)

    def test_badger_can_eat_rabbit(self):
        self.bodger.eat(self.fluffy)
        self.assertFalse(self.fluffy.is_alive)

    def test_fox_can_eat_badger(self):
        self.foxy.eat(self.bodger)
        self.assertFalse(self.bodger.is_alive)

    def test_fox_can_eat_rabbit(self):
        self.foxy.eat(self.fluffy)
        self.assertFalse(self.fluffy.is_alive)

    def test_rabbit_cannot_eat_badger(self):
        self.fluffy.eat(self.bodger)
        self.assertTrue(self.bodger.is_alive)

    def test_rabbit_cannot_eat_fox(self):
        self.fluffy.eat(self.foxy)
        self.assertTrue(self.foxy.is_alive)

    def test_badger_cannot_eat_fox(self):
        self.bodger.eat(self.foxy)
        self.assertTrue(self.foxy.is_alive)

    def test_lifeforms_cannot_eat_themselves(self):
        for lifeform in [self.fluffy, self.foxy, self.bodger, self.grass]:
            lifeform.eat(lifeform)
            self.assertTrue(lifeform.is_alive)

if __name__ == '__main__':
    unittest.main()
