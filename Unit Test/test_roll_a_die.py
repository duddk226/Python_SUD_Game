from unittest import TestCase
import assignment1
import random
from unittest.mock import patch


class TestRoll_a_die(TestCase):
    def test_roll_a_die_true_greaterequl(self):
        self.assertGreaterEqual(assignment1.roll_a_die(3, 6), 3)

    def test_roll_a_die_true_lessequl(self):
        self.assertLessEqual(assignment1.roll_a_die(3, 6), 17)

    def test_roll_a_die_true_zero(self):
        self.assertEqual(0, assignment1.roll_a_die(0, 0))

    def test_roll_a_die_random(self):
        random.seed(1)
        self.assertEqual(3, assignment1.roll_a_die(1, 10))

    @patch('assignment1.roll_a_die', return_value=2)
    def test_roll_a_die_patch(self, mock_input):
        self.assertEqual(2, assignment1.roll_a_die(1, 10))

    @patch('assignment1.roll_a_die', return_value=3)
    def test_roll_a_die_patch_second_test(self, mock_input):
        expected = 3
        self.assertEqual(expected, assignment1.roll_a_die(1, 10))
