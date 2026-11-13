import re
from typing import Callable

def generator_numbers(text: str):
    for x in re.findall(r'\d+(?:\.\d+)?', text):
        yield float(x)


def sum_profit(text: str, func: Callable):
    return sum(func(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_profit = sum_profit(text, generator_numbers)
print(f"Загальний дохід працівника: {total_profit:.2f} доларів.")