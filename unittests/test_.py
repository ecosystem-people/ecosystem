import unittest
from ecosystem import rabbit, badger, fox

class AnimalTests(unittest.TestCase):

    def setUp(self):
        self.fluffy = rabbit.Rabbit()
        self.bodger = badger.Badger()
        self.foxy = fox.Fox()

    def tearDown(self):
        pass

    def test_rabbits_initialize_alive(self):
        self.assertTrue(self.fluffy.is_alive)

    def test_badgers_initialize_alive(self):
        self.assertTrue(self.bodger.is_alive)

    def test_foxes_initialize_alive(self):
        self.assertTrue(self.foxy.is_alive)

    def test_badger_can_eat_rabbit(self):
        self.bodger.eat(self.fluffy)
        self.assertFalse(self.fluffy.is_alive)

    def test_fox_can_eat_badger(self):
        self.foxy.eat(self.bodger)
        self.assertFalse(self.bodger.is_alive)

    def test_rabbit_cannot_eat_badger(self):
        self.fluffy.eat(self.bodger)
        self.assertTrue(self.bodger.is_alive)

if __name__ == '__main__':
    unittest.main()
