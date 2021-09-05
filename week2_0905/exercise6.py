grade = int(input("Input your grade:"))
if grade >= 0 and grade <= 100:
    #Judge grade
    if (grade >= 90 and grade <=100):
        print('A')
    if (grade >= 80 and grade < 90):
        print('B')
    if (grade >= 70 and grade < 80):
        print('C')
    if (grade >= 60 and grade < 70):
        print('D')
    if (grade < 60):
        print('F')
else:
    print("Warning!!! The grade should be 0~100.")