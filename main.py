"""
Oluwafunmilayo Somoye
Dec. 2022
"""

from students import Student as st
from subjects import Subject as sj
from datetime import datetime as dt

def validate(string):
    """
    Check if a string contains
    only letters else raise error
    """
    if not isinstance(string, str):
        raise TypeError("data must be a string")

    if string.isdigit():
        print("\nOnly enter words.")
        raise AttributeError

def take_names():
    """
    Collects the first and last names
    of a student from the user
    """
    #first name
    first_name = input("\nEnter first name: ")
    validate(first_name)

    if len(first_name.split()) > 1:
        print("\nYou can only enter 1 first name")
        raise ValueError

    first_name = first_name.capitalize()

    #last name
    last_name = input("Enter last name: ")
    validate(last_name)
    last_name = last_name.capitalize()

    return first_name, last_name


def student_id(name_list, my_dict):
    """
    Get student id based on names
    """
    if not isinstance(name_list, set):
        raise TypeError("data must be a set")
    if not isinstance(my_dict, dict):
        raise TypeError("data must be a dictionary")

    first_name, last_name = take_names()
    if last_name in name_list:
        for i in my_dict.copy():
            if (my_dict[i].first_name == first_name) and (my_dict[i].last_name == last_name):
                index = i
                break #stop for loop                 
    else:
        print("\nYou have entered the last name of someone who is not in the record.")
        raise LookupError
    return index


def course_id(course_code, code_list, my_dict):
    """
    Get student id based on value
    """
    if not isinstance(course_code, str):
        raise TypeError("data must be a string")
    if not isinstance(code_list, set):
        raise TypeError("data must be a set")
    if not isinstance(my_dict, dict):
        raise TypeError("data must be a dictionary")
    
    if course_code in code_list:
        print(f"\n{course_code} exists")
        for i in my_dict.copy():
            if (my_dict[i].code == course_code):
                index = i
                break #stop for loop                 
    else:
        print("\nThe course code you have entered is not valid.")
        raise LookupError
    return index


