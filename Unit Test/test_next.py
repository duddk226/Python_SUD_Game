from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch


class TestMonster_appear(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)

    @patch('assignment1.roll_a_die', return_value=3)
    def test_next_move_hp_up(self,mock_input):
        self.test_character.set_hp(6)
        expected = 7
        assignment1.next_move(self.test_character)
        actual = self.test_character.get_hp()
        self.assertEqual(expected, actual)

    @patch('assignment1.roll_a_die', return_value=1)
    @patch('assignment1.get_user_input', side_effect=['r'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_next_move_to_monster_choose(self, mock_stdout, mock_input, mock_input2):
        expected = "While I was running away from ugly Evil monster, monster attacked my back."
        assignment1.next_move(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.roll_a_die', return_value=1)
    @patch('assignment1.get_user_input', side_effect=['f'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_next_move_to_fight(self, mock_stdout, mock_input, mock_input2):
        expected = "Fire Ball!!!!!!!!"
        assignment1.next_move(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())
