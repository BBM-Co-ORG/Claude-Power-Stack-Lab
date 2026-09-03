"""วันที่แบบไทย — แปลง พ.ศ. เป็น ค.ศ. และคำนวณวันครบกำหนด"""
from datetime import datetime, timedelta, timezone

BANGKOK = timezone(timedelta(hours=7))
DEFAULT_TERMS_DAYS = 30


def parse_thai_date(text: str) -> datetime:
    """รับ 'YYYY-MM-DD' ที่ปีอาจเป็น พ.ศ. หรือ ค.ศ. แล้วคืนค่าเป็น ค.ศ.

    ตัวอย่าง: '2569-09-03' (พ.ศ.) และ '2026-09-03' (ค.ศ.) ต้องได้ผลเท่ากัน
    """
    year_s, month_s, day_s = text.split("-")
    year = int(year_s)
    if year > 2500:
        year -= 543
    return datetime(year, int(month_s), int(day_s), tzinfo=BANGKOK)


def due_date(placed_at_iso: str, terms_days: int = DEFAULT_TERMS_DAYS) -> str:
    """คืนวันครบกำหนดเป็น 'YYYY-MM-DD' ตามเวลาประเทศไทย"""
    placed = datetime.fromisoformat(placed_at_iso)
    due = placed.astimezone(timezone.utc) + timedelta(days=terms_days)
    return due.strftime("%Y-%m-%d")
