def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n-1)

import pytest

@pytest.mark.parametrize("entry, result", [
    (0,1),
    (1,1),
    (2,2),
    (3,6),
    (4,24),
    (5,120)
    ])

def test_factorial(entry, result):
    assert factorial(entry) == result
