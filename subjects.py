"""
Oluwafunmilayo Somoye
Dec. 2022
"""

class Subject:
    """
    This is the subject class for a classroom
    Attributes: name, code
    Methods: print
    """
    def __init__(self, name="Basic Mathematics", code="MTH 001"):
        """
        Initialise subjects class with
        """
        self.name = name
        self.code = code
        self.college = "College of Mathematics and Statistics"

    def __str__(self):
        """
        Returns the string representation of the subject object
        """
        return self.name + " " + self.code + " " + " " + self.college