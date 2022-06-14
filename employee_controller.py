import json

from config import app


@app.route('/welcome',methods=['GET'])
def welcome_employee_api():
    return "API is up and Running..!"

from flask import request
from models import Employee
from config import db

@app.route('/emp/api/v1',methods=['POST'])  #http://localhost:5000/emp/api/v1  --> post
def save_employee():                           #{"EMP_ID":11,"EMP_NAME":........}
    reqdata = request.get_json()                # get_json --> request body == data
    if reqdata:
        e1 = Employee(id=reqdata.get('EMP_ID'),     # created model instance
                      name=reqdata.get('EMP_NAME'),
                      age=reqdata.get('EMP_AGE'),
                      email=reqdata.get('EMP_EMAIL'),
                      salary=reqdata.get('EMP_SALARY'),
                      address=reqdata.get('EMP_ADDRESS'),
                      contact=reqdata.get('EMP_CONTACT'))
        db.session.add(e1)
        db.session.commit()
        return json.dumps({"SUCCESS" : "Employee Record Saved Successfully....!"})
    else:
        return json.dumps({"ERROR":"Invalid Data"})

@app.route('/emp/api/v1/<int:eid>',methods=['DELETE'])
def delete_employee(eid):
    emp = Employee.query.filter_by(id=eid).first()    # select * from EMP_MASTER WHERE ID=EID
    if emp:
        db.session.delete(emp)
        db.session.commit()
        return json.dumps({"SUCCESS" : "Employee Record DELETE Successfully....!"})
    return json.dumps({"ERROR": "Employee Record With Given Id not present"})

@app.route('/emp/api/v1',methods=['GET'])
def get_all_emps():
    empList = Employee.query.all()                #select * from EMP_MASTER
    empJson = []
    for emp in empList:
        emp = {"EMP_ID" :emp.id,"EMP_NAME" : emp.name, "EMP_SALARY":emp.salary,
               "EMP_EMAIL" : emp.email,"EMP_ADDRESS": emp.address,"EMP_MOBILE":emp.contact}
        empJson.append(emp)
    return json.dumps(empJson)

@app.route('/emp/api/v1/<int:eid>',methods=['PUT'])
def update_employee(eid):
    emp = Employee.query.filter_by(id=eid).first()  # select * from EMP_MASTER WHERE ID=EID
    if emp:
        reqData = request.get_json()
        emp.name = reqData.get('EMP_NAME')
        emp.age = reqData.get('EMP_AGE')
        emp.contact = reqData.get('EMP_CONTACT')
        emp.email = reqData.get('EMP_EMAIL')
        emp.address = reqData.get('EMP_ADDRESS')
        emp.salary = reqData.get('EMP_SALARY')
        db.session.commit()         # whatever the data present--> update
        return json.dumps({"SUCCESS" : "Updated..."})
    return json.dumps({"ERROR": "Employee Record With Given Id not present"})

@app.route('/emp/api/v1/<int:eid>',methods=['GET'])
def search_employee_byid(eid):
    emp = Employee.query.filter_by(id=eid).first()
    if emp:
        return json.dumps({"EMP_ID" :emp.id,"EMP_NAME" : emp.name, "EMP_SALARY":emp.salary,
               "EMP_EMAIL" : emp.email,"EMP_ADDRESS": emp.address,"EMP_MOBILE":emp.contact})
    return json.dumps({"ERROR" : "No Records...!"})



if __name__ == '__main__':
    app.run(debug=True)
