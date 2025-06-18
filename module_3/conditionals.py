#example 2
from module_1.variables import temprature
from module_2.tuples_dict import student
from module_3.sets import sd_result_method

age = 18

if age >= 18:
    print("You can vote.")
else:
    print("You cant vote yet.")

#example 2
temprature = 28

if temprature >30:
    print("It's a hot day, stay hydrated.")
elif 20 <= temprature <= 30:
    print("The weather is pleasent")
else:
    print("It's a cold day!")

#example 3
student_gpa = 4.5
student_score = 75

if student_gpa >= 3.5:
    if 50 <= student_score <= 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} may be eligible for a partial scholarship ")
    elif student_score > 65:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is eligible for a full scholarship ")
    else:
        print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a scholarship ")
else:
    print(f"Student with GPA {student_gpa} and test score of {student_score} is not eligible for a scholarship ")