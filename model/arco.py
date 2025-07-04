from dataclasses import dataclass
from datetime import datetime

from model.product import Product


@dataclass
class Arco:
    Retailer_code: int
    p1: Product
    p2: Product
    Date: datetime

    def __eq__(self, other):
        return self.Retailer_code == other.Retailer_code and self.Date == other.Date and self.p1 == other.p1 and self.p2 == other.p2
