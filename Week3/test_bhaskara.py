import bhaskara
import pytest

class TestBhaskara:

    @pytest.mark.parametrize("a,b,c,v1,v2,v3", [
    (1, 0, 0, 1, 0),
    (1, -5, 6, 2, 3, 2),
    (10, 10, 10, 0),
    (10, 20, 10, 1, -1),
    ])

    @pytest.fixture
    def e(self):
        return bhaskara.Bhaskara()

    def testa_uma_raiz(self,e):
        assert e.calc_discriminant(a,b,c) == (v1,v2,v3)
