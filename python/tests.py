import unittest

from roles import Warrior, Rouge, Priest, Ranger


class RoleTests(unittest.TestCase):

    def test_roles_have_name(self):
        warrior = Warrior()
        rouge = Rouge()
        priest = Priest()
        ranger = Ranger()
        self.assertTrue(warrior.name)
        self.assertTrue(rouge.name)
        self.assertTrue(priest.name)
        self.assertTrue(ranger.name)

    def test_roles_have_job(self):
        warrior = Warrior()
        rouge = Rouge()
        priest = Priest()
        ranger = Ranger()
        self.assertTrue(warrior.job)
        self.assertTrue(rouge.job)
        self.assertTrue(priest.job)
        self.assertTrue(ranger.job)

    def test_roles_have_weapon(self):
        warrior = Warrior()
        rouge = Rouge()
        priest = Priest()
        ranger = Ranger()
        self.assertTrue(warrior.weapon)
        self.assertTrue(rouge.weapon)
        self.assertTrue(priest.weapon)
        self.assertTrue(ranger.weapon)


if __name__ == '__main__':
    unittest.main()
