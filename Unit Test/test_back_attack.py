from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch



class TestBack_attack(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 1, 1)

    @patch('assignment1.roll_a_die', return_value='3')
    def test_back_attack(self, mock_input):
        expected = 7
        assignment1.back_attack(self.test_character)
        actual = self.test_character.get_hp()
        self.assertEqual(expected, actual)

    @patch('assignment1.roll_a_die', return_value='3')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_back_attack_statement(self, mock_stdout,mock_input):
        expected = "While I was running away from ugly Evil monster, monster attacked my back...!!!!! How come..\n"
        "My NEW HP :", self.test_character.get_hp()
        assignment1.back_attack(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())
