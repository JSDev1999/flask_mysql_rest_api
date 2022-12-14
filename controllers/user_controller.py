from app import app
from models.user_model import user_model
from flask import request

obj = user_model()

# -------/ routes /--------
# -------/ get all users route /-------
@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()
# -------/ get add users route /-------
@app.route('/user/addone', methods=['POST'])
def user_addone_controller():
    print(request.json)
    return obj.user_addone_model(request.json)

# -------/ get update user route /-------
@app.route('/user/update', methods=['PUT'])
def user_update_controller():
    print(request.json)
    return obj.user_update_model(request.json)

# -------/ get delete user route /-------
@app.route('/user/delete/<id>', methods=['DELETE'])
def user_delete_controller(id):
    print(id)
    return obj.user_delete_model(id)