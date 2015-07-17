import unittest
from main import problem

class TestProblem(unittest.TestCase):

    def test_upper(self):
        self.assertFalse(problem("mispronounced", "snond"))
        self.assertFalse(problem("shotgunned", "snond"))
        self.assertFalse(problem('bystander', 'baand'))
        self.assertFalse(problem('titties', 'tits'))
        self.assertTrue(problem("misfunctioned", "snond"))
        self.assertTrue(problem("snond", "snond"))
        self.assertTrue(problem("synchronized", "snond"))
        self.assertTrue(problem('bystander', 'band'))
        self.assertTrue(problem('conch', 'conch'))
        self.assertTrue(problem('titties', 'tittis'))

if __name__ == '__main__':
    unittest.main()
