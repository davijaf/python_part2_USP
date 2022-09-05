def merge_sort(list):
    if len(list) <= 1:
        return list

    quote = len(list) // 2

    left_side = merge_sort(list[:quote])
    right_side = merge_sort(list[quote:])

    return merge(left_side,right_side)

def merge(left_side,right_side):
    if not left_side:
        return right_side

    if not right_side:
        return left_side

    if left_side[0] < right_side[0]:
        return [left_side[0]] + merge(left_side[1:],right_side)

    return [right_side[0]] + merge(left_side, right_side[1:])

import pytest

@pytest.mark.parametrize("entry, result", [
    ([9,1,2,3,4,5,6,7,8,0],[0,1,2,3,4,5,6,7,8,9]),
    ([9,8,7,6,5,4,3,2,1,0],[0,1,2,3,4,5,6,7,8,9]),
    ([1,3,5,7,9,0,2,4,6,8],[0,1,2,3,4,5,6,7,8,9]),
    ([0],[0]),
    ([1,0],[0,1]),
    ([8,0,2,1,4,3,5,7,6,-1],[-1,0,1,2,3,4,5,6,7,8]),
    ([0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]),
    ])

def test_merge_sort(entry, result):
    assert merge_sort(entry) == result