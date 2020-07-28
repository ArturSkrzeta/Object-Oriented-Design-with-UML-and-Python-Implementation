from employee import Employee
from course import Course
from datetime import datetime

class Enrollment():
        def __init__(self, employee, course):
            if not isinstance(employee, Employee):
                raise Error('Invalid employee!')

            if not isinstance(course, Course):
                raise Error('Invalid course!')

            self.employee = employee
            self.course = course
            self.grade = None
            self.date = datetime.now()

        def set_grade(self, grade):
            self.grade = grade
