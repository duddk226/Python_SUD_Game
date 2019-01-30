from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch


class TestVerify_user(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)

    @patch('assignment1.get_user_input', side_effect=['y'])
    @patch('assignment1.generate_character', side_effect =['User'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_verify_user(self, mock_stdout,mock_input,mock_input2):
        # expected = "Hello " + self.test_character.get_name() + "!\nLet's start! Hope you are ready!"
        expected = "\n\nHi, Are you a new user? if yes, please type Y, if no, please type YOUR NAME"
        assignment1.verify_user()
        self.assertIn(expected,mock_stdout.getvalue())
