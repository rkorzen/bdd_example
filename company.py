from dataclasses import dataclass, field
from functools import partial
from product import Product

without_init = partial(field, init=False, default=0)


@dataclass
class Company:
    name: str
    income_tax_rate: int
    vat_to_pay: float = without_init()
    income_tax_to_pay: float = without_init()
    income: float = without_init()

    def sell(self, product: Product) -> 'Company':
        self.income += product.price
        self.vat_to_pay += round((product.price * product.vat_rate) / (100 + product.vat_rate), 2)
        self.income_tax_to_pay += (self.income_tax_rate * (product.price - product.vat_value)) / 100
        return self

    def buy(self, product: Product) -> 'Company':
        vat_of_product = product.vat_value
        self.vat_to_pay -= vat_of_product
        self.income_tax_to_pay -= (self.income_tax_rate * (product.price - vat_of_product)) / 100
        return self

    def get_taxes(self):
        return round(self.vat_to_pay, 2), round(self.income_tax_to_pay, 2)

    def get_real_income(self):
        return round(self.income - self.income_tax_to_pay - self.vat_to_pay, 2)
