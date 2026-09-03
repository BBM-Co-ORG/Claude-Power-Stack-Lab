from labshop import pagination

ITEMS = list(range(1, 24))   # 23 รายการ


def test_จำนวนหน้าต้องรวมหน้าสุดท้ายที่ไม่เต็ม():
    """23 รายการ หน้าละ 10 ต้องได้ 3 หน้า ไม่ใช่ 2"""
    assert pagination.total_pages(ITEMS, 10) == 3


def test_หน้าสุดท้ายมีของเหลืออยู่จริง():
    assert pagination.page(ITEMS, 10, 3) == [21, 22, 23]


def test_page_size_เป็นศูนย์ต้อง_error():
    import pytest
    with pytest.raises(ValueError):
        pagination.total_pages(ITEMS, 0)
