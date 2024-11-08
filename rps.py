rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
l=[rock,paper,scissors,'play again']
game=True
while game==True:
    choice=int(input('enter a number in 0,1,2,3:'))
    print(l[choice])
    compchoice=random.randint(0,2)
    if choice in [0,1,2]:
        print(l[compchoice])
    else:
        pass
    print('result')
    if compchoice==0  and choice==1:
        print('you won')
    elif compchoice==0 and choice==2:
        print('you lose')
    elif compchoice==1 and choice==2:
        print("you won")
    elif compchoice==2 and choice==1:
        print('you lose')
    elif compchoice==2 and choice==0:
        print('you won')
    elif compchoice==1 and choice==0:
        print('you lose')
    elif choice==3 :
        game=False
    else:
        print('draw')





