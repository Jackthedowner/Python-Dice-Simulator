import random
dice_value=random.randint(1,6)



def board1():
    print('[]','[]','[]')
    print('[]',' @','[]')
    print('[]','[]','[]')
def board2():
    print(' @','[]','[]')
    print('[]','[]','[]')
    print('[]','[]',' @')
def board3():
    print('@','[]','[]')
    print('[]','@','[]')
    print('[]','[]','@')
def board4():
    print(' @','[]',' @')
    print('[]','[]','[]')
    print(' @','[]',' @')
def board5():
    print('@','[]','@')
    print('[]','@','[]')
    print('@','[]','@')
def board6():
    print('@','[]','@')
    print('@','[]','@')
    print('@','[]','@')

def dice():
    if dice_value==1:
       board1()
    elif dice_value==2:
         board2()
    elif dice_value==3:
         board3()
    elif dice_value==4:
         board4()
    elif dice_value==5:
         board5()
    elif dice_value==6:
     board6()

i=input('Press ENTER to ROLL dice:')
if i!='.':
    dice()

print('ROLLED DICE VALUE IS:',dice_value)