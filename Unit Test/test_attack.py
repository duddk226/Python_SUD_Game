from unittest import TestCase
import assignment1
import Character
import io
import Monster
from unittest.mock import patch


class TestAttack(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)
        self.test_monster = Monster.Monster()

    @patch('assignment1.roll_a_die', return_value='5')
    def test_attack_monster_die(self, mock_input):
        expected = 0
        assignment1.attack(self.test_character, self.test_monster)
        actual = self.test_monster.get_hp()
        self.assertEqual(expected, actual)

    @patch('assignment1.roll_a_die', return_value='5')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_monster_die(self, mock_stdout,mock_input):
        expected = "Agggggg.. EVIL MONSTER is DEAD..."
        assignment1.attack(self.test_character, self.test_monster)
        self.assertIn(expected,mock_stdout.getvalue())

    @patch('assignment1.roll_a_die', return_value='5')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_attack_monster_fireball(self, mock_stdout, mock_input):
        expected = ":Fire Ball!!!!!!!!\nDAMAGE:"
        assignment1.attack(self.test_character, self.test_monster)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.roll_a_die', return_value='5')
    def test_attack_monster_kill_increase(self, mock_input):
        expected = 1
        assignment1.attack(self.test_character, self.test_monster)
        actual = self.test_character.get_kill()
        self.assertEqual(expected, actual)

