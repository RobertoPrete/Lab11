from dataclasses import dataclass
from datetime import datetime

from model.product import Product


@dataclass
class Arco:
    Retailer_code: int
    p1: Product
    p2: Product
    Date: datetime

