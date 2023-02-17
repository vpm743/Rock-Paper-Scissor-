"""
Rock Paper Scissor

Ved Prakash Mishra
Class XI CS
"""

import random 
import time

print("*****************************************************************************")
print("\t-------------------")
print("\tROCK,PAPER,SCISSOR")
print("\t-------------------")
print("*****************************************************************************")
dict1={1:"rock",2:"paper",3:"scissor"}
print("***************")
print("instruction\n\nrock>scissor\nrock<paper\nscissor>paper")           #Instructions
print("***************")
print('Press x to Exit')
user_player=0
computer_player=0
v=1
play_round=1
while v==1:                                     #Infinite Loop
    print('\tRound',play_round)
    rps_input=input('Enter Rock or Paper or Scissor:-').lower()
    ran=random.randint(1,3)                     #Random Between 1 to 3
    print('rock!',end=' ')
    time.sleep(0.5)                             #Delay 0.5 seconds
    print('paper!',end=' ')
    time.sleep(0.5)                             #Delay 0.5 seconds
    print('scissor!',end=' ')
    time.sleep(0.5)                             #Delay 0.5 seconds
    print('shoot!')


    if dict1[ran]==rps_input:
        print('Computer Choose -',dict1[ran])
        print('Tie')   


    elif dict1[ran]=='rock' and rps_input=='scissor':
        print('Computer Choose -',dict1[ran])
        print('Computer_Player Win')
        computer_player+=1


    elif dict1[ran]=='rock' and rps_input=='paper':
        print('Computer Choose -',dict1[ran])
        print('user_player Win')
        user_player+=1
  

    elif dict1[ran]=='paper' and rps_input=='scissor':
        print('Computer Choose -',dict1[ran])
        print('user_player Win')
        user_player+=1


    elif dict1[ran]=='paper' and rps_input=='rock':
        print('Computer Choose -',dict1[ran])
        print('Computer_Player Win')
        computer_player+=1
        

    elif dict1[ran]=='scissor' and rps_input=='rock':
        print('Computer Choose -',dict1[ran])
        print('Player  Win')
        user_player+=1
       
    elif dict1[ran]=='scissor' and rps_input=='paper':
        print('Computer Choose -',dict1[ran])
        print('Computer_Player  Win')
        computer_player+=1
 

    else:
        print('invalid input')
        print()
    print('Player',user_player,'Computer_Player',computer_player)
    

    play_round+=1                           # Round Increase
    print("\n\n\n")
    
