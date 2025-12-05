def title():
    print()
    print("Enter 1. to add a new contact.")
    print("Enter 2. to show the number of a person.")
    print("Enter 3. to show the person of a number.")
    print("Enter 4. to show the contact list.")
    print("Enter 5. to exit.")
    print()

# ---------- Load Contacts from File ---------
def load_contacts():
    phone = {}
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, number = line.strip().split(":")
                phone[name] = int(number)
    except FileNotFoundError:
        # if file doesn't exist, start with an empty dictionary
        pass
    return phone

# ---------- Save Contacts to File ----------
def save_contacts(phone):
    with open("contacts.txt", "w") as file:
        for name, number in phone.items():
            file.write(f"{name}:{number}\n")

# ---------- Main Program ----------
phone = load_contacts()  # load existing contacts

while True:
    title()
    choice = input("Enter your choice: ")
    print()

    if choice == "1":
        person = input("Enter the person's name: ")
        num = input("Enter the phone number: ")

        if person in phone:
            print(" This contact already exists.")
        else:
            phone[person] = num
            save_contacts(phone)   # save after adding
            print(f" Contact '{person}' added and saved!")

    elif choice == "2":
        person = input("Enter the person's name: ")
        print(phone.get(person, " Contact not found."))

    elif choice == "3":
        num = input("Enter the phone number: ")
        found = False
        for name, n in phone.items():
            if str(n) == num:
                print(" Name:", name)
                found = True
                break
        if not found:
            print(" Number not found.")

    elif choice == "4":
        print("_________________")
        print("|   CONTACTS    |")
        print("-----------------")
        if len(phone) == 0:
            print("No contacts saved yet.")
        else:
            for key, value in phone.items():
                print(f"{key} --> {value}")

    elif choice == "5":
        print(" Exiting and saving contacts...")
        save_contacts(phone)
        break

    else:
        print(" Please enter a valid choice (1–5).")
