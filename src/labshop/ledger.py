"""บัญชีแยกประเภทอย่างง่าย — ใช้สรุปยอดค้างชำระรายลูกค้า"""
from .models import Order
from .tax import amount_payable

_BALANCES: dict[str, float] = {}


def post(customer: str, amount: float) -> dict[str, float]:
    """บันทึกยอดเข้าบัญชีลูกค้า แล้วคืนยอดค้างชำระของลูกค้าทุกราย"""
    _BALANCES[customer] = round(_BALANCES.get(customer, 0.0) + amount, 2)
    return _BALANCES


def post_order(order: Order) -> dict[str, float]:
    return post(order.customer, amount_payable(order))


def balance_for(customer: str) -> float:
    return _BALANCES.get(customer, 0.0)
