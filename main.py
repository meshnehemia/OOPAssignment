from pet import pet
while True:
    print("Welcome to the pet simulator!")
    name = input("Enter your pet's name: ")
    my_pet = pet(name)
    print(f"Your pet {my_pet.name} has been created!")
    while True:
        print("What would you like to do?")
        print("1. Eat")
        print("2. Sleep")
        print("3. Play")
        print("4. Train")
        print("5. Show Tricks")
        print("6. Play Trick")
        print("7. Get Status")
        print("8. Exit")
        choice = input()
        if choice == "1":
            my_pet.eat()
            my_pet.get_status()
        elif choice == "2":
            my_pet.sleep()
            my_pet.get_status()
        elif choice == "3":
            my_pet.play()
            my_pet.get_status()
        elif choice == "4":
            trick = input("Enter the trick you want to train: ")
            my_pet.train(trick)
            my_pet.get_status()
        elif choice == "5":
            my_pet.show_tricks()
            my_pet.get_status()
        elif choice == "6":
            my_pet.play_trick()
            my_pet.get_status()
        elif choice == "7":
            my_pet.get_status()
            my_pet.get_status()
        elif choice == "8":
            my_pet.get_status()
            break
        else:
            print("Invalid choice. Please try again.")