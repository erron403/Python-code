#!/usr/bin/env python3
# Created By: RaVierma
#
#
# The order of starting and ending position values.
#
#          |    |
#	1  |  2 |  3  
#     -----|----|-----
#          |    |
#	4  |  5 |  6  
#     -----|----|-----
#          |    |  
#	7  |  8 |  9
#

import random

barr = [ x *3 for x in [[' '],[' '],[' ']]]
arr_track = [[1,2,3],[4,5,6],[7,8,9]]
usr_position_track = []
win_count = {"player_A":0 , "player_B": 0}
wins_type_count = {"hr_win": [], "vrt_win": [], "right_dig":0, "left_dig":0}

        
def board_play():
    """
    Create tic-tac-toc board
    """
    print(f"""\n\t{' '*2} |    |\n\t{barr[0][0]}{' '*2}|  {barr[0][1]} |{' '*2}{barr[0][2]}\n{' '*6}{'-'*5}|{'-'*4}|{'-'*5}
        {' '*2} |    |\n\t{barr[1][0]}{' '*2}|  {barr[1][1]} |{' '*2}{barr[1][2]}\n{' '*6}{'-'*5}|{'-'*4}|{'-'*5}
        {' '*2} |    |\n\t{barr[2][0]}{' '*2}|  {barr[2][1]} |{' '*2}{barr[2][2]}\n{' '*6}
        """)

def place_userinput(player,position):
    position = int(position)
    if position <= 3 and not position <= 0 and position not in usr_position_track:
        barr[0][arr_track[0].index(position)] = player
        usr_position_track.append(position)
        
    elif position <= 6 and not position <= 3 and position not in usr_position_track:
        barr[1][arr_track[1].index(position)] = player
        usr_position_track.append(position)
        
    elif position <= 9 and not position <= 6 and position not in usr_position_track:
        barr[2][arr_track[2].index(position)] = player
        usr_position_track.append(position)
        
    else:
        print("\n\t[ +++++ Must be within 1 to 9 +++++ ]\n")

    
def hr_win():
    hr_and_vrt_win_helper(barr, "hr_win")

def vrt_win():
    # intialize the column by 0
    col = 0
    # create list to add columns as list.
    col_to_row = []
    while col < len(barr):
        col_data = []
        for r in barr:
            # add each row first element in col_data
            col_data.append(r[col])
        # after add each row first element then add col_data list in col_to_row list.
        col_to_row.append(col_data)
        # increment the column and repeate same process.
        col += 1
    # after covert column to row then perform vertical check
    hr_and_vrt_win_helper(col_to_row,"vrt_win")
    
                         
def hr_and_vrt_win_helper(arr,win_type):
    """"
    It Take two argument:
    arr: list on which win type perform
    win_typ: it can be hr_win or vrt_win
    """
    for r in arr:
        if arr.index(r) in wins_type_count[win_type]:
            continue
        else:
            if "X" in r and r.count("X") == 3:
                win_count["player_A"] += 1
                wins_type_count[win_type].append(arr.index(r))
                break

            elif "O" in r and r.count("O") == 3:
                win_count["player_B"] += 1
                wins_type_count[win_type].append(arr.index(r))
                break

    
def right_dignol():
    rdig = [barr[0][0],barr[1][1],barr[2][2]]
    dignol_helper(rdig,"right_dig")

def left_dignol():
    ldig = [barr[0][2],barr[1][1],barr[2][0]]
    dignol_helper(ldig,"left_dig")

def dignol_helper(arr,win_type):
    """
    This is digno check helper:
    arr: list on which action perform.
    win_type: it can be right_dig or left_dig.
    """
    if wins_type_count[win_type] != 1:
        if "X" in arr and arr.count("X") == 3:
            win_count["player_A"] += 1
            wins_type_count[win_type] = 1
        
        elif "O" in arr and arr.count("O") == 3:
            win_count["player_B"] += 1
            wins_type_count[win_type] = 1

def game_reset():
    global barr
    barr = [ x *3 for x in [[' '],[' '],[' ']]]
    global win_count
    win_count = win_count = {"player_A":0 , "player_B": 0}
    global wins_type_count
    wins_type_count = {"hr_win": [], "vrt_win": [], "right_dig":0, "left_dig":0}
    usr_position_track.clear()
    print(f"\n{'#' * 49}\n\t[ Game has been restart... ]\n")
    main()
    
def all_checks(player,name):
    '''
    Check all condition and promt for input
    '''
    if len(usr_position_track) != 9:
        while True:
            try:
                position = int(input(f"Player {name}: Enter position where you want to be {player}: "))
                if position not in [p for p in range(1, 10)]:
                    raise IndexError
                elif position in usr_position_track:
                    raise AssertionError
            except IndexError:
                print(f"\n\t[ {'+' *4} Must be within 1 to 9 {'+' *4} ]\n")
                continue
            except AssertionError:
                print(f"\n\t[ {'+' *4} Must be within 1 to 9 but not already use {'+' *4} ]\n")
                continue
            else:
                break
            
        place_userinput(player,position)
        board_play()
        hr_win()
        vrt_win()
        right_dignol()
        left_dignol()
        print(f"Score: Player A: {win_count['player_A']}\tV/S\t Palyer B: {win_count['player_B']}\n")
    
def main():    
    player1 = str(input("What is your marker X or O ?\n=> ")).upper()
    player2 = "X" if (player1.upper() != "X") else "O"
    print(f"[ Player A ]: your marker is: {player1}\n[ Player B ]: your marker is: {player2}")
    random_player = random.randint(0,1)
    
    _quit, restart = "No"
    while _quit in ["no", "n", "N", "No"]:
        while player1 not in ["X", "O"]:
            player1 = str(input("What is your marker X or O ?\n=> ")).upper()
            
        board_play()
        if (random_player == 0) and (len(usr_position_track) == 0):
            all_checks(player1,"A")
            all_checks(player2, "B")
        else:
            all_checks(player2,"B")
            all_checks(player1,"A")
  
        if len(usr_position_track) == 9:
            _quit = "yes"
            if win_count["player_A"] > win_count["player_B"]:
                print("\n\t\t[ Player A: you win!!! ]\n")
                restart = input("Do you want to play again: [ [y]es | [n]o ]: ")
            elif win_count["player_A"] < win_count["player_B"]:
                print("\n\t\t[ Player B: you win!!! ]\n")
                restart = input("Do you want to play again: [ [y]es | [n]o ]: ")
            elif win_count["player_A"] == win_count["player_B"]:
                print("\n\tThere is tie between Player A and Player B\n")
                restart = input("Do you want to play again: [ [y]es | [n]o ]: ")
            else:
                print("\n\tno one win!\n")
                restart = input("Do you want to play again: [ [y]es | [n]o ]: ")

    if restart in ["y", "Y", "yes", "Yes"]:
        game_reset()        
        
if __name__ == "__main__":
    main()
