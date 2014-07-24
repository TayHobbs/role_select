import unittest
import operator
from role import Role, Warrior, Priest


class Roletest(unittest.TestCase):


    def test_that_warrior_has_200_health(self):
        role = Warrior()
        self.assertEqual(role.health, 200)

    def test_that_warrior_50_magic(self):
        role = Warrior()
        self.assertEqual(role.magic, 50)

    def test_that_warrior_has_0_choice(self):
        role = Warrior()
        self.assertEqual(role.choice, 0)
    
    def test_that_priest_has_100_health(self):
        role = Priest()
        self.assertEqual(role.health, 100)

    def test_that_priest_has_50_magic(self):
        role = Priest()
        self.assertEqual(role.magic, 200)
