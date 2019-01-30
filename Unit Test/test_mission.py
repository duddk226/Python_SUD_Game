from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch


class TestMission(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 2, 3)

    @patch('assignment1.get_user_input', side_effect=['1'])
    def test_mission_user_choose_1(self, mock_input):
        expected = '쿠키'
        assignment1.mission(self.test_character)
        actual = self.test_character.get_mission()
        self.assertEqual(expected, actual)

    @patch('assignment1.get_user_input', side_effect=['2'])
    def test_mission_user_choose_2(self, mock_input):
        expected = '캐나다'
        assignment1.mission(self.test_character)
        actual = self.test_character.get_mission()
        self.assertEqual(expected, actual)

    @patch('assignment1.get_user_input', side_effect=['1'])
    def test_mission_mission_01_kill5monster(self, mock_input):
        expected = 0
        assignment1.mission(self.test_character)
        actual = self.test_character.get_mission_01()
        self.assertEqual(expected, actual)

    @patch('assignment1.get_user_input', side_effect=['2'])
    def test_mission_mission_02_kill5monster(self, mock_input):
        expected = 0
        assignment1.mission(self.test_character)
        actual = self.test_character.get_mission_02()
        self.assertEqual(expected, actual)

    @patch('assignment1.get_user_input', side_effect=['1'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mission_user_choose_1_print(self,mock_stdout, mock_input):
        expected = "\nOn the Paper, it says 쿠키. ohh.. What is 쿠키?"
        assignment1.mission(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('assignment1.get_user_input', side_effect=['2'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mission_user_choose_2_print(self, mock_stdout, mock_input):
        expected = "\nOn the Paper, it says 캐나다. ohh.. What is 캐나다?"
        assignment1.mission(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())