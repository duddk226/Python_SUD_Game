from unittest import TestCase
import assignment1
import Character
import io
from unittest.mock import patch


class TestVerify_user(TestCase):
    def setUp(self):
        self.test_character = Character.Character("User", 2, 3)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cha_map_check_left_wall_map(self, mock_stdout):
        expected = "["
        assignment1.cha_map(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cha_map_check_right_wall_map(self, mock_stdout):
        expected = "]"
        assignment1.cha_map(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cha_map_check_location_hash_tag(self, mock_stdout):
        expected = "#"
        assignment1.cha_map(self.test_character)
        self.assertIn(expected, mock_stdout.getvalue())

