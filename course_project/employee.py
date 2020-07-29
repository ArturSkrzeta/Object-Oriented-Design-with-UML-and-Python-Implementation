from person import Person
from datetime import datetime

class Employee(Person):

    def __init__(self, id, firstName, lastName, phoneNumber, dateOfBirth, title, international, dateOfEmployment):
        super().__init__(firstName, lastName, phoneNumber, dateOfBirth)
        self.id = id
        self.title = title
        self.international = False
        self.dateOfEmployment = dateOfEmployment
        self.enrolled = []

    def __repr__(self):
        return f'Employee: {self.firstName} {self.lastName} - {self.title} - {self.addresses}'

    def add_enrollment(self,enroll):
        from enrollment import Enrollment
        if not isinstance(enroll, Enrollment):
            raise Error("Invalid Enrollment")
        self.enrolled.append(enroll)

    # def convert_enrolled_into_string(self):
    #     if len(self.enrolled) != 0:
    #         str_enrolled= ''
    #         for enroll in self.enrolled:
    #             str_ = enroll.country + ' ' + enroll.city + ' ' + enroll.street + ' ' + enroll.postal + '; '
    #             str_enrolled += str_
    #
    #         return str_enrolled

    def is_on_probation(self):
        return False

    def is_part_time(self):
        return len(self.enrolled) <= 3
