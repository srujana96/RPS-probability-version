# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 12:55:54 2020
project - ai prediction - rock paper scissor game
@author: Srujana Chilukuri
"""

import numpy as np
import csv

score_p1=0
score_p2=0
count_p2 = 0
result = ""

prob_1=0
prob_2=0
prob_3=0
repeat_prob=0
random = "false"
data = dict ({})
objects = dict ({1:"Rock", 2:"Paper", 3:"Scissors"})
list_key = list(objects.keys())
list_value = list(objects.values())

with open("data.txt", 'r+',newline='') as file:
    file.seek(0)
    file.truncate()

while(1):
    prob_1=0
    prob_2=0
    prob_3=0
    print("Enter your move - 1 for stone, 2 for paper, 3 for scissors:")
    try:
        player2_move = int(input())
    except:
        print("Enter valid value:")
        player2_move = int(input()) 
    
    if(player2_move > 3 or player2_move < 1):
        print("Enter valid value(1 or 2 or 3).Program stopped.")
        """player2_move = int(input())"""
        quit()
        
    count = 1
    with open("data.txt", newline='') as file:
        rows = csv.reader(file, delimiter=",")
        for row in rows:
            data[count] = row[0:]
            count = count + 1
            if(data[count-1][1]=='Rock'):
                prob_1 = prob_1+ 1
            elif(data[count-1][1]=='Paper'):
                prob_2 = prob_2+ 1
            elif(data[count-1][1]=='Scissors'):
                prob_3 = prob_3+ 1
            
    if(count == 1):
        player1_move = np.random.randint(1,4)
        
    elif(count == 2):
        if(data[count-1][2] == "win"):
            if(data[count-1][0] == "Rock"):
                    player1_move = 3
            elif(data[count-1][0] == "Paper"):
                    player1_move = 1
            elif(data[count-1][0] == "Scissors"):
                    player1_move = 2
        
        elif(data[count-1][2] == "lose"):
                if(data[count-1][1] == "Rock"):
                    player1_move = 2
                elif(data[count-1][1] == "Paper"):
                    player1_move = 3
                elif(data[count-1][1] == "Scissors"):
                    player1_move = 1
        elif(data[count-1][2] == "tie"):
            if(data[count-1][1] == "Rock"):
                    player1_move = 2
            elif(data[count-1][1] == "Paper"):
                    player1_move = 3
            elif(data[count-1][1] == "Scissors"):
                    player1_move = 1
    else:
        """mode: repeats previous move"""
        player1_move_1 = 0
        if(data[count-1][1] == data[count-2][1]):
            repeat_prob = repeat_prob+1
            if(data[count-1][1] == "Rock"):
                player1_move = 2
            elif(data[count-1][1] == "Paper"):
                player1_move = 3
            elif(data[count-1][1] == "Scissors"):
                player1_move = 1
            print("1st player1move :",player1_move)
                
        else:
            """mode: beats opponents previous move,
            mode: plays opponents previous move,
            mode: beats its previous move, 
            mode: plays its previous move"""
            prev_opp_move = list_key[list_value.index(data[count-2][0])]
            prev_move = list_key[list_value.index(data[count-2][1])]
            player_move = list_key[list_value.index(data[count-1][1])]
            if(player_move == ((prev_opp_move%3)+1)):
                print("con:1")
                if(data[count-1][2] == "win"):
                    if(data[count-1][0] == "Rock"):
                        player1_move = 3
                    elif(data[count-1][0] == "Paper"):
                        player1_move = 1
                    elif(data[count-1][0] == "Scissors"):
                        player1_move = 2
                    print("2nd player1move :",player1_move)
                if(data[count-1][2] == "lose"):
                    if(data[count-1][0] == "Rock"):
                        player1_move = 3
                    elif(data[count-1][0] == "Paper"):
                        player1_move = 1
                    elif(data[count-1][0] == "Scissors"):
                        player1_move = 2
                if(data[count-1][2] == "tie"):
                    if(data[count-1][0] == "Rock"):
                        player1_move = 3
                    elif(data[count-1][0] == "Paper"):
                        player1_move = 1
                    elif(data[count-1][0] == "Scissors"):
                        player1_move = 2        
                
            elif(player_move == prev_opp_move ):
                print("con:2")
                if((data[count-1][2] == "win") or (data[count-1][2] == "lose")):
                    if(data[count-1][0] == "Rock"):
                        player1_move = 2
                    elif(data[count-1][0] == "Paper"):
                        player1_move = 3
                    elif(data[count-1][0] == "Scissors"):
                        player1_move = 1
                if(data[count-1][2] == "tie"):
                    if(data[count-1][0] == "Rock"):
                        player1_move = 2
                    elif(data[count-1][0] == "Paper"):
                        player1_move = 3
                    elif(data[count-1][0] == "Scissors"):
                        player1_move = 1
                        
            elif(player_move == ((prev_move%3)+1)):
                print("con:3")
                if(data[count-1][2] == "lose"):
                    if(data[count-1][1] == "Rock"):
                        player1_move = 3
                    elif(data[count-1][1] == "Paper"):
                        player1_move = 1
                    elif(data[count-1][1] == "Scissors"):
                        player1_move = 2
                if(data[count-1][2] == "win"):
                    if(data[count-1][1] == "Rock"):
                        player1_move = 3
                    elif(data[count-1][1] == "Paper"):
                        player1_move = 1
                    elif(data[count-1][1] == "Scissors"):
                        player1_move = 2
                if(data[count-1][2] == "tie"):
                    if(data[count-1][1] == "Rock"):
                        player1_move = 3
                    elif(data[count-1][1] == "Paper"):
                        player1_move = 1
                    elif(data[count-1][1] == "Scissors"):
                        player1_move = 2
                    print("2nd player1move :",player1_move)
            
            elif((player_move == (((prev_move%3)+1)%3)+1 ) or (player_move == (((prev_opp_move %3)+1)%3)+1)):
                print("con:4")
                random = "true"
                #if((data[count-1][2] == "lose") or (data[count-1][2] == "tie")):
                if(data[count-1][1] == "Rock"):
                    player1_move = 3
                elif(data[count-1][1] == "Paper"):
                    player1_move = 1
                elif(data[count-1][1] == "Scissors"):
                    player1_move = 2
                    
                #player1_move = np.random.randint(1,4)
                
            print("2nd player1move :",player1_move)
            
            """maxim = max(prob_1,prob_2,prob_3)
            if(player1_move != player1_move_1):
                print(repeat_prob,maxim)
                if(repeat_prob >= maxim):
                    player1_move = player1_move_1"""
            if((player1_move == 1 and prob_1 == 0) or (player1_move == 2 and prob_2 == 0) or (player1_move == 3 and prob_3 == 0)):
                    player1_move = (player1_move%3)+1
        
            if(random=="true"):
                player1_move = np.random.randint(1,4)
                
    if(player1_move == player2_move):
        print(objects[player1_move], ",",objects[player2_move], "- It's a Tie")
        result = "tie"
    elif(player1_move < player2_move):
        if( player1_move+player2_move == 4 ):
            score_p1 += 1
            result = "win"
            print(objects[player1_move], ",",objects[player2_move], "- I win!")
        else:
            score_p2 += 1
            result = "lose"
            print(objects[player1_move], ",",objects[player2_move], "- You win!")
    elif(player1_move > player2_move):
        if( player1_move+player2_move == 4 ):
            score_p2 += 1
            result = "lose"
            print(objects[player1_move], ",",objects[player2_move], "- You win!")
        else:
            score_p1 += 1
            result = "win"
            print(objects[player1_move], ",",objects[player2_move], "- I win!")
        
    with open("data.txt", 'a+',newline = '') as file:
        out = csv.writer(file)
        row1 = [objects[player1_move],objects[player2_move],result]
        out.writerow(row1)
    
    print ("Scores: Player-",score_p2 ,", Computer-", score_p1)
    
    
