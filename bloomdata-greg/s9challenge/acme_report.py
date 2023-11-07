import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):

    """
    returns a list of randomly generated products
    """

    products = []

    for _ in range(num_products):
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        products.append(Product(name=name,
                                price=random.randint(5, 100),
                                weight=random.randint(5, 100),
                                flammability=random.uniform(0.0, 2.5)))

    return products


def inventory_report(product_list):

    """
    takes in a list of products and returns of tuple of statistics
    """

    names = set()
    prices = []
    weights = []
    flame = []

    for product in product_list:
        names.add(product.name)
        prices.append(product.price)
        weights.append(product.weight)
        flame.append(product.flammability)

    av_price = sum(prices) / len(prices)
    av_weight = sum(weights) / len(weights)
    av_flame = sum(flame) / len(flame)

    return (len(names), av_price, av_weight, av_flame)


if __name__ == '__main__':
    print(inventory_report(generate_products()))
