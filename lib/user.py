class User:
    def __init__(self, name):
        self.name = name

    def log_in(self):
        self.logged_in = True

    def __str__(self):
        return f"User name: (name={self.name})"

