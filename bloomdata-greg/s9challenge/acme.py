import random


class Product:

    '''
    generic acme product class
    '''

    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):

        '''
        calculates how likely a product is be stolen
        '''

        s = self.price / self.weight
        if s < 0.5:
            return "Not so stealable..."
        elif 0.5 <= s < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):

        '''
        calculates the size of the product's explosion
        '''

        e = self.flammability * self.weight
        if e < 10:
            return "...fizzle."
        elif 10 <= e < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):

    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):

        '''
        calculates the pain inflicted by a punch with the glove
        '''

        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
