# Name: Janvi Sehrawat
# Date: 7/11/2025
# Title: Gradebook Analyzer

# ---TASK 1--- #

def main():
    print("-" * 100)
    print("\t WELCOME TO THE GRADEBOOK ANALYZER!!")
    print("\n A GradeBook Analyzer collects student names and marks,\n computes average, median, highest, and lowest scores, assigns grades, separates\n pass/fail students using list comprehensions, and displays results in a formatted table.")
    print("-" * 100)

    while True:
        print("\nMenu:")
        print("1. Analyze a mew class")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':

# ---TASK 2--- #

            marks = {}
            a= int(input("\nEnter the number of students: "))
            for i in range(a):
                name= input(f"Enter the name of student {i+1}: ")
                marks[name] = float(input(f"Enter the marks of {name}: "))

# ---TASK 3--- #

            print("\nMarks Dictionary: ", marks)
            def calculate_average(marks_dict):
                total = sum(marks_dict.values())
                average = total/len(marks_dict)
                return average

            def calculate_median(marks_dict):
                marks_list = sorted(marks_dict.values())
                a = len(marks_list)

                if a%2 == 0:
                    mid1 = marks_list[a // 2-1]
                    mid2 = marks_list[a // 2]
                    median = (mid1 + mid2)/2
                else:
                    median = marks_list[a // 2]
                return median

            def find_max_score(marks_dict):
                top_student = max(marks_dict, key=marks_dict.get)
                top_marks = marks_dict[top_student]
                return top_student, top_marks

            def find_min_score(marks_dict):
                low_student = min(marks_dict, key=marks_dict.get)
                low_marks = marks_dict[low_student]
                return low_student, low_marks

            avg = calculate_average(marks)
            median = calculate_median(marks)
            top_student_name, top_score = find_max_score(marks)
            lowest_student_name, low_score = find_min_score(marks)

            print("\n---- STATISTICAL ANALYSIS ----")
            print(f"Average Marks: {avg: .2f}")
            print(f"Median Marks: {median: .2f}")
            print(f"Highest Marks: {top_student_name} ({top_score})")
            print(f"Lowest Marks: {lowest_student_name} ({low_score})")

# ---TASK 4--- #

            def assign_grades(marks_dict):
                grades = {}
                for name, mark in marks_dict.items():
                    if mark >= 90:
                        grade = 'A'
                    elif mark >= 80:
                        grade = 'B'
                    elif mark >= 70:
                        grade = 'C'
                    elif mark >= 60:
                        grade = 'D'
                    else:
                        grade = 'F'
                    grades[name] = grade
                return grades

            def count_grade_distribution(grades_dict):
                distribution = {}
                for grade in grades_dict.values():
                    distribution[grade] = distribution.get(grade, 0)+1
                return distribution

            grades = assign_grades(marks)
            distribution = count_grade_distribution(grades)

            print("\n---- GRADE DISTRIBUTION ----")
            print("\nGrade Dictionary: ",grades)
            for grade, count in distribution.items():
                print(f"Grade {grade}: {count} sutdent(s)")

# ---TASK 5--- #

            def get_pass_fail_lists(marks_dict):
                passed_students = [name for name, marks in marks_dict.items() if marks >= 60]
                failed_students = [name for name, marks in marks_dict.items() if marks < 60]
                return passed_students, failed_students

            passed, failed = get_pass_fail_lists(marks)

            print("\n---- Pass/Fail Summary ----")
            print(f"Passed Students ({len(passed)}): {passed}")
            print(f"Failed Students ({len(failed)}): {failed}")

# ---TASK 6--- #

            def display_results_table(marks_dict, grades_dict):
                print("\n-------- GRADEBOOK RESULTS --------")
                print("{:<15} {:<10} {:<10}".format("Name", "Marks", "Grade"))
                print("-"* 40)
                for name in marks_dict:
                    print("{:<15} {:<10} {:<10}".format(name, marks_dict[name], grades_dict[name]))

                print("-"*40)

            display_results_table(marks, grades)
        
        elif choice == '2':
            print("\nThank You For Using Gradebook Analyzer!!")
            break

        else:
            print("\nInvalid choice! Please select 1 or 2.")

if __name__ == "__main__":

    main()
