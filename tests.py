import unittest
from ecosystem import rabbit, badger

class AllTheTests(unittest.TestCase):

    def test_rabbits_initialize_alive(self):
        fluffy = rabbit.Rabbit()
        self.assertTrue(fluffy.is_alive)

    def test_badger_can_eat_rabbit(self):
        bodger = badger.Badger()
        fluffy = rabbit.Rabbit()
        bodger.eat(fluffy)
        self.assertFalse(fluffy.is_alive)

if __name__ == '__main__':
    unittest.main()
