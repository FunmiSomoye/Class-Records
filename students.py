"""
Oluwafunmilayo Somoye
Dec. 2022
"""

class Student:
    """
    This is a student class for a classroom
    Attributes: first_name, last_name, semester, course1, course2
    Class variable: year
    Methods: print, add_course
    """
    def __init__(self, first_name="Edward", last_name="Jade", semester="Fall 2022", course_1=None, course_2=None):
        """
        Initialise student class with
        """
        year = 2018
        self.first_name = first_name
        self.last_name = last_name
        self.semester = semester
        self.course = [course_1, course_2]
        self.grades = [[],[]]
        self.final_score = None
        self.grade = None

    def __str__(self):
        """
        returns the string representation of the student object
        """
        return self.first_name + " " + self.last_name + " " + " " + self.semester + " " + str(self.course[0]) + " " + str(self.course[1])
    
    def add_course(self, courses):
        """
        Assign courses to students
        """
        if not self.course[0]:
            if len(courses) == 1:
                self.course[0] = courses[0]
            else:
                self.course[0] = courses[0]
                self.course[1] = courses[1]

        else:
            if self.course[0] == courses[0]:

                if courses[1]:

                    if self.course[0] != courses[1]:
                        self.course[1] = courses[1]
                        print("\nA student cannot take more than 2 courses")
                        print(f"{self.first_name} {self.last_name} already takes"\
                        f" {self.course[0]}")
                        print(f"Automatically dropped {courses[0]} for {self.first_name} {self.last_name}")
                    else:
                        print("\nYou cannot assign the same course to a student twice.")
                        raise ValueError

                else:
                    print("\nYou cannot assign the same course to a student twice.")
                    raise ValueError

            else:   
                self.course[1] = courses[0]
                if courses[1]:
                    print("\nA student cannot take more than 2 courses")
                    print(f"Automatically dropped {courses[1]} for {self.first_name} {self.last_name}")
                    

