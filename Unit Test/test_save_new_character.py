from unittest import TestCase
import Character
import json
import assignment1


class TestSave_new_character(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)

    def test_save_new_character_dictionary(self):
        expected = self.test_character.__dict__
        assignment1.save_new_character(self.test_character)
        actual = {'hp': 10,
                  'kill': 0,
                  'mission': '',
                  'mission_01': 0,
                  'mission_02': 0,
                  'name': 'User',
                  'quit': False,
                  'x_coord': 1,
                  'y_coord': 1}
        self.assertEqual(expected, actual)

    def test_save_new_character_json(self):
        expected = "User.json"
        assignment1.save_new_character(self.test_character)
        actual = self.test_character.get_name() + ".json"
        self.assertEqual(expected, actual)


