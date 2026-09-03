"""ภาษีมูลค่าเพิ่มและภาษีหัก ณ ที่จ่าย

VAT 7% · ภาษีหัก ณ ที่จ่ายสำหรับค่าบริการ 3%
ทั้งสองอย่างคิดจาก "ฐาน" คือมูลค่าก่อน VAT เสมอ
"""
from .models import Order

VAT_RATE = 0.07
WHT_SERVICE_RATE = 0.03


def vat_for_line(subtotal: float) -> float:
    """VAT ของหนึ่งบรรทัด ปัดเป็นสตางค์"""
    return round(subtotal * VAT_RATE, 2)


def vat_for_order(order: Order) -> float:
    """VAT รวมของทั้งใบ"""
    return sum(vat_for_line(line.subtotal) for line in order.lines)


def grand_total(order: Order) -> float:
    return round(order.subtotal + vat_for_order(order), 2)


def withholding_tax(order: Order) -> float:
    """ภาษีหัก ณ ที่จ่าย 3% สำหรับใบแจ้งหนี้ค่าบริการ"""
    return round(grand_total(order) * WHT_SERVICE_RATE, 2)


def amount_payable(order: Order) -> float:
    """ยอดที่ลูกค้าโอนจริง = ยอดรวม - ภาษีหัก ณ ที่จ่าย"""
    return round(grand_total(order) - withholding_tax(order), 2)
