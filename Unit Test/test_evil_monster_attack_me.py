from unittest import TestCase
import assignment1
import Character
import io
import Monster
from unittest.mock import patch


class TestEvil_monster_attack_me(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)
        self.test_monster = Monster.Monster()

    @patch('assignment1.roll_a_die', return_value='4')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evil_monster_attack_me_print_check(self, mock_stdout, mock_input):
        expected = "HAHA, NICE TRY. It's MY turn hahahahhahahh"
        assignment1.evil_monster_attack_me(self.test_character, self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.roll_a_die', return_value='4')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evil_monster_attack_me_print_check2(self, mock_stdout, mock_input):
        expected = "EVIL MONSTER: ICE ARROW!!!!!!!!!!"
        assignment1.evil_monster_attack_me(self.test_character, self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.roll_a_die', return_value='4')
    def test_evil_monster_attack_me_print_new_char_hp(self,mock_input):
        expected = 6
        assignment1.evil_monster_attack_me(self.test_character, self.test_character)
        actual = self.test_character.get_hp()
        self.assertTrue(expected, actual)

    @patch('assignment1.roll_a_die', return_value='4')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_evil_monster_attack_me_revenge_statement(self, mock_stdout, mock_input):
        expected = "It's MY TURN. ARE YOU READY?"
        assignment1.evil_monster_attack_me(self.test_character, self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

