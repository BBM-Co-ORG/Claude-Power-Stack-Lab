"""เทสที่ไม่เสถียร — บางรอบผ่าน บางรอบไม่ผ่าน โดยที่โค้ดไม่ได้เปลี่ยน

อย่า "แก้" ด้วยการรันซ้ำจนผ่าน ให้หาสาเหตุว่าทำไมผลถึงไม่คงที่
"""
from datetime import datetime

from labshop import tax
from labshop.models import LineItem, Order


def _order_with_timestamp() -> Order:
    now = datetime.now()
    qty = 1 + (now.microsecond % 2)
    return Order("INV-TMP", "ลูกค้าทดสอบ", now.isoformat(),
                 [LineItem("SKU-X", "ค่าบริการ", qty, 100.00)])


def test_vat_ของใบชั่วคราว():
    order = _order_with_timestamp()
    assert tax.vat_for_order(order) == 7.00
