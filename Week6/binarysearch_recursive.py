import pytest

def search_binary(list, element, min=0, max=None):
    if max == None:
        max = len(list)-1
    if max < min:
        return False
    else:
        quote = min + (max-min)//2
    if list[quote] > element:
        return search_binary(list, element, min, quote-1)
    elif list[quote] < element:
        return search_binary(list, element, quote+1, max)
    else:
        return quote

a = [10,20,30,40,50,60]
@pytest.mark.parametrize("list,value,index", [
    (a,10,0),
    (a,20,1),
    (a,30,2),
    (a,40,3),
    (a,50,4),
    (a,60,5),
    (a,70,False),
    (a,15,False),
    (a,-10,False)
])

def test_search_binary(list,value,index):
    assert search_binary(list,value) == index