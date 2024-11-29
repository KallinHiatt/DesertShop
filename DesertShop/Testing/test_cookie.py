from dessert import Cookie

def test_cookie_init():
    cookie = Cookie("Chocolate chip", 12, 15.60)
    name = cookie.get_name()
    assert name == "Chocolate chip"
    quant = cookie.get_cookie_quantity()
    assert quant == 12
    price = cookie.get_price_per_dozen()
    assert price == 15.60
def test_calculate_cost():
    cookie = Cookie("Chocolate chip", 12, 15.60)
    cost = cookie.get_cookie_quantity() * (cookie.get_price_per_dozen()/12)
    assert cookie.calculate_cost() == cost
def test_packaging():
    cookie = Cookie("Chocolate chip", 12, 15.60)
    assert cookie.packaging == "Box"