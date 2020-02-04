from behave import *
from company import Company, Product


@given("I own company called '{name}' with income tax rate {income_tax_rate}")
def step_impl(context, name, income_tax_rate):
    context.company = Company(name, int(income_tax_rate))


@when("I sell {name} for {value} with vat rate {vat_rate}")
def step_impl(context, name, value, vat_rate):
    context.company.sell(Product(name, float(value), int(vat_rate)))


@when("I buy {name} for {price} with vat rate {vat_rate}")
def step_impl(context, name, price, vat_rate):
    product = Product(name, float(price), int(vat_rate))
    context.company.buy(product)


@then("my real income will be {income}")
def step_impl(context, income):
    assert context.company.get_real_income() == float(income)


@then("vat will be equal {vat_value} and income tax {income_tax_value}")
def step_impl(context, vat_value, income_tax_value):
    assert context.company.get_taxes() == (float(vat_value), float(income_tax_value))
