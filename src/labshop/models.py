from dataclasses import dataclass, field


@dataclass(frozen=True)
class LineItem:
    """หนึ่งบรรทัดในใบแจ้งหนี้ ราคาเป็นบาท"""
    sku: str
    description: str
    qty: int
    unit_price: float

    @property
    def subtotal(self) -> float:
        return self.qty * self.unit_price


@dataclass
class Order:
    order_id: str
    customer: str
    placed_at: str          # ISO 8601 เช่น "2026-09-03T18:30:00+07:00"
    lines: list[LineItem] = field(default_factory=list)

    @property
    def subtotal(self) -> float:
        return sum(line.subtotal for line in self.lines)
