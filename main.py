from app.contact_book import ContactBook

book = ContactBook()

while True:
    print("\n1. Add Contact")
    print("2. Show All")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Select: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        book.add_contact(name, phone, email)

    elif choice == "2":
        book.show_all()

    elif choice == "3":
        name = input("Enter name: ")
        book.search_contact(name)

    elif choice == "4":
        name = input("Qaysi kontaktni yangilaysiz: ")
        phone = input("Yangi Nom: ")
        email = input("Yangi email : ")
        book.update_contact(name, phone or None, email or None)
    elif choice == "5":
        name = input("Enter name: ")
        book.delete_contact(name)
    elif choice == "6":
        break
    else:
        print("Invalid choice")
