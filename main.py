from auth import register_user, login_user


def main():
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            email = input("Enter email: ")
            print(register_user(username, password, email))

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            print(login_user(username, password))

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main()
