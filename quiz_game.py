print("\n\t\t\tWelcome to Quiz Game\n")
score=0
total_questions=3
 
answer = input("\nQ.1: Who developed the Python language?\n\
A. Zim Den \nB. Guido van Rossum \nC. Niene Stom \nD. Wick van Rossum\n> ")
if answer.lower() == 'b':
    score += 1
    print('Correct Answer...!')
else:
    print('Wrong Answer :(')
 
 
answer = input("\nQ.2: In which year was the Python language developed?\n\
A. 1995 \nB. 1972 \nC. 1981 \nD. 1989\n> ")
if answer.lower()=='d':
    score += 1
    print('Correct Answer...!')
else:
    print('Wrong Answer :(')
 
answer = input("\nQ.3: In which language is Python written?\n\
A. English \nB. PHP \nC. C \nD. All of the above\n> ")
if answer.lower()=='c':
    score += 1
    print('Correct Answer...!')
else:
    print('Wrong Answer :(')
 
print('\nThankyou for Playing, you attempted',score,\
"questions correctly!")
mark=(score/total_questions)*100
print('\nScore obtained:',int(mark))