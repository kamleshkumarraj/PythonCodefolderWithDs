D={1:'a',2:'c',3:'c',4:'b',5:'d',6:'a',7:'a',8:'a',9:'d',10:'b'}
print("""Q1. Who is father of our nation?
a. Mahatma Gandhi
b. Subash Chandra Bosh
c. Dr. Rajendra Prashad
d. LAl Bahadur Shastri""")
q1=input("Ans. ")

print("""\nQ2. Who invented Computer?
a. Dennis Ritchie
b. Alan Turing
c. Charles Babbage
d. James Gosling """)
q2=input("Ans. ")

print("""\nQ3. Who is the father of C language?
a. Steve Jobs
b. James Gosling
c. Dennis Ritchie
d. Rasmus Lerdorf""")
q3=input("Ans. ")

print("""\nQ4. Who developed the Python language?
a. Zim Den
b. Guido van Rossum
c. Niene Stom
d. Wick van Rossum""")
q4=input("Ans. ")

print("""\nQ5. In which year was the Python language developed?
a. 1995
b. 1972
c. 1981
d. 1989""")
q5=input("Ans. ")

print("""\nQ6. Which one of the following is the correct extension of the Python file?
a. .py
b. .python
c. .p
d. None of these""")
q6=input("Ans. ")

print("""\nQ7. What is the method inside the class in python language?
a. Object
b. Function
c. Attribute
d. Argument""")
q7=input("Ans. ")

print("""\nQ8. Which of the following is not a keyword in Python language?
a. val
b. raise
c. try
d. with""")
q8=input("Ans. ")

print("""\nQ9. Which one of the following has the highest precedence in the expression?
a. Division
b. Subtraction
c. Power
d. Parentheses""")
q9=input("Ans. ")

print("""\nQ10. Which of the following option is not a core data type in the python language?
a. Dictionary
b. Class
c. Lists
d. All of the above""")
q10=input("Ans. ")


q=[q1,q2,q3,q4,q5,q6,q7,q8,q9,q10]
score=0
k=0
for v in D.values():
    if v==q[k]:
        score=score+10
    else:
        score=score-5
    k=k+1
print("Total Score =",score)