from unittest import TestCase
import assignment1
import Character
import io
import Monster
from unittest.mock import patch


class TestMonster_appear_user_choice(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)
        self.test_monster = Monster.Monster()

    @patch('assignment1.get_user_input', side_effect=['r'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_appear_user_choice_runaway(self, mock_stdout, mock_input):
        expected = "FLEEEEE~ HAHAHA you can't catch me. Let's move on."
        assignment1.monster_appear_user_choice(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.get_user_input', side_effect=['f'])
    @patch('assignment1.roll_a_die', return_value='5')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_monster_appear_user_choice_fight(self, mock_stdout, mock_input, mock_input2):
        expected = "Fire Ball!!!!!!!!"
        assignment1.monster_appear_user_choice(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

