import os 
from prettytable import PrettyTable
import collections


class Repository:
    """ Defining class to store data as per university """
    def __init__(self,uniname,path,prettyprint):
        self.universityname = uniname
        self.directory = path
        self.student_summary = {}
        self.instructor_summary = {}
        self.getstudentdata()
        self.getinstructordata()
        self.getgrades()
        print(self.prettyprint_studentsummary())
        print(self.prettyprint_instructorsummary())

    def file_reading_gen(self,path, fields, sep = '\t', header = False):
        """ Defining function to read the files """
        if not os.path.isfile(path):
            raise FileNotFoundError
        f = open(path, 'r')
        with f:
            for(idx, line) in enumerate(f):
                farray = line.strip().split(sep)
                if len(farray) != fields:
                    raise ValueError
                else:
                    if header:
                        header = False
                        continue
                    else:
                        yield tuple(i for i in farray)
    
    def getstudentdata(self):
        """ Defining function to collect the student data """
        filename = os.path.join(self.directory,"students.txt")
        try:
             for student in self.file_reading_gen(filename, 3, "\t"):
                self.student_summary[student[0]] = Student(cwid = student[0], name = student[1], major = student[2])
        except FileNotFoundError as error:
            print(error)
        except ValueError as error:
            print(error)
        except Exception as error:
            print(error)
    
    def getinstructordata(self):
        """ Defining function to collect the instructor data """
        filename = os.path.join(self.directory,"instructors.txt")
        try:
            for instructor in self.file_reading_gen(filename, 3, "\t"):
                self.instructor_summary[instructor[0]] = Instructor(cwid = instructor[0], name = instructor[1], dept = instructor[2])
        except FileNotFoundError as error:
            print(error)
        except ValueError as error:
            print(error)
        except Exception as error:
            print(error)
    
    def getgrades(self):
        """ Defining the function to collect data for grades and courses """
        filename = os.path.join(self.directory,"grades.txt")
        try:
            for grade in self.file_reading_gen(filename, 4, "\t"):
                studentobj = self.student_summary[grade[0]]
                instructorobj = self.instructor_summary[grade[3]]
                studentobj.addcoursegrades(grade[1], grade[2])
                instructorobj.addcourse(grade[1])
                
        except FileNotFoundError as error:
            print(error)
        except ValueError as error:
            print(error)
        except Exception as error:
            print(error)

    def prettyprint_studentsummary(self):
        """ Defining function to use pretty table to tabularize the student data  """
        table = PrettyTable(field_names = Student.FIELDNAME)
        for studentdata in self.student_summary.values():
            finalrow = studentdata.getstudentrow()
            table.add_row(finalrow)
        return table
    
    def prettyprint_instructorsummary(self):
        """ Defining function to use pretty table to tabularize the Instructor data  """
        table = PrettyTable(field_names = Instructor.FIELDNAME)
        for instructordata in self.instructor_summary.values():
            for row in instructordata.getinstructorrow():
                table.add_row(row)
        return table


class Student:
    """ Defining class to get the student objects for each student """
    FIELDNAME = ['CWID', 'NAME', 'COURSE']
    def __init__(self,cwid,name,major):
        """ Main function for Instructor """
        self.CWID = cwid
        self.NAME = name
        self.MAJOR = major
        self.courses = collections.defaultdict(str)

    def addcoursegrades(self, course, grades):
        """ Defining function to add grades to student data """
        self.courses[course] = grades
    
    def getstudentrow(self):
        """ Defining function to sort each row for student information used in pretty table """
        listofcourses = [course for course in self.courses]
        prettyrow = (self.CWID, self.NAME, sorted(listofcourses))
        return prettyrow


class Instructor:
    """ Defining class to get the instructor objects for each instructor """
    FIELDNAME = ['CWID', 'NAME', 'DEPT', 'COURSE', 'STUDENTS']
    def __init__(self, cwid, name, dept):
        """ Main function for Instructor """
        self.Cwid = cwid
        self.Name = name
        self.Dept = dept
        self.Courses = collections.defaultdict(int)
    
    def addcourse(self, course):
        """ Defining function to add courses to instructor data """
        self.Courses[course] += 1

    def getinstructorrow(self):
        """ Defining function to sort each row for instructor information used in pretty table """
        for coursename, enrollcount in self.Courses.items():
            yield [self.Cwid, self.Name, self.Dept, coursename, enrollcount]
    
    
if __name__ == '__main__':
    Repository("Stevens", "D:\SEM 3\SSW 810\Assignments\Diksha", True)


