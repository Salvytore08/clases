users = []

def add_user(name, age, email):
    user = {"name": name, "age": age, "email": email}
    users.append(user)
    print(f"User {name} added successfully.")

def delete_user(email):
    for user in users:
        if user["email"] == email:
            users.remove(user)
            print(f"User {user['name']} deleted successfully.")
            return
    print("User not found.")

def view_users():
    for user in users:
        print(f"Name: {user['name']}, Age: {user['age']}, Email: {user['email']}")

def update_user(email):
    for user in users:
        if user["email"] == email:
            new_name = input("Enter new name: ")
            new_age = input("Enter new age: ")
            new_email = input("Enter new email: ")
            user["name"] = new_name
            user["age"] = new_age
            user["email"] = new_email
            print(f"User {new_name} updated successfully.")
            return
    print("User not found.")

while True:
    print("\nWhat would you like to do?")
    print("1. Add user")
    print("2. Delete user")
    print("3. View users")
    print("4. Update user")
    print("5. Quit")
    choice = input("Enter choice (1-5): ")

    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        email = input("Enter email: ")
        add_user(name, age, email)
    elif choice == "2":
        email = input("Enter email: ")
        delete_user(email)
    elif choice == "3":
        view_users()
    elif choice == "4":
        email = input("Enter email: ")
        update_user(email)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")