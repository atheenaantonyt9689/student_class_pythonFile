from student import Student
def run():

    s1=Student('John', [98, 80, 75, 78, 90, 69, 71])

    s2=Student('Kevin', [81, 82, 85, 90, 89, 62])
    s1.average_marks()
    s1.highest_marks()
    print("average",s1.average_marks())
    print("highest_marks",s1.highest_marks())


run()