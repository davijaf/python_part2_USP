import orderlist
import pytest

class TestOrder:

    @pytest.fixture
    def o(self):
        return orderlist.Order()

    @pytest.fixture
    def l(self):
        return orderlist.List()

    def is_ordered(self, list):
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                return False
        return True

    def test_bubble_mount_list(self,o,l):
        x = o.bubble(l.mount_list(100))
        assert self.is_ordered(x)

    def test_ds_mount_list(self,o,l):
        x = o.direct_selection(l.mount_list(100))
        assert self.is_ordered(x)

    def test_bubble_ef_mount_list(self,o,l):
        x = o.bubble_ef(l.mount_list(100))
        assert self.is_ordered(x)

    def test_sorted_mount_list(self,o,l):
        x = o.sorted(l.mount_list(100))
        assert self.is_ordered(x)

    def test_bubble_list_order(self,o,l):
        x = o.bubble(l.list_order(100))
        assert self.is_ordered(x)

    def test_ds_list_order(self,o,l):
        x = o.direct_selection(l.list_order(100))
        assert self.is_ordered(x)

    def test_bubble_ef_list_order(self,o,l):
        x = o.bubble_ef(l.list_order(100))
        assert self.is_ordered(x)

    def test_sorted_list_order(self,o,l):
        x = o.sorted(l.list_order(100))
        assert self.is_ordered(x)