def main():
    """
    This program allows you to: 
    """
    #create pre-recorded students
    students = dict()

    def save_new_stu(stu_dict, my_value):
        """
        Save newly created course in student records
        (Dictionary)
        """
        if not isinstance(stu_dict, dict):
            raise TypeError("data must be a dictionary")
    
        global stu_id_base
        stu_id_base += 1
        stu_dict[stu_id_base] = my_value

    save_new_stu(students, st("Jason", "Durello"))
    save_new_stu(students, st("Jason", "Stewart"))
    save_new_stu(students, st("John", "Doe"))
    save_new_stu(students, st("Penelope", "Pittstop"))

    #create a set of unique student last name
    last_names = {students[i].last_name for i in students}

    #create pre-recorded courses
    courses = dict()

    def save_new_course(course_dict, my_value):
        """
        Save newly created course in course records
        (Dictiionary)
        """
        if not isinstance(course_dict, dict):
            raise TypeError("data must be a dictionary")
        global course_id_base
        course_id_base += 1
        course_dict[course_id_base] = my_value

    save_new_course(courses, sj("Discrete Structures", "MTH215"))
    save_new_course(courses, sj("Computer Science", "CS201"))

    #create a set of unique course codes
    course_codes = {courses[i].code for i in courses}
    course_names = {courses[i].name for i in courses}

    choice = ""
    while choice != "x":
        try:
            print("""\nEnter:
            1 to add a new Student to system
            2 to print the details of a student
            3 to remove a Student from system
            4 to add a new Course to system
            5 to assign a Course to a Student  
            'x' to exit
            """)
            print("What would you like to do?")
            choice = input("Enter a selection from menu: ")

            if choice not in ("1", "2", "3", "4", "5", "x"):
                print("\nThe menu option you have entered does not exist.")
                raise LookupError

             #Add a student
            if choice == "1":
                first, last = take_names()
                
                #check if there is already a student with the entered last name
                if last in last_names:
                    print("\nA student with that name already exists")
                    raise ValueError
                else:
                    yr = dt.now().year #get today's year
                    new_student = st(first, last) #create new student
                    save_new_stu(students, new_student)
                    students[stu_id_base].year = yr #update year variable for new student
                    last_names.add(last) #update unique last names set
                    print(f"\n{first} {last} has been added to system")

            #Print student details
            elif choice == "2":
                print("Which student's details would you like to see?")
                id = student_id(last_names, students)
                print("")
                print(students[id])

            #Delete record of a student
            elif choice == "3":
                i = student_id(last_names, students)
                print(f"\nDeleted {students[i].first_name} {students[i].last_name} from system.")
                del students[i]
                #reset names set since more than one students may bear
                #the same names
                last_names = {students[name].last_name for name in students} 
                   
            #Add a course
            elif choice == "4":
                #give pointers to avoid errors
                print("Course name can consist of more than one word.")
                print("Course codes are alphanumeric and should be only 1 word"\
                " E.g. EST504")

                name = input("\nEnter course name: ")
                validate(name)
                name = name.capitalize()
                code = input("Enter course code: ")

                print(name, code)
                
                #raise error if course code is more than 1 word
                if len(code.split()) > 1: 
                    print("\nCourse codes should only consists of one word.")
                    print("There should not be any spaces between letters and numbers.")
                    raise ValueError

                #raise error if course code is not alpha numeric
                if not code.isalnum():
                    print("\nCourse codes must be alphanumeric. E.g. MTH215")
                    raise AttributeError

                #If course code already exists
                if (name in course_names):
                    print("\nThe course name you have entered already exists.")
                    raise ValueError

                #If course code already exists
                if code in course_codes:
                    print("\nThe course code you have entered already exists.")
                    raise ValueError

                save_new_course(courses, sj(name, code))
                print(f"{name} {code} has been added to courses")
                
            #Assign a course to a student
            elif choice == '5':
                #select student to assign course to
                print("\nSelect a student to assign course to.")
                print("Some students may have similar names.")
                print("It is important the right course is assigned to the right student.")
                st_id = student_id(last_names, students)
        
                #select course(s) to assign
                print("\nThe available courses are: ")
                #print courses
                for k, v in courses.items():
                    print(k, v.name, v.code)
            
                #take user input
                print("\nSelect course(s) to assign to a student")
                chosen_course = input("Enter one or two course code(s) "\
                "separated by spaces: ")
                chosen_course = chosen_course.upper()
                chosen_course = chosen_course.split() #convert to list
                
                #check if user input is more than two
                if len(chosen_course) > 2:
                    print("\nYou cannot enter more than two courses.")
                    raise ValueError

                if len(chosen_course) > 1:
                    if chosen_course[1] == chosen_course[0]:
                        print("\nYou cannot assign the same course to a student twice.")
                        raise ValueError
                    else:
                        pass
                else:
                    pass

                #get course class object
                new_list = []
                for course in chosen_course:
                    c_id = course_id(course, course_codes, courses)
                    new_list.append(courses[c_id])

                #Assign courses to chosen student
                students[st_id].add_course(new_list)
                if len(new_list) == 1:
                    print(f"\n{students[st_id].first_name} now offers {students[st_id].course[0].name}")
                else:
                    print(f"\n{students[st_id].first_name} now offers {students[st_id].course[0].name} "\
                    f"and {students[st_id].course[1].name}")

        except AttributeError:
            print("Please key in a valid entry")

        except LookupError:
            print("Please enter in a valid value")
        
        except ValueError:
            print("Please enter valid value(s) exactly as required.")
        
        except TypeError as ex:
            print("Invalid Type:", type(ex), ex)




if __name__ == "__main__":
    #initiate global variables
    stu_id_base = 0
    course_id_base = 0
    main()
