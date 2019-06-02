import unittest

class AllTheTests(unittest.TestCase):

    def test_nothing(self):
        self.assertEqual(3, 3)

if __name__ == '__main__':
    unittest.main()
