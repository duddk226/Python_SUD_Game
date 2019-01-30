from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch


# east = y+1
# west = y-1
# north = x-1
# south =x +1
class TestMove(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)
        self.test_character_2 = Character.Character("User", 2, 2)

    @patch('assignment1.get_user_input', return_value='n')
    @patch('assignment1.next_move', return_value='3')
    def test_move_north(self, mock_input, mock_input2):
        expected = 0, 1
        assignment1.move(self.test_character)
        actual = self.test_character.get_x(), self.test_character.get_y()
        self.assertEqual(expected, actual)

    @patch('assignment1.get_user_input', return_value='w')
    @patch('assignment1.next_move', return_value='3')
    def test_move_west(self, mock_input, mock_input2):
        expected = 1, 0
        assignment1.move(self.test_character)
        actual = self.test_character.get_x(), self.test_character.get_y()
        self.assertEqual(expected, actual)

    @patch('assignment1.get_user_input', return_value='s')
    @patch('assignment1.next_move', return_value='3')
    def test_move_south(self, mock_input, mock_input2):
        expected = 2, 1
        assignment1.move(self.test_character)
        actual = self.test_character.get_x(), self.test_character.get_y()
        self.assertEqual(expected, actual)

    @patch('assignment1.get_user_input', return_value='e')
    @patch('assignment1.next_move', return_value='3')
    def test_move_east(self, mock_input, mock_input2):
        expected = 1, 2
        assignment1.move(self.test_character)
        actual = self.test_character.get_x(), self.test_character.get_y()
        self.assertEqual(expected, actual)

    @patch('assignment1.get_user_input', return_value='q')
    @patch('assignment1.next_move', return_value='3')
    def test_move_quit(self, mock_input, mock_input2):
        expected = True
        assignment1.move(self.test_character)
        actual = self.test_character.get_quit()
        self.assertEqual(expected, actual)

    @patch('assignment1.get_user_input', return_value='e')
    @patch('assignment1.next_move', return_value='3')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_move_not_valid(self, mock_stdout, mock_input, mock_input2):
        expected = "sorry, you reached the end of the map, Let's go different direction.\n"
        assignment1.move(self.test_character_2)
        self.assertEqual(mock_stdout.getvalue(), expected)

    @patch('assignment1.get_user_input', return_value='"')
    @patch('assignment1.next_move', return_value='3')
    def test_move_quit_thegame(self, mock_input, mock_input2):
        expected = assignment1.cha_map(self.test_character)
        assignment1.move(self.test_character)
        actual = assignment1.cha_map(self.test_character)
        self.assertEqual(expected, actual)
