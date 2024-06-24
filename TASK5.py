contacts = []

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    address = input("Enter contact address: ")
    
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for contact in contacts:
            print("Name:", contact['name'], "Phone:", contact['phone'])

def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print("Name:", contact['name'], "Phone:", contact['phone'], "Email:", contact['email'], "Address:", contact['address'])
            found = True
    if not found:
        print("No contacts found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Enter new details (leave blank to keep current value):")
            new_name = input("Name [{contact['name']}]: ") or contact['name']
            new_phone = input("Phone [{contact['phone']}]: ") or contact['phone']
            new_email = input("Email [{contact['email']}]: ") or contact['email']
            new_address = input("Address [{contact['address']}]: ") or contact['address']
            
            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    global contacts
    new_contacts = [contact for contact in contacts if contact['name'].lower() != name.lower()]
    if len(new_contacts) < len(contacts):
        contacts = new_contacts
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
