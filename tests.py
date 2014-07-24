import unittest

import mock

from role import Role, Warrior, Priest, Rouge, Hunter, role_selection


class Roletest(unittest.TestCase):


    def test_that_warrior_has_200_health(self):
        self.assertEqual(Warrior().health, 200)

    def test_that_warrior_50_magic(self):
        self.assertEqual(Warrior().magic, 50)

    def test_that_warrior_has_0_choice(self):
        self.assertEqual(Warrior().choice, 0)

    def test_that_warrior_has_shield(self):
        self.assertEqual(Warrior().weapon, "shield")

    def test_that_warrior_has_title(self):
        self.assertEqual(Warrior().title, "The Brave")
    
    def test_that_priest_has_100_health(self):
        self.assertEqual(Priest().health, 100)

    def test_that_priest_has_50_magic(self):
        self.assertEqual(Priest().magic, 200)

    def test_that_priest_has_0_choice(self):
        self.assertEqual(Priest().choice, 0)

    def test_that_priest_has_staff(self):
        self.assertEqual(Priest().weapon, "staff")

    def test_that_priest_has_title(self):
        self.assertEqual(Priest().title, "The Healing")

    def test_that_rouge_has_150_health(self):
        self.assertEqual(Rouge().health, 150)

    def test_that_rouge_has_50_magic(self):
        self.assertEqual(Rouge().magic, 30)

    def test_that_rouge_has_0_choice(self):
        self.assertEqual(Rouge().choice, 0)

    def test_that_rouge_has_staff(self):
        self.assertEqual(Rouge().weapon, "daggers")

    def test_that_rouge_has_title(self):
        self.assertEqual(Rouge().title, "The Quick")

    def test_that_hunter_has_125_health(self):
        self.assertEqual(Hunter().health, 125)

    def test_that_hunter_has_100_magic(self):
        self.assertEqual(Hunter().magic, 100)

    def test_that_hunter_has_0_choice(self):
        self.assertEqual(Hunter().choice, 0)

    def test_that_hunter_has_staff(self):
        self.assertEqual(Hunter().weapon, "bow")

    def test_that_hunter_has_title(self):
        self.assertEqual(Hunter().title, "The Swift")

    @mock.patch("__builtin__.raw_input", mock.Mock(return_value="y"))
    def test_warrior_role_selection_changes_choice_attribute(self):
        sut = role_selection()
        self.assertEqual(sut.choice, 2)
        self.assertIsInstance(sut, Priest)

    @mock.patch("__builtin__.raw_input", return_value="no")
    def test_warrior_role_selection_changes_choice_attribute_other_way(self, mock_answer):
        sut = role_selection()
        self.assertEqual(sut.choice, 0)
        self.assertIsInstance(sut, Warrior)

    @mock.patch("__builtin__.raw_input", mock.Mock(return_value="y"))
    def test_that_character_with_most_choice_is_returned(self):
        self.assertIsInstance(role_selection(), Priest)
