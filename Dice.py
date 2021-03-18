# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 01:53:12 2021

@author:Manish Kumar Goswami

"""
import random

count = 0


while 1 :
    num = random.randint(1, 6)
    
    if num == 1:
        print("____________")
        print("|          |")
        print("|          |")
        print("|    O     |")
        print("|          |")
        print("|          |")
        print("````````````")
        break
        
        
        
    elif num == 2:
        print("____________")
        print("|O         |")
        print("|          |")
        print("|          |")
        print("|          |")
        print("|         O|")
        print("````````````")
        break

    
        
    elif num == 3:
        print("____________")
        print("|O         |")
        print("|          |")
        print("|    O     |")
        print("|          |")
        print("|         O|")
        print("````````````")
        break
        
    
    elif num == 4:
        print("____________")
        print("|O        O|")
        print("|          |")
        print("|          |")
        print("|          |")
        print("|O        O|")
        print("````````````")
        break
    
    
    elif num == 5:
        print("____________")
        print("|O        O|")
        print("|          |")
        print("|    O     |")
        print("|          |")
        print("|O        O|")
        print("````````````")
        break
        
    elif num == 6:
        
        count = count + 1
        
        if(count < 3):
            print("____________")
            print("|O        O|")
            print("|          |")
            print("|O        O|")
            print("|          |")
            print("|O        O|")
            print("````````````")
        else:
            print("You Got Continously 3 six ")
            break
    
        
    


















