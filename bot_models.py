class Product:
    def __init__(self, brand, store, price, url ):
        self.brand = brand
        self.store = store
        self.price = price
        self.url = url

class RTX_3080(Product):
    def __init__(self, brand, store, price, url):
        self.product_name = 'RTX 3080'
        self.max_price = 850
        super().__init__(brand, store, price, url)

class RTX_3070(Product):
    def __init__(self, brand, store, price, url):
        self.product_name = 'RTX 3070'
        self.max_price = 670
        super().__init__(brand, store, price, url)

class RTX_3060ti(Product):
    def __init__(self, brand, store, price, url):
        self.product_name = 'RTX 3060ti'
        self.max_price = 500
        super().__init__(brand, store, price, url)

class PS5(Product):
    def __init__(self, brand, store, price, url):
        self.product_name = 'Playstation 5'
        self.max_price = 600
        super().__init__(brand, store, price, url)
class XBOX(Product):
    def __init__(self, brand, store, price, url):
        self.product_name = 'Xbox Series X'
        self.max_price = 600
        super().__init__(brand, store, price, url)
    