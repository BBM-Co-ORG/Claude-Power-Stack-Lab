from pathlib import Path

from labshop import importer

DATA = Path(__file__).resolve().parent.parent / "data"


def test_อ่านไฟล์_utf8_ได้ครบทุกใบ():
    orders, errors = importer.read_orders(DATA / "orders_utf8.csv")
    assert len(orders) == 3
    assert errors == []


def test_อ่านไฟล์ที่บันทึกจาก_excel_ภาษาไทยรุ่นเก่าได้():
    """ลูกค้าบางรายส่งไฟล์ TIS-620 มา ระบบต้องอ่านได้ ไม่ใช่พัง"""
    orders, _ = importer.read_orders(DATA / "orders_tis620.csv")
    assert len(orders) == 3
    assert orders[0].customer == "บริษัท กรุงเทพ ซัพพลาย จำกัด"


def test_แถวที่เสียต้องถูกเก็บไว้ใน_errors():
    orders, errors = importer.read_orders(DATA / "orders_broken.csv")
    assert len(errors) == 1
