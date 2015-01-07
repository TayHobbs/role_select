import unittest

from roles import Warrior, Rouge, Priest


class RoleTests(unittest.TestCase):

    def test_roles_have_name(self):
        warrior = Warrior()
        rouge = Rouge()
        priest = Priest()
        self.assertTrue(warrior.name)
        self.assertTrue(rouge.name)
        self.assertTrue(priest.name)

    def test_roles_have_job(self):
        warrior = Warrior()
        rouge = Rouge()
        priest = Priest()
        self.assertTrue(warrior.job)
        self.assertTrue(rouge.job)
        self.assertTrue(priest.job)

    def test_roles_have_weapon(self):
        warrior = Warrior()
        rouge = Rouge()
        priest = Priest()
        self.assertTrue(warrior.weapon)
        self.assertTrue(rouge.weapon)
        self.assertTrue(priest.weapon)


if __name__ == '__main__':
    unittest.main()
