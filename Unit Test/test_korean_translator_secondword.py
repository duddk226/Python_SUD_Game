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
    def test_korean_translator_secondword_nada(self, mock_stdout, mock_input, mock_input2):
        expected = "humm.. Interesting! It says 나다 in Korean is nada!/\n"
        "Oh!! 캐나다 is CANADA!!"
        assignment1.korean_translator_secondword(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.random_boolean', return_value=0)
    @patch('assignment1.get_user_input', return_value='y')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_korean_translator_secondword_kie(self, mock_stdout, mock_input, mock_input2):
        expected = "humm.. Interesting! It says 키 in Korean is kie!/\n"
        "Oh!! 쿠키 is COOKIE!!"
        assignment1.korean_translator_secondword(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.random_boolean', return_value=0)
    @patch('assignment1.get_user_input', return_value='n')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_korean_translator_secondword_donotneed(self, mock_stdout, mock_input, mock_input2):
         expected = "oh, this isn't what i need.."
         assignment1.korean_translator_secondword(self.test_character)
         self.assertIn(expected, mock_stdout.getvalue())
