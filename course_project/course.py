from trainer import Trainer
# from enrollment import Enrollment

class Course:

    def __init__(self, id, name, code, _max, _min, trainer):
        self.id = id
        self.name = name
        self.code = code
        self.max = _max
        self.min = _min
        self.trainers = []
        self.enrollments = []

        if isinstance(trainer, Trainer):
            self.trainers.append(trainer)
        elif isinstance(trainer, list):
            for entry in trainer:
                if not isinstance(trainer, Trainer):
                    raise Error('Invalid trainer!')
            self.trainers = trainer
        else:
            raise Error('Invalid trainer!')

    def __repr__(self):
        return f'Course {self.id}: {self.name} - {self.code}'

    def add_trainer(self, trainer):
        if not isinstance(trainer, Trainer):
            raise Error('Invalid trainer!')
        else:
            self.trainers.append(trainer)

    def add_enrollment(self, enrollment):
        if not isinstance(enrollment, Enrollment):
            raise Error('Invalid Enrollment!')
        if len(enrollments) == slef.max:
            raise Error('Course is full!')
        self.enrollments.append(enrollment)

    def is_cancelled(self):
        return len(self.enrollments) < self.min
