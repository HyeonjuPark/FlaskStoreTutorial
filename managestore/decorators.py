from functools import wraps
from flask import request, redirect

from managestore.models import UserDB

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

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = get_logged_in_user(request)
        token = data.get('data')
        print(token)

        # if not token:
        #     return redirect('/signin')
            # return data, status
        
        return f(*args, **kwargs)
    
    return decorated
