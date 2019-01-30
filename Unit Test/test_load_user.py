from unittest import TestCase
import json


class TestLoad_user(TestCase):

    def test_load_user_name(self):
        filename = "unit_test.json"
        with open(filename, 'r') as f_obj:
            user = json.load(f_obj)
        expected = user["name"]
        actual = "unittest"
        self.assertEqual(expected, actual)

    def test_load_user_hp(self):
        filename = "unit_test.json"
        with open(filename, 'r') as f_obj:
            user = json.load(f_obj)
        expected = user["hp"]
        actual = 9
        self.assertEqual(expected, actual)

    def test_load_user_kill(self):
        filename = "unit_test.json"
        with open(filename, 'r') as f_obj:
            user = json.load(f_obj)
        expected = user["kill"]
        actual = 1
        self.assertEqual(expected, actual)
