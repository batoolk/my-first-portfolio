start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You decide to go left.") # finished the story by writing what happens
    print("You fell from the top of the mountain.")
    print("You woke up from your sleep and this was just a nightmare.")

elif user_input == "right":
    print("You choose to go right and see your mom") # finished the story writing what happens
    print("your mom asks, 'how are you?'")
    response = input("what do you say?")

    if "good" in response:
        drinkCoffee = input("your mom smiles and ask,'shall we drink coffee, then?'")

        if "yes" in drinkCoffee:
            print("your mom pours a cup of coffee each. you drink the coffee together.")
            go = input ("your mom is going to the store and asks if want to the store too. type 'we are ready' if you  want to go.")
            if " we are" in  go:
                "you both go the store.the end."
        else:
            print("your mom drink coffee alone. the end.")

    else:
        print("your mom frowns. the end.")
