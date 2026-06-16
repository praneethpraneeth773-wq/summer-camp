print("Marks Evaluation System")

for i in range(3):

    maths = 80
    science = 75

    print("\nStudent", i + 1)

    print("Total:", maths + science)
    print("Difference:", maths - science)
    print("Product:", maths * science)

    print(maths > science)
    print(maths < science)
    print(maths == science)

    print(maths > 35 and science > 35)
    print(maths > 90 or science > 90)
    print(not(maths < science))

    total = maths + science
    print("Total Marks:", total)

    if total >= 150:
        print("Excellent")
    else:
        print("Good")

print("Program Finished")