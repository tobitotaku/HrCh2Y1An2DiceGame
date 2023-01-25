# This code template is created for Challenge 2: Dice Game. 
# The template must be complete by the student before the submission.

import random as rand
import string
import os

# global variables
# todo 1: std_number must have the correct student number
std_number = '1042623'
# name student: Tobias Roessingh

# game parameters. Do Not change these variables.
player_one = 'peter'
player_two = 'colin'
test_cases = [ 
    {player_one: {'sides':4,'num':9} , player_two : {'sides':6,'num':6}} ,
    {player_one: {'sides':4,'num':3} , player_two : {'sides':9,'num':2}} , 
    {player_one: {'sides':8,'num':3} , player_two : {'sides':14,'num':1}} , 
    {player_one: {'sides':3,'num':10} , player_two : {'sides':6,'num':1}} , 
    {player_one: {'sides':4,'num':1} , player_two : {'sides':20,'num':1}} 
    ]


def simulate_general_Euler_205(case:dict , num_of_experiments:int = 1_000_000): # Do Not Change this function
    '''
    This function simulates the probability of Dice Game, i.e. Euler 205.
    '''
    def general_dice(sides:int=6): # Do Not Change this function
        '''
        This function implements a general dice function
        '''
        return lambda : rand.randint(1,sides) if sides > 1 else None
    
    def get_dice_collections(): # Do Not Change this function
        '''
        Each player has a collection of dice. This function returns the collections in a dictionary.
        '''    
        dice_peter = general_dice(case[player_one]['sides'])
        dice_colin = general_dice(case[player_two]['sides'])
        return {player_one: [dice_peter]*case[player_one]['num'] , player_two:[dice_colin]*case[player_two]['num']}

    def calculate_probability():
        '''
        This function calculates the probability of winning for one given case.
        '''
        winning_probability = {player_one:0,player_two:0,'Draw':0}
        # todo 2: Complete the implemetation of this function
        # start here ..............

        total = 0
        p1_wins = 0
        p2_wins = 0
        draws = 0
        # all possible sum(dice rolls) of player_one
        for i in range(1 * case[player_one]['num'], case[player_one]['sides'] * case[player_one]['num']):
            
            # all possible sum(dice rolls) of player_two
            for j in range(1 * case[player_two]['num'], case[player_two]['sides'] * case[player_two]['num']):
                total += 1
                if i == j:
                    draws += 1
                elif i > j:
                    p1_wins += 1
                elif i < j:
                    p2_wins += 1

        winning_probability[player_one] = round(p1_wins / total, 2)
        winning_probability[player_two] = round(p2_wins / total, 2)
        winning_probability['Draw'] = round(draws / total, 2)

        # finish here ..............       
        return winning_probability # the result of the simulation will be returned here
    return calculate_probability() # do not change this


def find_num_dice_equal_prob(case , max_num_dice=30):
    # probability of the given case will be calculated here
    probs = simulate_general_Euler_205(case)
    message_init_case = 'Initial result for case:'+str(case)+' With Probabilities:'+str(probs)
    fair_case = case
    fair_probs = probs

    # todo 3: complete the function to find a case for a fair game
    # hint: iterate in a loop for max_num_dice and find number of dice for both players such that they play a fair game
    # in each iteration call simulate_general_Euler_205 and check probabilities, increase number of dice for minimum probability, 
    # then call the function again with a new case. 
    # At the end fair_case will contain information of case with updated number of dice and fair_probs will contain probabilities of fair case.

    # start here ..............
    #

    def recursive_fair_dices(case):
        probs = simulate_general_Euler_205(case)
        if case[player_one]['num'] >= max_num_dice or case[player_two]['num'] >= max_num_dice:
            # max dices reached!
            return False

        if probs[player_one] == probs[player_two]:
            return case

        if probs[player_one] > probs[player_two]:
            case[player_two]['num'] += 1
            return recursive_fair_dices(case)

        elif probs[player_one] < probs[player_two]:
            case[player_one]['num'] += 1
            return recursive_fair_dices(case)

    # lets start at 1 dice
    fair_case[player_one]['num'] = 1
    fair_case[player_two]['num'] = 1
    fair_case = recursive_fair_dices(fair_case)
    fair_probs = simulate_general_Euler_205(fair_case)

    # finish here ..............       
    #here fair_case and fair_probs must be ready with the results of the search    
    message_fair_case = 'Final result for fair game in case:'+str(fair_case)+' With Probabilities:'+str(fair_probs)
    return message_init_case+os.linesep+message_fair_case


def main(): # Do Not change this function
    '''
    This function checks student number, iterates over test cases and stores the final results in a log file.
    '''
    if len(std_number)!=7 or len(set(std_number)-set(string.digits)):
        print('ERROR: student number is not valid')
        return

    log=''
    log_ext = '.txt'
    log_name = 'dice_game_'
    out_file_name = log_name + std_number + log_ext
    # iterate over the test cases
    for case_num in range(0,len(test_cases)):
        log = log + os.linesep*2 + 'CASE '+str(case_num)+os.linesep*2 + find_num_dice_equal_prob(test_cases[case_num])
    # print the result
    print(log)
    # store the result in a log file
    with open(out_file_name,'w') as log_file:
        log_file.write(log)
        log_file.close()
    
main() # Do Not change this function
