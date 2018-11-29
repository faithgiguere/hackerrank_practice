"""Problem: https://www.hackerrank.com/challenges/the-minion-game/problem"""

def minion_game(string):
    # List of vowels
    vowels = ['A', 'E', 'I', 'O', 'U']
    # Track points for each side
    vowel_points = 0
    con_points = 0

    for i in range(len(string)):
            # If letter is a vowel, add up all length strings starting 
            # with this char and add to vowel points
            if string[i] in vowels:
                vowel_points += (len(string) - i)
            else:
                # If letter is a vowel, add up all length strings starting 
                # with this char and add to vowel points
                con_points += (len(string) - i)
    
    # If vowel points are greater, Kevin wins
    if vowel_points > con_points:
        print('Kevin ' + str(vowel_points))
    # If consonant points are greater, Stuart wins
    elif con_points > vowel_points:
        print('Stuart ' + str(con_points))
    # Otherwise points are even and it's a draw
    else:
        print('Draw') 
