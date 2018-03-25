from typing import Dict
from unittest import TestCase

from src.get_digits import get_digits


class GetDigitsTest(TestCase):
    def test_returns_list(self):
        result = get_digits(1)
        self.assertIsInstance(result, list)

    def test_returns_number_for_1_digit_number(self):
        for i in range(10):
            with self.subTest(i=i):
                result = get_digits(i)
                self.assertEqual(result, [i])

    def test_returns_2_numbers_for_2_digit_number(self):
        for i in range(10, 100):
            with self.subTest(i=i):
                result = get_digits(i)
                self.assertEqual(len(result), 2)

    def test_some_cases(self):
        cases: Dict[int, list] = {0: [0], 1: [1], 12: [1, 2], 34: [3, 4], 89: [8, 9], 100: [1, 0, 0]}
        for case in cases:
            with self.subTest(case=case):
                result = get_digits(case)
                self.assertEqual(result, cases[case])
