"""Problem: https://www.hackerrank.com/challenges/py-set-mutations/problem?h_r=next-challenge&h_v=zen"""

# Number of elements in set A
num_elements = int(input())
# Elements in set A
A = set(map(int, input().split()))
# Number of commands to perform on A
num_commands = int(input())

# For all following commands
for i in range(num_commands):
    # Read in command and associated set
    command = input().split()
    B = set(map(int, input().split()))
    # Perform command on A with set B
    getattr(A, command[0])(B)

# Print sum of A
print(sum(A))
