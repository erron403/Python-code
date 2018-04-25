#!/usr/bin/env python3

barr = [ x *3 for x in [[' '],[' '],[' ']]]
arr_track = [[1,2,3],
        [4,5,6],
        [7,8,9]]
usr_position_track = []
win_count = {"player_X":0 , "player_O": 0}
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
                win_count["player_X"] += 1
                wins_type_count[win_type].append(arr.index(r))
                break

            elif "O" in r and r.count("O") == 3:
                win_count["player_O"] += 1
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
            win_count["player_X"] += 1
            wins_type_count[win_type] = 1
        
        elif "O" in arr and arr.count("X") == 3:
            win_count["player_X"] += 1
            wins_type_count[win_type] = 1

def all_checks(player):
    '''
    Check all condition and promt for input
    '''
    if len(usr_position_track) != 9:
        # check for numeric
        position = input(f"Player {player}: Enter position where you want to be {player}: ")
        while not position.isnumeric():
            print(f"\n\t[ {'+' *4} Must be within 1 to 9 {'+' *4} ]\n")
            position = input(f"Player {player}: Enter position where you want to be {player}: ")
        # check for within range    
        while int(position) not in [p for p in range(1, 10)]:
            print(f"\n\t[ {'+' *4} Must be within 1 to 9 {'+' *4} ]\n")
            position = input(f"Player {player}: Enter position where you want to be {player}: ")
        while int(position) in usr_position_track:
            print(f"\n\t[ {'+' *4} Must be within 1 to 9 but not already use {'+' *4} ]\n")
            position = input(f"Player {player}: Enter position where you want to be {player}: ")
                                                              
        place_userinput(player,position)
        board_play()
        hr_win()
        vrt_win()
        right_dignol()
        left_dignol()
        print(f"Score: Player X: {win_count['player_X']}\tV/S\t Palyer O: {win_count['player_O']}\n")
    
def game_reset():
    global barr
    barr = [ x *3 for x in [[' '],[' '],[' ']]]
    arr_track.clear()
            
def main():    
    end = "yes"
    player1 = str(input("What is you want to be X or O ?\n=> ")).upper()
    player2 = "X" if (player1.upper() != "X") else "O"           
    while end not in ["no", "n", "N", "No"]:
        while player1 not in ["X", "O"]:
            player1 = str(input("What is you want to be X or O ?\n=> ")).upper()
            
        board_play()
        all_checks(player1)
        all_checks(player2)
  
        if len(usr_position_track) == 9:
            if win_count["player_X"] > win_count["player_O"]:
                print("\n\t\t[ Player X: you win!!! ]\n")
                end = input("Do you want to continue play: [ [y]es | [n]o ]: ")
            elif win_count["player_X"] < win_count["player_O"]:
                print("\n\t\t[ Player O: you win!!! ]\n")
                end = input("Do you want to continue play: [ [y]es | [n]o ]: ")
            elif win_count["player_X"] == win_count["player_O"]:
                print("\n\tThere is tie between Player X and Player O\n")
                end = input("Do you want to continue play: [ [y]es | [n]o ]: ")
            else:
                print("\n\tno one win!\n")
                end = input("Do you want to continue play: [ [y]es | [n]o ]: ")

    if end in ["y", "Y", "yes", "Yes"]:
       game_reset()        
        
if __name__ == "__main__":
    main()
