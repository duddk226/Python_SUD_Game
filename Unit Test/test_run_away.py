from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch


class TestRun_away(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)

    @patch('assignment1.roll_a_die', return_value='3')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_away(self, mock_stdout, mock_input):
        expected = "FLEEEEE~ HAHAHA you can't catch me. Let's move on."
        assignment1.run_away(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.roll_a_die', return_value='1')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_away_notequal(self, mock_stdout, mock_input):
        expected = "FLEEEEE~ HAHAHA you can't catch me. Let's move on. I am so curious. I really need to find out\n"
        "what those word mean ! "
        assignment1.run_away(self.test_character)
        self.assertNotEquals(mock_stdout.getvalue(), expected)
