from person import Person

class Employee(Person):

    def __init__(self, id, firstName, lastName, phoneNumber, dateOfBirth, address, title, international, dateOfEmployment):
        super().__init__(firstName, lastName, phoneNumber, dateOfBirth, address)
        self.id = id
        self.title = title
        self.international = False
        self.dateOfEmployment = dateOfEmployment
        self.enrolled = []

    def __repr__(self):
        return f'Employee: {self.firstName} {self.lastName} - {self.title} - {self.addresses}'

    def add_enrollment(self,enrollment):
        if not isinstance(self, enrollment):
            raise Error("Invalid Enrollment")
        self.enrolled.append(enrollment)

    def is_on_probation(self):
        return False

    def is_part_time(self):
        return len(self.enrolled) <= 3
