from acme import Product
from acme_report import generate_products


def test_default_product_price():
    '''Test default product price being 10.'''
    assert Product('Test Product').price == 10


def test_stealability():

    assert Product(name='x',
                   price=1,
                   weight=1).stealability == "Very stealable!"

    assert Product(name='x',
                   price=0.5,
                   weight=1).stealability == "Kinda stealable."

    assert Product(name='x',
                   price=0.1,
                   weight=1).stealability == "Not so stealable..."


def test_explode():

    assert Product(name='x',
                   flammability=1,
                   weight=1).explode == "...fizzle."

    assert Product(name='x',
                   flammability=10,
                   weight=1).explode == "...boom!"

    assert Product(name='x',
                   flammability=10,
                   weight=5).explode == "...BABOOM!!"


def test_default_generate_products():
    assert len(generate_products()) == 30
