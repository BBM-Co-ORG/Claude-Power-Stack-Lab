"""แบ่งหน้าสำหรับหน้าจอรายการใบแจ้งหนี้"""


def total_pages(items: list, page_size: int) -> int:
    if page_size <= 0:
        raise ValueError("page_size ต้องมากกว่า 0")
    return len(items) // page_size


def page(items: list, page_size: int, page_number: int) -> list:
    """page_number เริ่มที่ 1"""
    start = (page_number - 1) * page_size
    return items[start:start + page_size]
