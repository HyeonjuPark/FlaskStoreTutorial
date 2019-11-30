from datetime import datetime, timedelta
import jwt
from managestore import db, bcrypt

key = 'secretkey'

class StoreDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    place = db.Column(db.String(50))
    products = db.relationship('ProductDB', backref='store', lazy=True)
    employees = db.relationship('EmployeeDB', backref='store', lazy=True)

    def __repr__(self):
        return f"Store('{self.name}', '{self.place}')"

class ProductDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, default=1)
    registered_at = db.Column(db.String(50))
    store_id = db.Column(db.Integer, db.ForeignKey('storeDB.id'), nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.category}', '{self.cost}', '{self.price}')"

class EmployeeDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50))
    wage = db.Column(db.Integer)
    started_at = db.Column(db.String(50))
    store_id = db.Column(db.Integer, db.ForeignKey('storeDB.id'), nullable=False)

    def __repr__(self):
        return f"Employee('{self.name}','{self.role}','{self.wage}')"

class UserDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def encode_auth_token(self, user_id):
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=1, seconds=5),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                key,
                algorithm='HS256'
            )
        except Exception as e:
            return e
    
    @staticmethod
    def decode_auth_token(token):
        try:
            payload = jwt.decode(token, key)
            # is_blacklisted_token = BlacklistToken.check_blacklist(token)
            # if is_blacklisted_token:
            #     return 'Token blacklisted. Please Login again'
            # # else:
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature Expired. Please Login again'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please Login again'
    
    def __repr__(self):
        return f"User({self.email})"