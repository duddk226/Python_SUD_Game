from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch


class TestGame(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)
        self.test_character_2= Character.Character("User", 1, 1)
        self.test_character.set_hp(0)

    @patch('assignment1.get_user_input', side_effect=['y', 'user', '1', 'q'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_game_quit(self, mock_stdout, mock_input):
        expected = "Thank you so much for playing my game!  Good Bye!"
        assignment1.game()
        self.assertIn(expected, mock_stdout.getvalue())
