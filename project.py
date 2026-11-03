import csv

MEMBERS_FILE = "members.csv"
YEARS = ["Freshman", "Sophomore", "Junior", "Senior"]
LEVELS = ["New", "Intermediate", "Experienced"]

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
            remove_member(members)
            save_members(members)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Please enter a number from 1 to 4.")


def load_members():
    members = []
    try:
        with open(MEMBERS_FILE, newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                members.append(row)
    except FileNotFoundError:
        pass
    return members

def print_menu():
    print("\nDebate Society Manager")
    print("1. Add a member")
    print("2. View members")
    print("3. Remove a member")
    print("4. Exit\n")

def add_members(members):
    print("Let's add a member. Press 'Enter' when you are done!")
    while True:
        name = input("Name: ").strip()
        if not name:
            break
        if name_exists(members, name):
            print(f"{name} is already a member.")
            continue
        year = choose_option("Year", YEARS)
        level = choose_option("Debate experience", LEVELS)
        members.append({"name": name, "year": year, "level": level})
        print(f"Added {name}.")

def name_exists(members, name):
    for member in members:
        if member["name"].lower() == name.lower():
            return True
    return False

def choose_option(label, options):
    print(f"{label}:")
    for number, option in enumerate(options, start=1):
        print(f"  {number}. {option}")
    while True:
        index = parse_choice(input("Enter a number: ").strip(), len(options))
        if index is not None:
            return options[index]
        print(f"Please enter a number from 1 to {len(options)}.")

def parse_choice(text, count):
    try:
        number = int(text)
    except ValueError:
        return None
    if 1 <= number <= count:
        return number - 1
    return None

def save_members(members):
    with open(MEMBERS_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "year", "level"])
        writer.writeheader()
        for member in members:
            writer.writerow(member)

def view_members(members):
    if not members:
        print("No members yet, come back later!!")
        return    
    print("Here's the list of members.")
    for number, member in enumerate(members, start=1):
        print(f"{number}. {member['name']} ({member['year']}, {member['level']})")       

def remove_member(members):
    if not members:
        print("No members to remove.")
        return
    view_members(members)
    text = input("Number of the member to remove (press Enter to cancel): ").strip()
    if text == "":
        return
    index = parse_choice(text, len(members))
    if index is None:
        print("That isn't a valid number.")
        return
    removed = members.pop(index)
    print(f"Removed {removed['name']}.")

    
if __name__ == "__main__":
    main()

