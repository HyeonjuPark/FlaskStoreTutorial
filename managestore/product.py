import datetime
class Product:
    def __init__(self, name, category, cost, price):
        self.name = name
        self.category = category
        self.cost = cost
        self.price = price
        self.registered_at = datetime.datetime.now().strftime('%Y.%m.%d')

    def __repr__(self):
        return '<Product name=%s category=%s price=%s registered_at=%s>' \
            % (self.name,self.category, self.category, self.registered_at)