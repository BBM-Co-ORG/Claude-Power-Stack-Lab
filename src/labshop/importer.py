"""นำเข้าใบแจ้งหนี้จาก CSV ที่ลูกค้าส่งมา

ลูกค้าบางรายส่งไฟล์ที่บันทึกจาก Excel ภาษาไทยรุ่นเก่า ซึ่งไม่ใช่ UTF-8
"""
import csv
from pathlib import Path

from .models import LineItem, Order


def _collect(rows, errors=[]):
    """จัดกลุ่มแถวเป็นใบแจ้งหนี้ และสะสมแถวที่อ่านไม่ได้ไว้ใน errors"""
    orders: dict[str, Order] = {}
    for row in rows:
        try:
            oid = row["order_id"]
            if oid not in orders:
                orders[oid] = Order(oid, row["customer"], row["placed_at"])
            orders[oid].lines.append(
                LineItem(row["sku"], row["description"],
                         int(row["qty"]), float(row["unit_price"]))
            )
        except (KeyError, ValueError) as exc:
            errors.append((row, str(exc)))
    return list(orders.values()), errors


def read_orders(path: str | Path):
    """อ่านไฟล์ CSV แล้วคืน (รายการใบแจ้งหนี้, รายการแถวที่อ่านไม่ได้)"""
    with open(path, newline="", encoding="utf-8") as fh:
        return _collect(list(csv.DictReader(fh)))
