


class Employee():

    def __init__(self, first_name, last_name, salary_of_year):
        self.first_name = first_name
        self.last_name = last_name
        self.salary_of_year = salary_of_year

    def give_raise(self, increment_of_salary=5000):
        self.salary_of_year += increment_of_salary
