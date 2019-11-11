import unittest
import HW10_Diksha_Pancholi as HW10

class Test_Studentdata(unittest.TestCase):
    
    def teststudentdata(self):
        """ Function to check the student data """
        cwid = HW10.Student.CWID
        name = HW10.Student.NAME
        major = HW10.Student.MAJOR
        allcourses = HW10.Student.courses
        completedcourses = HW10.Major.updatecourseinfo(allcourses)
        expected = ['10103', 'Baldwin, C', 'SFEN', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 555'], None]['10115', 'Wyatt, X', 'SFEN', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 555'], None]['10172', 'Forbes, I', 'SFEN', ['SSW 555', 'SSW 567'], ['SSW 564'], ['CS 501', 'CS 513', 'CS 545']]['10175', 'Erickson, D', 'SFEN', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 555'], ['CS 501', 'CS 513', 'CS 545']]['10183', 'Chapman, O', 'SFEN', ['SSW 689'], ['SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']]['11399', 'Cordova, I', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], None]['11461', 'Wright, U', 'SYEN', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810']]['11658', 'Kelly, P', 'SYEN', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]['11714', 'Morton, A', 'SYEN', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]['11788', 'Fuller, E', 'SYEN', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], None]
        calculated = [cwid,name,major,completedcourses]
        self.assertEqual(expected, calculated)

class testmajorsdata(unittest.TestCase):
    def majorsdatatest(self):
        """ Function to check the Majors data """
        expected1 = [['SFEN', ['SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545']]['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810']]]
        department = HW10.Major.dept
        Required = HW10.Major.required
        Elective = HW10.Major.electives
        calculated1 = [department, Required, Elective]
        self.assertEqual(expected1, calculated1)
            
if __name__ == '__main__':
    unittest.main(exit =  False, verbosity= 2)