from unittest import TestCase
import Monster


class TestMonster(TestCase):
    def setUp(self):
        self.test_monster = Monster.Monster()

    def test_get_hp_default(self):
        expected = 5
        actual = self.test_monster.get_hp()
        self.assertEqual(expected, actual)

    def test_set_hp_monster(self):
        expected = 3
        actual = self.test_monster.set_hp(3)
        self.assertEqual(expected, actual)

    def test_set_hp_monster_2(self):
        expected = 3
        actual = self.test_monster.set_hp(self.test_monster.get_hp() - 2)
        self.assertEqual(expected, actual)

    def test_get_name_default(self):
        expected = "EVIL MONSTER"
        actual = self.test_monster.get_name()
        self.assertEqual(expected, actual)

