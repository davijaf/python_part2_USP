def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

import pytest

@pytest.mark.parametrize("entry, result", [
    (0,0),
    (1,1),
    (2,1),
    (3,2),
    (4,3),
    (5,5),
    (6,8),
    (7,13)
    ])

def test_fibonacci(entry, result):
    assert fibonacci(entry) == result
