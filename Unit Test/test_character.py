from unittest import TestCase
import Character


class TestAttack(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)
        self.test_character2 = Character.Character('', 2, 0)

    def test_get_name_name(self):
        expected = "User"
        actual = self.test_character.get_name()
        self.assertEqual(expected, actual)

    def test_get_name_char2(self):
        expected = ''
        actual = self.test_character2.get_name()
        self.assertEqual(expected, actual)

    def test_get_x_char1(self):
        expected = 1
        actual = self.test_character.get_x()
        self.assertEqual(expected, actual)

    def test_get_x_char2(self):
        expected = 2
        actual = self.test_character2.get_x()
        self.assertEqual(expected, actual)

    def test_set_x_char1(self):
        expected = 0
        actual = self.test_character.set_x(0)
        self.assertEqual(expected, actual)

    def test_set_x_char2(self):
        expected = 1
        actual = self.test_character2.set_x(1)
        self.assertEqual(expected, actual)

    def test_get_y_char1(self):
        expected = 1
        actual = self.test_character.get_y()
        self.assertEqual(expected, actual)

    def test_get_y_char2(self):
        expected = 0
        actual = self.test_character2.get_y()
        self.assertEqual(expected, actual)

    def test_set_y_char1(self):
        expected = 0
        actual = self.test_character.set_y(0)
        self.assertEqual(expected, actual)

    def test_set_y_char2(self):
        expected = 2
        actual = self.test_character2.set_y(2)
        self.assertEqual(expected, actual)

    def test_get_hp_char1(self):
        expected = 10
        actual = self.test_character.get_hp()
        self.assertEqual(expected, actual)

    def test_get_hp_char2(self):
        expected = 10
        actual = self.test_character2.get_hp()
        self.assertEqual(expected, actual)

    def test_set_hp_char1(self):
        expected = 6
        actual = self.test_character.set_hp(6)
        self.assertEqual(expected, actual)

    def test_set_hp_char2(self):
        expected = 3
        actual = self.test_character2.set_hp(3)
        self.assertEqual(expected, actual)

    def test_increment_hpchar1(self):
        self.test_character.set_hp(3)
        expected = 4
        self.test_character.increment()
        actual = self.test_character.get_hp()
        self.assertEqual(expected, actual)

    def test_increment_hpchar1(self):
        self.test_character2.set_hp(2)
        expected = 3
        self.test_character2.increment()
        actual = self.test_character2.get_hp()
        self.assertEqual(expected, actual)

    def test_get_kill(self):
        expected = 0
        actual = self.test_character.get_kill()
        self.assertEqual(expected, actual)

    def test_increment_kill(self):
        expected = 1
        self.test_character.increment_kill()
        actual = self.test_character.get_kill()
        self.assertEqual(expected, actual)

    def test_increment_kill_double(self):
        expected = 2
        self.test_character.increment_kill()
        self.test_character.increment_kill()
        actual = self.test_character.get_kill()
        self.assertEqual(expected, actual)

    def test_get_mission(self):
        expected = ''
        actual = self.test_character.get_mission()
        self.assertEqual(expected, actual)

    def test_set_mission(self):
        expected = '아무거나'
        actual = self.test_character.set_mission('아무거나')
        self.assertEqual(expected, actual)

    def test_set_mission_char_2(self):
        expected = 'setting up mission'
        actual = self.test_character2.set_mission('setting up mission')
        self.assertEqual(expected, actual)

    def test_get_mission_01(self):
        expected = 0
        actual = self.test_character.get_mission_01()
        self.assertEqual(expected, actual)

    def test_set_mission_01(self):
        expected = 1
        actual = self.test_character.set_mission_01(1)
        self.assertEqual(expected, actual)

    def test_set_mission_01_negtative(self):
        expected = -1
        actual = self.test_character.set_mission_01(-1)
        self.assertEqual(expected, actual)

    def test_get_mission_02(self):
        expected = 0
        actual = self.test_character2.get_mission_01()
        self.assertEqual(expected, actual)

    def test_set_mission_02(self):
        expected = 33
        actual = self.test_character2.set_mission_02(33)
        self.assertEqual(expected, actual)

    def test_set_mission_02_string(self):
        expected = 'string'
        actual = self.test_character2.set_mission_02('string')
        self.assertEqual(expected, actual)

    def test_get_quit(self):
        expected= False
        actual = self.test_character.get_quit()
        self.assertEqual(expected, actual)

    def test_set_quit(self):
        expected = True
        actual = self.test_character2.set_quit(True)
        self.assertEqual(expected, actual)
