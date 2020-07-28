from person import Person
from course import Course

class Trainer(Person):
    def __init__(self, id, firstName, lastName, phoneNumber, dateOfBirth, address, domain, salary):
        super().__init__(firstName, lastName, phoneNumber, dateOfBirth, address)
        self.id = id
        self.domain = domain
        self.salary = salary
        self.courses = []
        self.got_raise = False

    def __repr__(self):
        return f'Trainer: {self.firstName} {self.lastName} - {self.domain} - {self.salary}'

    def check_for_raise(self):
        if len(self.courses) >=4 and not self.got_raise:
            self.salary += 10000
            self.got_raise = True

    def add_course(self, course):
        if not isinstance(course, Course):
            raise Error('Invalid Course')
        else:
            self.courses.append(course)
