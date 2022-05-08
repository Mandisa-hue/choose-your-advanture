name = input("Type your name " )
print("Welcome" , name, "to ths adventure!")

answer = input(" You are on a dirt road, it has come to an end and you can go left or right. Whch way would you like to go ? " ).lower()

if answer == "left":
    answer = input(" You came to a river, you can walk around it or swim across ? ")

    if answer == "swim":
        print("You swam across and were eaten by a crocodile.")

    elif answer == "walk":
        print("You walked for many miles and ran out of water and you lost the game. ")

    else:
        print("Not a valid option. You lose.")
        
elif answer == "right":
    answer = input("You came to a bridge, it looks wobbly, do you what to cross it or head back ? (cross/back) ")

    if answer == "back":
        print("You go back and are ran over by a truck and lose")

    elif answer == "cross":
        anwser = input("You cross the brdge and meet a strangr. Do you talk to them (yes/no)? ")
    
        if answer == "yes":
            print("You spoke to the stranger and they give you gold. You WIN! ")
        elif answer == "no":
            print("You ignored the stranger and they are offended. You LOSE! ")
        else:
            print("Not a valid option. You lose.")
    else:
            print("Not a valid option. You lose.")
            
else:
    print("Not a valid option. You lose.")
    
            
print("Thank you for trying", name) 
 
