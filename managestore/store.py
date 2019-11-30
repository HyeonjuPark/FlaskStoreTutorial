# -*- encoding:utf-8 -*-
from product import Product
from employee import Employee

class Store:
    def __init__(self, name, place):
        self.name = name
        self.place = place
        self.employeeList = []
        self.productList = []
        self.soldProductList = []
        self.inventory = {}
        # self.productInventory = {<key: product object> : <value: count>}
        # self.soldProductInventory = {<key: product object> : <value: count>}

    def list_product(self):
        for key in self.inventory.keys():
            print('%s: %s개' % (key, self.inventory[key]))
        # print(self.productList)
        # for product in self.productList:
        #     print(product)

    def sell_product(self, productName):
        for product in self.productList:
            if product.name == productName: # and not product.isSold:
                # product.isSold = True
                self.productList.remove(product)
                self.soldProductList.append(product)
                self.inventory[productName] -= 1
                return True
        print('재고가 없습니다.')
        return False
    
    def add_product(self, product):
        self.productList.append(product)
        if self.inventory.get(product.name):
            self.inventory[product.name] += 1
        else:
            self.inventory[product.name] = 1

    def list_employee(self):
        print(self.employeeList)

    def hire_employee(self, employee):
        self.employeeList.append(employee)
    
    def fire_employee(self, employee):
        self.employeeList.remove(employee)
    
    def total_sales(self):
        total = 0
        for product in self.soldProductList:
            total += product.price
        return total

    def total_profit(self):
        total = 0
        totalWage = 0
        for employee in self.employeeList:
            totalWage += employee.wage
        for product in self.soldProductList:
            total += product.price - product.cost
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