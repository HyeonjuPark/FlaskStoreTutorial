from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# from datetime import datetime
# from .product import Product
# from .storesecond import Store
# from .employee import Employee
# from managestore.models import StoreDB

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from managestore import routes
# 판매로그 관리 db 생성

# def check_logged_in_user(request):
#     token = request.headers.get('Authorization')
    # if token:
        # jwt decode token => json: user_id, email, expiration_date
        # valid true false
        # pyjwt

# def init():
#     new_store = StoreDB(name='JARA', place='Suwon')
#     db.session.add(new_store)
#     db.session.commit()

# product = Product('jacket', 'top', 10000, 50000)
# product2 = Product('pants', 'bottom', 50000, 120000)
# employee = Employee('hjpark', 'manager', 2000000)
# employee2 = Employee('isseo', 'staff', 1800000)
# store = Store('JARA', 'Suwon')
# store.add_product(product)
# store.add_product(product)
# store.add_product(product2)
# store.hire_employee(employee)
# store.hire_employee(employee2)

# if __name__ == '__main__':
#     app.run(debug=True)