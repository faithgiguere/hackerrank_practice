"""Print a triangle of given height with and without using strings."""

# Without strings
for i in range(1,int(input())):
    print(i*(10**i -1)//9)

# With strings
for i in range(1,int(input())):
    print(str(i)*i)
    