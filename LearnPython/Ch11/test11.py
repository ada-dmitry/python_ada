import unittest
from task11 import Employee


class TestEmployee(unittest.TestCase):
    '''Класс для тестирования класса Employee'''

    def setUp(self):
        self.my_employee = Employee('Renal', 'Gayazov', 30000)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(self.my_employee.salary_of_year, 35000)

    def test_give_custom_raise(self):
        self.my_employee.give_raise(9000)
        self.assertEqual(self.my_employee.salary_of_year, 39000)

if __name__ == '__main__':
    unittest.main()

