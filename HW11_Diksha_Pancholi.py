import os 
from prettytable import PrettyTable
import collections
import sqlite3

class Repository:
    """ Defining class to store data as per university """
    filepath = "D:\SEM 3\SSW 810\Assignments\810_startup.db"
    def __init__(self,uniname,path,prettyprint):
        self.universityname = uniname
        self.directory = path
        self.student_summary = {}
        self.instructor_summary = {}
        self.major_summary = {}
        self.getinstructordata()
        self.getstudentdata()
        self.getgrades()
        self.getmajors()
        print(self.prettyprint_major_summary())
        print(self.prettyprint_studentsummary())
        print(self.prettyprint_instructorsummary())
        print(self.instructor_table_db(Repository.filepath))

    def file_reading_gen(self,path, fields, sep, header = True):
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

    def getmajors(self):
        """ Defining function to get the data from majors.txt file"""
        filename = os.path.join(self.directory,"majors.txt")
        try:
            for major in self.file_reading_gen(filename, 3, "\t"):
                self.major_summary[major[0]] = Major(major[0])
            for major in self.file_reading_gen(filename,3,'\t'):
                major_data = self.major_summary[major[0]]
                major_data.add_course(major[1],major[2])
        except FileNotFoundError as error:
            print(error)
        except ValueError as error:
            print(error)
        except Exception as error:
            print(error)

    def prettyprint_instructorsummary(self):
        """ Defining function to use pretty table to tabularize the Instructor data  """
        table = PrettyTable(field_names = Instructor.FIELDNAME)
        for instructordata in self.instructor_summary.values():
            for row in instructordata.getinstructorrow():
                table.add_row(row)
        return table

    def prettyprint_major_summary(self):
        """ Defining function to use pretty table to tabularize the Majors data related to elective and required courses """
        table = PrettyTable(field_names = Major.FIELDNAME)
        for majordata in self.major_summary.values():
            finalrow=majordata.getmajorrow()
            table.add_row(finalrow)
        return table

    def prettyprint_studentsummary(self):
        """ Defining function to use pretty table to tabularize the student data """
        table = PrettyTable(field_names = Student.FIELDNAME)
        for studentdata in self.student_summary.values():
            courses = self.major_summary[studentdata.MAJOR].updatecourseinfo(studentdata.courses)
            CWID, name, major, c = studentdata.getstudentrow()
            finalrow = [CWID, name, major]
            for item in courses:
                finalrow.append(item)
            table.add_row(finalrow)
        return table

    def instructor_table_db(self, db_path):
        """ Defining function to print new instructor table using the connection with database """
        table = PrettyTable(field_names=['CWID', 'NAME', 'DEPT', 'COURSE', 'TOTAL STUDENT'])
        query = "select instructors.CWID, instructors.Name, instructors.Dept, grades.Course, count(grades.StudentCWID) as Total_Students from grades inner join instructors on Instructors.CWID = grades.InstructorCWID group by grades.Course, instructors.CWID order by count(*) DESC"
        dbconnect = sqlite3.connect(db_path)
        for d in dbconnect.execute(query):
            table.add_row(d)
        return table


class Student:
    """ Defining class to get the student objects for each student """
    FIELDNAME = ['CWID', 'NAME', 'MAJOR', 'COMPLETED COURSES', 'REMAINING REQUIRED', 'REMAINING ELECTIVES']
    def __init__(self,cwid,name,major):
        """ Main function for Student """
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
        prettyrow = (self.CWID, self.NAME, self.MAJOR, sorted(listofcourses) )
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
        """ Defining function to sort each row for course information used in pretty table """
        for coursename, enrollcount in self.Courses.items():
            yield [self.Cwid, self.Name, self.Dept, coursename, enrollcount]

class Major:
    """ Defining a class to check the required or elective courses for a major """
    FIELDNAME = ['Dept', 'Required', 'Electives']
    def __init__(self, dept):
        """ Main function for Major class"""
        self.dept = dept
        self.electives = set()
        self.required = set()

    def add_course(self, flag, course):
        """ Defining function to get the required and elective courses in a set"""
        if flag == 'R':
            self.required.add(course)
        elif flag == 'E':
            self.electives.add(course)
        else:
            raise ValueError("Error! Unknown course flag!")
    
    def getmajorrow(self):
        """ Defining function to sort each row for course information used in pretty table """
        return [self.dept, sorted(list(self.required)), sorted(list(self.electives))]

    def remainingrequiredcourses(self,courses):
        """ Defining function to get the remaining required courses for a student)"""
        if self.required.difference(courses) == set():
            return None
        else:
            return sorted(list(self.required.difference(courses)))

    def remainingelectivecourses(self,courses):
        """ Defining function to get the remaining elective courses for a student """
        left_courses = self.electives.difference(courses)
        if len(left_courses) < len(self.electives): 
            return None
        else: 
            return sorted(list(self.electives))

    def updatecourseinfo(self,courses):
        """ Defining function to check if the student has passed the course or not """
        passed_grades = ('A', 'A-', 'B+', 'B', 'B-', 'C+', 'C') 
        completed_courses = set()
        for course, grade in courses.items():
            if grade == ' ': 
                continue
            elif grade in passed_grades:
                completed_courses.add(course)

        remaining_required = self.remainingrequiredcourses(completed_courses)
        remaining_electives = self.remainingelectivecourses(completed_courses)

        return [sorted(list(completed_courses)), remaining_required, remaining_electives]

    
if __name__ == '__main__':
    Repository("Stevens", "D:\SEM 3\SSW 810\Assignments\Diksha", True)