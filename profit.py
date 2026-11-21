"""Task 2: find income numbers in a text with a generator and sum them."""

import re
from typing import Callable, Iterator

# A real number (e.g. 1000.01 or 324) with a space before and after it
NUMBER_PATTERN = re.compile(r"(?<= )\d+(?:\.\d+)?(?= )")


def generator_numbers(text: str) -> Iterator[float]:
    """Yield every real number from the text, one by one."""
    for match in NUMBER_PATTERN.finditer(text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Iterator[float]]) -> float:
    """Sum all numbers that the generator function `func` finds in the text."""
    total = sum(func(text))
    return round(total, 2)  # avoid float artifacts like 1351.4600000000001


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
