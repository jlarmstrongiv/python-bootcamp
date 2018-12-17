#!/bin/python3

# Exercise 1

weird = 'Weird'
not_weird = 'Not Weird'

inputNumber = int(input())
if (inputNumber % 2 == 0):
  if (inputNumber >= 6 and inputNumber <= 20):
    print(weird)
  else:
    print(not_weird)
else:
  print(weird)

# Exercise 2
inputNumber = int(input())

for number in range(inputNumber):
  print(number ** 2)

# Exercise 3
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


    grade_sum = 0
    for grade in student_marks[query_name]:
        grade_sum = grade_sum + grade
    average = grade_sum / len(student_marks[query_name])
    print(f'{average:.2f}') # this line was fun
