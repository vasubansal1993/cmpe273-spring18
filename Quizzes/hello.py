from flask import Flask
from flask import request, jsonify
app = Flask(__name__)

users_details = []
id = 0
Dict_list={}
@app.route('/')
def hello():
    return "Hello World",200


#@app.route('/users',methods=['POST'])
#def new_users():
 #   name = request.form['name']
  #  return "hello{}!".format(name)  


@app.route('/users',methods=['POST'])
def new_user():
     global id
     id = id+1
     users_detail = {
                'id':id,
                'name':request.form['name']
                }
     users_details.append(users_detail)
     return jsonify({'User Deatils' : users_details}),201

@app.route('/users/<id>',methods=['GET'])#
def out(id):
    for i in range(len(users_details)):
        if int(users_details[i]['id']) == int(id):
            return jsonify({'User Deatils':users_details[i]}),200
     
@app.route('/users/<id>',methods=['DELETE'])
def delete_id(id):
    k=0
    for i in range(len(users_details)):
        if int(users_details[i]['id']) == int(id):
            k=i
    users_details.pop(k)
    return jsonify({'User Deatils': users_details}),204



    