"""Problem: https://www.hackerrank.com/challenges/merge-the-tools/problem"""

def merge_the_tools(string, k):    
    # Check each k-length segment in string
    for i in range(0, len(string), k):
        keep = set(string[i:i+k])
        for c in string[i:i+k]:
            # If letter is in set, remove and print it
            if c in keep:
                keep.remove(c)
                print(c, end='')
        print()
    return 
    