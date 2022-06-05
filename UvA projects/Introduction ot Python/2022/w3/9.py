"""
Create a 'Student' class that has three string attributes: 'name', 'department',
and 'university'.

'name' and 'department' must be passed to the 'Student' class at object
construction (in this order).

'university' is an optional argument in the constructor, which takes the value
'University of Amsterdam' by default.

Finally, add a method called 'info' to the class, which returns the following
string:
"[NAME] studies at the [DEPT] Department of [UNI]."
where:
- [NAME] should be replaced with the student's name,
- [DEPT] should be replaced with the student's department, and
- [UNI] should be replaced with the student's university.

Use the (incomplete) code segment at the bottom of this question to start with,
and modify it as needed.

For example:
If we create an object from your class as:
student_1 = Student('Mike', 'Psychology')
then the method call student_1.info() should return the string:
'Mike studies at the Psychology Department of University of Amsterdam.'
"""

class Student:
    def __init__(self, name, department, university= 'University of Amsterdam'):
        self.name = name
        self.department = department
        self.university = university

    def info(self):
        return self.name + ' studies at the '+ self.department + ' Department of '+ self.university

student_1 = Student('Mike', 'Psychology')
print(student_1.info())

Student('Astrid', 'Chemistry', university='University of Maastricht').info()