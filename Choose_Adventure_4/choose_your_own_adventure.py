name = input("Enter your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on dirt road, it has come to an end and you can go left or right. Which way you would like to go? ").lower()

if answer == 'left':
    answer = input("You come to a river, you can walk around it or swim accross? Type 'walk' to walk around the river or type 'swim' to swim across the river: ")
    
    if answer == 'swim':
        print("You swam across and were eaten by an aligator")
    elif answer == 'walk':
        print('You walked for many miles, ran out of water and you lost the game')
    else:
        print("Not a valid option. You loose.")
elif answer == 'right':
    answer = input("You come to bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")
    
    if answer == 'back':
        print("You go back and loose.")
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        
        if answer == 'yes':
            print("You talk to the stranger, they gave you gold. You WIN!")
        elif answer == 'no':
            print('You ignored the stranger and they offended and you loose.')
        else:
            print("Not a valid option. You loose.")
    else:
        print("Not a valid option. You loose.")
            
else:
    print("Not a valid option. You loose.")
    
print("Thank you for trying",name)
