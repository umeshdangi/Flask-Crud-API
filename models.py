from config import db

#ORM -> object is mapped with relational db
class Employee(db.Model):
    __tablename__ = 'EMP_MASTER'
    id = db.Column('emp_id',db.Integer(),primary_key=True)
    name = db.Column('emp_name',db.String(30))
    age  = db.Column('emp_age',db.Integer())
    salary = db.Column('emp_salary',db.Float())
    email = db.Column('emp_email',db.String(30),unique=True)
    contact = db.Column('emp_mobile',db.BigInteger(),unique=True)
    address = db.Column('emp_address',db.String(255))


if __name__ == '__main__':
    #create table
    db.create_all()     # its equivalent -->Create table -->
    e1 = Employee(id=101,name='XXXX',age=30,email='acb@gmail.com',salary=2893.34,address='Pune',contact=9988223344)
    #insert
    db.session.add(e1)
    db.session.commit()
