from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch


class TestKorean_translator(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)

    @patch('assignment1.random_boolean', return_value=1)
    @patch('assignment1.get_user_input', return_value='y')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_korean_translator_yes_Ca(self, mock_stdout, mock_input, mock_input2):
        expected = "humm.. Interesting! It says 캐 in Korean is Ca! "
        assignment1.korean_translator(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.random_boolean', return_value=1)
    @patch('assignment1.get_user_input', return_value='n')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_korean_translator_no_Ca(self, mock_stdout, mock_input, mock_input2):
        expected = "oh, This isn't what I need.. Let's move on.."
        assignment1.korean_translator(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())


