from typing import List

from src.get_digits import get_digits


def fizzbuzz() -> List:
    result = [''] * 100
    for i in range(100):
        digits = get_digits(i)
        is_multiple_or_has_five = i % 5 == 0 or 5 in digits
        is_multiple_or_has_three = i % 3 == 0 or 3 in digits

        if is_multiple_or_has_five and is_multiple_or_has_three:
            result[i] = "FizzBuzz"
        elif is_multiple_or_has_three:
            result[i] = "Fizz"
        elif is_multiple_or_has_five:
            result[i] = "Buzz"
        else:
            result[i] = i
    return result
