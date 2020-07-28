# from trainer import Trainer
from course import Course
from employee import Employee
from address import Address
from enrollment import Enrollment
from datetime import datetime

id_addresses = ['adr1', 'adr2', 'adr3', 'adr4', 'adr5', 'adr6', 'adr7']
id_employees = ['emp1', 'emp2', 'emp3', 'emp4']
id_trainers = ['tra1', 'tra2']
id_courses = ['cou1', 'cou2', 'cou3', 'cou4', 'cou5']

dict_address = {
    'adr1': ['Poland', 'Krosno', 'Pilsudskiego 3', '20-132'],
    'adr2': ['Germany', 'Berlin', 'Adolfa 3', '12-677'],
    'adr3': ['Poland', 'Krakow', 'Krakowska 3', '11-112'],
    'adr4': ['Poland', 'Krakow', 'Ruczaj 3', '22-362'],
    'adr5': ['Poland', 'Tarnow', 'Tarnowska 13', '32-322'],
    'adr6': ['Poland','Krakow','Pradnik 13', '11-111'],
    'adr7': ['France','Paris','Saint Street 1', '55-213']
}

dict_person = {
    'emp1': ['Artur', 'Skrzeta', '+48 727 929 994', datetime(1993,4,20)],
    'emp2': ['Zbyszek', 'Kowal', '+48 333 929 111', datetime(1990,2,21)],
    'emp3': ['Maria', 'Nowak', '+48 123 555 678', datetime(1996,11,1)],
    'emp4': ['Karol', 'Zych', '+48 455 155 998', datetime(1991,3,11)],
    'tra1': ['John', 'Smith', '+48 566 532 123', datetime(1987,12,24)],
    'tra2': ['Mike', 'Thomson', '+48 987 924 001', datetime(1985,9,8)]
}

dict_employee = {
    'emp1': ['Data Analyst', False, datetime(2019,1,20)],
    'emp2': ['Software Enginner', True, datetime(2018,1,1)],
    'emp3': ['Strategic Buyer', False, datetime(2014,7,22)],
    'emp4': ['Operational Buyer', False, datetime(2015,11,1)]
}

dict_trainer = {
    'tra1': ['Data Analysis with Python', 10000.00],
    'tra2': ['RPA Specialization', 8000.00]
}

dict_course = {
    'cou1': ['Basic Python','BPY001', 3, 2],
    'cou2': ['Intermediate Python','IPY001', 3, 2],
    'cou3': ['Advanded Python','APY001', 3, 2],
    'cou4': ['RPA introduction','RPAI001', 3, 2],
    'cou5': ['RPA for SAP automation','RPAS001', 3, 2]
}

def create_address_objects():
    obj_addresses = []
    for id in id_addresses:
        a = Address(id, dict_address[id][0], dict_address[id][1], dict_address[id][2], dict_address[id][3])
        obj_addresses.append(a)
    return obj_addresses

def associate_address_with_person(addresses):
    for key in dict_person:
        if key == 'emp1': dict_person[key].append([addresses[0],addresses[2]])
        if key == 'emp2': dict_person[key].append(addresses[3])
        if key == 'emp3': dict_person[key].append(addresses[1])
        if key == 'emp4': dict_person[key].append(addresses[4])
        if key == 'tra1': dict_person[key].append(addresses[6])
        if key == 'tra2': dict_person[key].append(addresses[5])

def create_employee_objects():
    obj_employees =[]
    for id in id_employees:
        e = Employee(id, dict_person[id][0], dict_person[id][1], dict_person[id][2], dict_person[id][3], dict_person[id][4],
                        dict_employee[id][0], dict_employee[id][1], dict_employee[id][2])
        obj_employees.append(e)
    return obj_employees

def create_trainer_objects():
    obj_trainer = []
    for id in id_trainers:
        t = Trainer(id, dict_person[id][0], dict_person[id][1], dict_person[id][2], dict_person[id][3], dict_person[id][4],
                        dict_trainer[id][0], dict_trainer[id][1])
        obj_trainer.append(t)
    return obj_trainer

def associate_trainer_with_course(trainers):
    for key in dict_course:
        if key == 'cou1': dict_course[key].append(trainers[0])
        if key == 'cou2': dict_course[key].append(trainers[0])
        if key == 'cou3': dict_course[key].append(trainers[0])
        if key == 'cou4': dict_course[key].append(trainers[1])
        if key == 'cou5': dict_course[key].append(trainers[1])

def create_course_objects(trainers):
    obj_course = []
    for id in id_courses:
        c = Course(id, dict_course[id][0], dict_course[id][1], dict_course[id][2], dict_course[id][3], dict_course[id][4])
        if id == 'cou1': trainers[0].add_course(c)
        if id == 'cou2': trainers[0].add_course(c)
        if id == 'cou3': trainers[0].add_course(c)
        if id == 'cou4': trainers[1].add_course(c)
        if id == 'cou5': trainers[1].add_course(c)
        obj_course.append(c)
    return obj_course


def print_objects(list):
    for item in list:
        print(item)

def make_enrollment(employee, course):
    en = Enrollment(employee, course)
    employee.enrolled.append(course)
    return en



def main():

    addresses = create_address_objects()
    associate_address_with_person(addresses)

    employees = create_employee_objects()

    trainers = create_trainer_objects()
    associate_trainer_with_course(trainers)

    courses = create_course_objects(trainers)

    make_enrollment(employees[0],courses[1])

    print(employees[0].enrolled[0])
    print(trainers[0].courses[0])





if __name__ == "__main__":
    main()
