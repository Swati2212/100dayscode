print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure.")
cross_road = input("You are at the crossroad? Where do you want to go? Type 'left' or 'right' \n").lower()

if cross_road == "left":
    lake = input("You came to the lake.There is a island in the middle of the lake. Type 'Wait' for the boat. Type 'Swim' to swim across.\n")
    if lake == 'wait':
        door = input("You arrived at the island unharm.There is a house with 3 doors. One red, one yellow, and one blue.Which color do you choose.\n")
        if door == 'red':
            print("Burned by fire.Game over!")
        elif door == 'blue':
            print("Eaten by beast. Game Over!")
        else:
            print("You win!")
    else:
        print("Attacked by trout. Game over!")
else:
    print("You fell into the hole.Game over!")
