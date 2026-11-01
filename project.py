members = []

while True:    
    print("Debate Society Manager\n")
    print("1. Add a member")
    print("2. View members")
    print("3. Exit\n")
    choice = input("Choose an option: ")
    if choice == "1":
        print("Let's add a member. Press 'Enter' when you are done!")
        while True:
            member = input("Name: ")
            if not member:
                members.append(member)
                break

        print("Thank you for your cooperation!")

    elif choice == "2":  
        if members:
            print("Here's the list of members.")
            for n, person in enumerate(members, start=1):         
                print(f"{n}. {person}")

        else:
            print("Come back later!!")       

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")        

