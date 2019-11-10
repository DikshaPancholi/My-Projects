import unittest
import HW09_Diksha_Pancholi as HW9

class Test_Repository(unittest.TestCase):
    def testRepository(self):
        path1 = "D:\SEM 3\SSW 810\Assignments\Diksha\testinstructors.txt"
        path2 = "D:\SEM 3\SSW 810\Assignments\Diksha\teststudent.txt"
        testinstructor = list(HW9.Repository("Stevens",path1,True).prettyprint_instructorsummary)
        self.assertEqual(testinstructor, ("98765	Einstein, A	SFEN 98764	Feynman, R	SFEN "))
        teststudent = list(HW9.Repository("Stevens",path2,True).prettyprint_studentsummary)
        self.assertEqual(teststudent, ("10103	Baldwin, C	SFEN 10115	Wyatt, X	SFEN "))

if __name__ == '__main__':
    unittest.main(exit =  False, verbosity= 2)