# -*- encoding:utf-8 -*-
from .product import Product
from .employee import Employee

class Store:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.employeeList = []
        self.inventory = {}
        self.inventorySold = {}

    def list_product(self):
        for product in self.inventory.keys():
            print('%s: %s개' % (product.name, self.inventory[product]))

    def sell_product(self, productName):
        for product in self.inventory.keys():
            if product.name == productName:  # and not product.isSold:
                self.inventory[product] -= 1
                if self.inventorySold.get(product):
                    self.inventorySold[product] += 1
                else:
                    self.inventorySold[product] = 1
                return True
        print('재고가 없습니다.')
        return False
    
    def add_product(self, product, count=1):
        if self.inventory.get(product):
            self.inventory[product] += count
        else:
            self.inventory[product] = count

    def list_employee(self):
        print(self.employeeList)

    def hire_employee(self, employee):
        self.employeeList.append(employee)
    
    def fire_employee(self, employee):
        self.employeeList.remove(employee)
    
    def total_sales(self):
        total = 0
        for product in self.inventorySold.keys():
            total += product.price * self.inventorySold[product]
        return total

    def total_profit(self):
        total = 0
        totalWage = 0
        for employee in self.employeeList:
            totalWage += employee.wage
        for product in self.inventorySold.keys():
            total += (product.price - product.cost) * self.inventorySold[product]
        return total - totalWage

    def __repr__(self):
        return '<Store name=%s place=%s>' % (self.name, self.place)

if __name__ == '__main__':
    product = Product('jacket', 'top', 10000, 50000)
    product2 = Product('pants', 'bottom', 50000, 120000)
    employee = Employee('hjpark', 'manager', 2000000)
    employee2 = Employee('isseo', 'staff', 1800000)
    store = Store('JARA', 'Suwon')
    store.add_product(product)
    store.add_product(product)
    store.add_product(product2)
    store.list_product()
    store.hire_employee(employee)
    store.hire_employee(employee2)
    store.list_employee()
    store.fire_employee(employee2)
    store.list_employee()
    store.sell_product('jacket')
    print('total sales', store.total_sales())
    print('total profit', store.total_profit())