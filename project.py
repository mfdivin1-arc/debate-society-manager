import csv

MEMBERS_FILE = "members.csv"

def main():
    members = load_members()
    print(f"Welcome! {len(members)} member(s) loaded.")

    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_members(members)
            save_members(members)

        elif choice == "2":
            view_members(members)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Please enter 1, 2, or 3.")


def print_menu():  
    print("Debate Society Manager\n")
    print("1. Add a member")
    print("2. View members")
    print("3. Exit\n")


def load_members():
    members = []
    try:
        with open(MEMBERS_FILE, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                members.append(row[0])
    except FileNotFoundError:
        pass
    return members


def add_members(members):
    print("Let's add a member. Press 'Enter' when you are done!")
    while True:
        member = input("Name: ").strip()
        if not member:
            break
        members.append(member)
        print(f"Added {member}")


def save_members(members):
    with open(MEMBERS_FILE, "w", newline="") as file:
        writer = csv.writer(file)
        for name in members:
            writer.writerow([name])


def view_members(members):
    if members:
        print("Here's the list of members.")
        for n, person in enumerate(members, start=1):         
            print(f"{n}. {person}")

    else:
        print("Come back later!!")


if __name__ == "__main__":
    main()

