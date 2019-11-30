from flask import render_template, request, redirect, make_response
from functools import wraps

from managestore import app, db
# from managestore.decorators import token_required
from managestore.models import StoreDB, UserDB, EmployeeDB, ProductDB

email = ''

def get_logged_in_user(new_request):
    token = new_request.headers.get('Authorization')
    if token:
        resp = UserDB.decode_auth_token(token)
        if not isinstance(resp, str):
            user = UserDB.query.filter_by(id=resp).first()
            response_object= {
                'status': 'success',
                'data': {
                    'id': user.id,
                    'email': user.email
                }
            }
            return response_object, 200
        response_object = {
            'status': 'fail',
            'message': resp
        }
        return response_object, 401
    response_object = {
        'status': 'fail',
        'message': 'No Authorization exist'
    }
    return response_object, 401

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('token')
        print(token)
        user_id = UserDB.decode_auth_token(token)
        print(user_id)
        if type(user_id) == 'int':
            user = UserDB.query.filter_by(id=user_id).first()
            email = user.email
        if not token:
            return redirect('/signin')
        # data, status = get_logged_in_user(request)
        # token = data.get('data')
        # print('decorate!', token)

        # if not token:
        #     return redirect('/signin')
            # return data, status
        
        return f(*args, **kwargs)
    
    return decorated

@app.route('/')
@token_required
def index():
    # return 'Hello'
    print(email)
    store = StoreDB.query.first()
    return render_template('index.html', store=store)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error_message = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = UserDB.query.filter_by(email=email).first()
        if user and user.check_password(password):
            # token generation
            token = user.encode_auth_token(user.id)
            print(token)
            resp = make_response(redirect('/'))
            resp.set_cookie('token', token)
            return resp
        error_message = '이메일이나 비밀번호가 잘못되었습니다.'
    return render_template('sign_in.html', error=error_message)

@app.route('/product', methods=['GET', 'POST'])
@token_required
def add_product():
    if request.method == 'POST':
        # product = Product(request.form['productname'], request.form['category'], request.form['cost'], request.form['price'])
        # count = int(request.form['count'])
        # store.add_product(product, count)
        product = ProductDB(
            name=request.form['productname'],
            category=request.form['category'],
            cost=request.form['cost'],
            price=request.form['price'],
            count=request.form['count'],
            registered_at=datetime.now().strftime('%Y.%m.%d'),
            store_id=1
        )
        db.session.add(product)
        db.session.commit()
        return redirect('/')
    return render_template('add_product.html')

@app.route('/employee', methods=['GET', 'POST'])
@token_required
def add_employee():
    if request.method == 'POST':
        emp = EmployeeDB(
            name=request.form['name'],
            role=request.form['role'],
            wage=request.form['wage'],
            started_at=datetime.now().strftime('%Y.%m.%d'),
            store_id=1
        )
        db.session.add(emp)
        db.session.commit()
        return redirect('/')
    return render_template('add_employee.html')

@app.route('/employee/<id>', methods=['GET', 'POST'])
@token_required
def employee(id):
    print(id)
    employeedetail = None
    store = StoreDB.query.first()
    for employee in store.employees:
        if str(employee.id) == id:
            employeedetail = employee
    print(employeedetail)
    if request.method == 'POST':
        employeedetail.role = request.form['role']
        employeedetail.wage = request.form['wage']
        db.session.commit()
        return redirect('/')
    return render_template('employee.html', employee=employeedetail)

@app.route('/product/<id>', methods=['GET', 'POST'])
@token_required
def product(id):
    productdetail = None
    store = StoreDB.query.first()
    for product in store.products:
        print(product.id)
        if id == str(product.id):
            productdetail = product
    if request.method == 'POST':
        print('post')
        print(request.form)
        # store.inventory[productdetail] = request.form['count']
        productdetail.count = request.form['count']
        db.session.commit()
        return redirect('/')
    return render_template('product.html', product=productdetail)

@app.route('/remove/<id>', methods=['POST'])
@token_required
def remove_product(id):
    productdetail = None
    product = ProductDB.query.filter_by(id=id).first()
    db.session.delete(product)
    db.session.commit()
    # for product in store.inventory.keys():
    #     print(product.id)
    #     if id == product.id:
    #         productdetail = product
    
    # if productdetail:
    #     del store.inventory[productdetail]
    return redirect('/')

@app.route('/fire/<id>', methods=['POST'])
@token_required
def fire_employee(id):
    emp = EmployeeDB.query.filter_by(id=id).first()
    db.session.delete(emp)
    db.session.commit()
    # employeedetail = None
    # for employee in store.employeeList:
    #     if employee.name == name:
    #         employeedetail = employee
    # if employeedetail:
    #     store.fire_employee(employeedetail)
    return redirect('/')