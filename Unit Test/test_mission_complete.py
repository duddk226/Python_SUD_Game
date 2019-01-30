from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch


class TestMission_complete(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 2, 3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_mission_complete_goodbye(self,mock_stdout):
        self.test_character.set_mission_02(2)
        expected = "good job! You made it!!!! Thank you so much for playing my Game, See you next_move Time!"
        assignment1.mission_complete(self.test_character)
        self.assertIn(expected,mock_stdout.getvalue())

    def test_mission_complete_quit(self):
        self.test_character.set_mission_02(2)
        expected = True
        assignment1.mission_complete(self.test_character)
        actual = self.test_character.get_quit()
        self.assertEqual(expected, actual)

    def test_mission_complete_quit_nottrue(self):
        self.test_character.set_mission_02(300)
        expected = False
        assignment1.mission_complete(self.test_character)
        actual = self.test_character.get_quit()
        self.assertEqual(expected, actual)




