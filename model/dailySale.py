from dataclasses import dataclass
from datetime import datetime


@dataclass
class DailySale:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: datetime
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

