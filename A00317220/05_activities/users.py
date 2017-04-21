from flask import Flask, abort, request
import json

from users_commands import get_all_users, add_user, remove_user,reciente,history

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/users',methods=['POST'])
def create_user():
  content = request.get_json(silent=True)
  username = content['username']
  password = content['password']
  if not username or not password:
    return "empty username or password", 400
  if username in get_all_users():
    return "user already exist", 400
  if add_user(username,password):
    return "user created", 201
  else:
    return "error while creating user", 400

@app.route(api_url+'/users',methods=['GET'])
def read_user():
  list = {}
  list["users"] = get_all_users()
  return json.dumps(list), 200

@app.route(api_url+'/users',methods=['PUT'])
def update_user():
  return "not found", 404

@app.route(api_url+'/users',methods=['DELETE'])
def delete_user():
  error = False
  for username in get_all_users():
    if not remove_user(username):
        error = True

  if error:
    return 'some users were not deleted', 400
  else:

    return 'all users were deleted', 200


@app.route(api_url+'/users/<string:username>', methods=['GET'])
def read_one_user(username):
        return username, 200
		
		
		
@app.route(api_url+'/users/<string:username>', methods =['POST'])
def post_user():
 return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/users/<string:username>', methods =['PUT'])
def put_user():
 return "HTTP 404 NOT FOUND", 404


@app.route(api_url+'/users/<string:username>',methods=['DELETE'])
def delete_username(username):
 if user_data(username)== False:
 return "HTTP 404 NOT FOUND", 404
 else:
  remove_user(username);
  return 'usuario borrado',200		

@app.route(api_url+'/users/recently_logged', methods =['GET'])
def darReciente(): 
	list ={}
	list= reciente()
	return json.dumps(list),200

@app.route(api_url+'/users/recently_logged', methods =['POST'])
def create_reciente():
        return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/users/recently_logged', methods =['PUT'])
def update_reciente():
        return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/users/recently_logged', methods =['DELETE'])
def delete_reciente():
        return "HTTP 404 NOT FOUND", 404


		
@app.route(api_url+'/users/<string:username>/commands', methods =['GET'])
def history(username):


@app.route(api_url+'/users/<string:username>/commands', methods =['POST'])
def create_history():
 return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/users/<string:username>/commands', methods =['PUT'])
def update_history():
 return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/users/<string:username>/commands', methods =['DELETE'])
def delete_history():
 return ""HTTP 404 NOT FOUND", 404


  list = {}
  list =history(username);
  return json.dumps (list),200


  
		
		

if __name__ == "__main__":

  app.run(host='0.0.0.0',port=8080,debug='True')
