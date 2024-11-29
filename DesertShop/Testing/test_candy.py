from dessert import Candy

def test_candy_init():
    candy = Candy("Chocolate", 3.5, 1.5)
    name = candy.get_name()
    assert name == "Chocolate"
    weight = candy.get_candy_weight()
    assert weight == 3.5
    price = candy.get_price_per_pound()
    assert price == 1.5
def test_tax_percent():
    candy1 = Candy("Chocolate", 3.5, 1.5)
    assert candy1.tax_percent == 7.25
def test_calculate_cost():
    candy = Candy("Chocolate", 3.5, 1.5)
    cost = candy.get_candy_weight() * candy.get_price_per_pound()
    assert candy.calculate_cost() == cost
def test_packaging():
    candy = Candy("Chocolate", 3.5, 1.5)
    assert candy.packaging == "Bag"
    