import pytest
from labshop.models import LineItem, Order


@pytest.fixture
def order_two_lines() -> Order:
    """ยอด 3600.03 + 6385.05 = 9985.08

    ปัด VAT รายบรรทัดแล้วรวม ได้ 698.95
    รวมก่อนแล้วปัดครั้งเดียว ได้ 698.96 — ต่างกันหนึ่งสตางค์
    """
    return Order(
        "INV-2601", "บริษัท กรุงเทพ ซัพพลาย จำกัด", "2026-09-03T18:30:00+07:00",
        [
            LineItem("SKU-A", "ค่าที่ปรึกษา รายเดือน", 3, 1200.01),
            LineItem("SKU-B", "ค่าอบรม ต่อคน", 7, 912.15),
        ],
    )


@pytest.fixture
def order_single_line() -> Order:
    return Order(
        "INV-2602", "ห้างหุ้นส่วน สยามเทค", "2026-09-01T09:15:00+07:00",
        [LineItem("SKU-C", "ค่าบำรุงรักษาระบบ", 1, 45000.00)],
    )
