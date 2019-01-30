from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch


class TestGenerate_character(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)

    @patch('assignment1.get_user_input', return_value='User')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_character_name(self, mock_stdout, mock_input):
        expected = "Hello User!\nLet's start! Hope you are ready!"
        assignment1.generate_character()
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.get_user_input', return_value='Jane')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_generate_character_name_new_name(self, mock_stdout, mock_input):
        expected = "Hello Jane!\nLet's start! Hope you are ready!"
        assignment1.generate_character()
        self.assertIn(expected, mock_stdout.getvalue())
