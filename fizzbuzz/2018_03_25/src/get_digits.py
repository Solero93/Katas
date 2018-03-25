from typing import List


def get_digits(number: int) -> List[int]:
    return [int(digit) for digit in str(number)]
