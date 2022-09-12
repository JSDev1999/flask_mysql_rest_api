from app import app
from models.user_model import user_model
from flask import request

obj = user_model()

# routes
@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()

@app.route('/user/addone', methods=['POST'])
def user_addone_controller():
    print(request.json)
    return obj.user_addone_model(request.json)