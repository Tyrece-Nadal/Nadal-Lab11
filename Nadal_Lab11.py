#User grade input in loop
grades_list = []
passed_student = 0
total_grade = 0

#grade user input in loop
while True:
    grades_input = input("Please enter your grade(Type 'done' to finish):")
    if grades_input.isdigit() :
        grades_input = int(grades_input)
        if grades_input <= 40 or grades_input >= 100:
            print("Invalid user input!")
        else:
            grades_list.append(grades_input)
        if int(grades_list) >= 75:
            passed_student += 1

    elif grades_input.lower() == 'done':
        print("Grades List!", grades_list)
        break
    else:
        print("Invalid!")
        
#Computation
total_grade = sum(grades_list) / len(grades_list)
passing_percentage = (passed_student / len(grades_list)) * 100
print(f"Average grade {total_grade: .2f}")
print(f"Number of students passed: {passed_student}")
print(f"Passing Percentage {passing_percentage: .2f}")

        