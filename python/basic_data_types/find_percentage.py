"""Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem"""

if __name__ == '__main__':
    n = int(input())
    # Dict for student scores
    student_marks = {}

    for _ in range(n):
        # Read in names and scores
        name, *line = input().split()
        scores = list(map(float, line))
        # Link student name to their scores
        student_marks[name] = scores
    # Read in name of student average requested
    query_name = input()
    # Find scores of requested student
    query_scores = student_marks[query_name]
    # Calculate average of student scores
    average = sum(query_scores) / len(query_scores)
    # Round to 2 decimal places
    print("{:.2f}".format(average))