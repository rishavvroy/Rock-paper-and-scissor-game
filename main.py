import random
def game_win(comp, player):
    if player!='rock' and player!='scissor' and player!='paper':
        return a
    elif comp==player:
        return None
    elif comp=='scissor':
        if player=='rock':
            return True
        elif player=='paper':
            return False
    elif comp=='rock':
        if player=='paper':
            return True
        elif player=='scissor':
            return False
    elif comp=='paper':
        if player=='rock':
            return False
        elif player=='scissor':
            return True

randNo=random.randint(1,3)
if randNo==1:
    comp='scissor'
if randNo==2:
    comp='rock'
if randNo==3:
    comp='paper'
print("choose:'rock', 'paper'or, 'scissor' to start the game")
player=input("Player choise:")
print(f"computer choose:{comp}")
print(f"you choose:{player}")
a='plear try again'
b=game_win(comp, player)
if b==None:
    print("Tie")
elif b==True:
    print("player wins")
elif b==False:
    print("computer wins")
elif b==a:
    print("please choose from 'rock', 'paper' or, 'scissor'")