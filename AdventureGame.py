print("Hello Adventurer")
print("Welcome to the unbeatable challenge")


def game(): #create a function
    start=input("Care to start? Yes or No\n").lower().strip() #lower() coverts answer to lowercase and strip gets ride of white space
    if start== "yes":
        print("Lets Start")
        print("You found a black cat in your path do you")
        print("pet the cat or leave it be?")
        print("pet or leave")
        cat=input().lower().strip()
        if cat== "pet" or cat == "leave":   #make sure input is valid, if not its game over
            if cat== "pet":
                print("the cat started attacking you and you died")
            else:
                print("You ignored the cat. Good choice, it didnt seem nice")
                print("But you still lose because this is my game muahahah")
                pring("Game Over")
         
        else:
            print("Game Over")

    else:
        print("Game Over")
        
    
game()#call the function
