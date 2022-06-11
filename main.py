print("\nThe game of rock , paper and scissors")
print("\nR : Rock, P : Paper, S : Scissors")
print("\nPick an option between 'R' ,'P' and 'S' " )
print("\nPLEASE FOLLOW RULES!!!")
import random
dict_1 = {'R':"Rock",'P':"Paper",'S':"Scissors"}
option = ['R','P','S']

is_Starting_again = True
while True:
    cpu = random . choice(option)
    choices = input("\nYour choice : ")
    choices = choices.upper()
    if choices not in option:
        print("\nInvalid!!! Try again")
        continue
    print("Player({}):CPU({})".format(dict_1[choices],dict_1[cpu]))
    if choices == cpu:
        print ("\n Oops, we picked the same option.")
    
    elif cpu == 'R' and choices == 'S' or cpu == 'P' and choices == 'R' or cpu == 'S' and choices == 'P':
        print("\n Sorry, you failed!!!")
        break
    else :
        print("\nHurray you won!!!")
        break