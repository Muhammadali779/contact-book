class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def update(self, phone=None, email=None):
        if phone:
            self.phone = phone
        if email:
            self.email = email

    def display(self):
        return f"{self.name} | {self.phone} | {self.email}"
