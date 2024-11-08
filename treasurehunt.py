print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice=input("choose left or right")
if choice=='left':
    choice2=input("choose wait or swim")
    if choice2=='wait':
        choice3=input("red door or blue door or yellow door")
        if choice3=='red':
            print("game over")
        elif choice3=='blue':
            print("gameover")
        elif choice3=='yellow':
            print('you win')
        else:
            print('game over')
    else:
        print('game over')
else:
    print("game over")

