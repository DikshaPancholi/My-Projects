import unittest
import HW11_Diksha_Pancholi as HW11

class Repository(unittest.TestCase):
    def testRepository(self):
        ''' Defining function to test the new instructor summary table in repository class'''
        Expected = ('98763', 'Rowland, J', 'SFEN','SSW 810','4')
        self.assertEqual(HW11.Repository.instructor_table_db("D:\SEM 3\SSW 810\Assignments\810_startup.db")[1], Expected)
        
            
if __name__ == '__main__':
    unittest.main(exit =  False, verbosity= 2)