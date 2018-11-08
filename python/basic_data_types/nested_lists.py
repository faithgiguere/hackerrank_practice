"""Problem: https://www.hackerrank.com/challenges/nested-list/problem """

if __name__ == '__main__':
    # List to hold students
    students = []
    
    for _ in range(int(input())):
        # Read in name and score
        name = input()
        score = float(input())
        # Create a student
        student = [name, score]
        # Add student to student list
        students.append(student)
        
    # Sort scores, remove duplicate grades    
    scores = sorted(set(s[1] for s in students))
    second_highest = scores[1]
    # Find names of students with second highest score and sort alphabetically
    second_highest_names = sorted(s[0] for s in students if s[1] == second_highest)
    
    for name in second_highest_names:
        print(name)