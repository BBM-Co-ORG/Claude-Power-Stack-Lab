from labshop import tax


def test_vat_รวมทั้งใบต้องปัดครั้งเดียวจากยอดรวม(order_two_lines):
    """VAT ของทั้งใบต้องคิดจากยอดรวมก่อน แล้วค่อยปัดครั้งเดียว

    ยอดรวม 9985.08 → round(9985.08 x 0.07, 2) = 698.96
    """
    assert tax.vat_for_order(order_two_lines) == 698.96


def test_ยอดรวมของใบบรรทัดเดียว(order_single_line):
    assert tax.grand_total(order_single_line) == 48150.00


def test_ภาษีหัก_ณ_ที่จ่าย(order_single_line):
    assert tax.withholding_tax(order_single_line) == 1444.50


def test_ยอดที่ลูกค้าโอนจริง(order_single_line):
    assert tax.amount_payable(order_single_line) == 46705.50
