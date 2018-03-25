from unittest import TestCase

from src.fizzbuzz import fizzbuzz
from src.get_digits import get_digits


def has_3_in_digits(number: int):
    return 3 in get_digits(number)


def has_5_in_digits(number: int):
    return 5 in get_digits(number)


class FizzBuzzTest(TestCase):
    def test_output_is_list(self):
        result = fizzbuzz()
        self.assertIsInstance(result, list)

    def test_number_of_elements_is_100(self):
        result = fizzbuzz()
        self.assertEqual(len(result), 100)

    def test_multiples_of_three(self):
        result = fizzbuzz()
        for i in range(len(result)):
            if i % 3 == 0:
                with self.subTest(i=i):
                    self.assertIn(result[i], ["Fizz", "FizzBuzz"], msg=i)

    def test_multiples_of_five(self):
        result = fizzbuzz()
        for i in range(len(result)):
            if i % 5 == 0:
                with self.subTest(i=i):
                    self.assertIn(result[i], ["Buzz", "FizzBuzz"], msg=i)

    def test_multiple_of_fifteen(self):
        result = fizzbuzz()
        for i in range(len(result)):
            if i % 15 == 0:
                with self.subTest(i=i):
                    self.assertEqual(result[i], "FizzBuzz", msg=i)

    def test_multiples_of_three_but_not_five(self):
        result = fizzbuzz()
        for i in range(len(result)):
            if i % 3 == 0 and i % 5 != 0 and not has_5_in_digits(i):
                with self.subTest(i=i):
                    self.assertEqual(result[i], "Fizz", msg=i)

    def test_multiples_of_five_but_not_three(self):
        result = fizzbuzz()
        for i in range(len(result)):
            if i % 5 == 0 and i % 3 != 0 and not has_3_in_digits(i):
                with self.subTest(i=i):
                    self.assertEqual(result[i], "Buzz", msg=i)

    def test_rest_should_remain_same(self):
        result = fizzbuzz()
        for i in range(len(result)):
            if i % 3 != 0 and i % 5 != 0 and not has_3_in_digits(i) and not has_5_in_digits(i):
                with self.subTest(i=i):
                    self.assertEqual(result[i], i, msg=i)

    def test_numbers_ending_in_three(self):
        result = fizzbuzz()
        for i in range(len(result)):
            if i % 10 == 3 and not has_5_in_digits(i):
                with self.subTest(i=i):
                    self.assertEqual(result[i], "Fizz", msg=i)

    def test_numbers_ending_in_5_not_multiple_of_3(self):
        result = fizzbuzz()
        for i in range(len(result)):
            if i % 10 == 5 and i % 3 != 0 and not has_3_in_digits(i):
                with self.subTest(i=i):
                    self.assertEqual(result[i], "Buzz", msg=i)

    def test_numbers_ending_in_5_multiple_of_3(self):
        result = fizzbuzz()
        for i in range(len(result)):
            if i % 10 == 5 and i % 3 == 0:
                with self.subTest(i=i):
                    self.assertEqual(result[i], "FizzBuzz", msg=i)

    def test_numbers_beginning_with_3_not_multiple_of_5(self):
        result = fizzbuzz()
        for i in range(len(result)):
            if has_3_in_digits(i) and i % 5 != 0 and not has_5_in_digits(i):
                with self.subTest(i=i):
                    self.assertEqual(result[i], "Fizz", msg=i)
