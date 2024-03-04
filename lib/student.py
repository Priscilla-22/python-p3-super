from user import User


class Student(User):
    def __init__(self, name, grade):
        super().__init__(name)
        self.grade = grade

    def log_in(self):
        super().log_in()
        self.in_class = True

    def __str__(self):
        return f"Student (name={self.name}, grade={self.grade})"
