from app.contact import Contact
from app.storage import Storage

class ContactBook:
    def __init__(self):
        self.contacts = []
        self.storage = Storage()
        self.load_contacts()

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self.save_contacts()

    def show_all(self):
        for c in self.contacts:
            print(c.display())

    def search_contact(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                print(c.display())
                return
        print("Contact not found")

    def delete_contact(self, name):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                self.contacts.remove(c)
                self.save_contacts()
                return
        print("Contact not found")

    def update_contact(self, name, phone=None, email=None):
        for c in self.contacts:
            if c.name.lower() == name.lower():
                c.update(phone, email)
                self.save_contacts()
                return
        print("Contact not found")

    def save_contacts(self):
        data = [{"name": c.name, "phone": c.phone, "email": c.email} for c in self.contacts]
        self.storage.save(data)

    def load_contacts(self):
        data = self.storage.load()
        self.contacts = [Contact(d["name"], d["phone"], d["email"]) for d in data]
