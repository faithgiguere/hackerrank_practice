"""Problem: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem"""

# Number of elements in set
n = int(input())
# Create set with elements on second line
s = set(map(int, input().split()))
# Number of commands given 
num_commands = int(input())

for i in range(num_commands):
    command = input()
    # If the given command is pop no need for a value, just pop
    if command == 'pop':
        s.pop()
    else:
        # Otherwise split command into its two parts (command and value)
        command = command.split()
        # If command is discard, perform discard on set
        if command[0] == 'discard':
            # Convert number to int
            s.discard(int(command[1]))
        else:
            # Otherwise command must be remove
            # Perform remove on set, convert number to int
            s.remove(int(command[1]))

print(sum(s))
