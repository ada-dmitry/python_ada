import unittest

def fact(x):
    if(x==1):
        return 1
    else:
        return x*fact(x-1)
    
class FactTest(unittest.TestCase):
    '''Проверка функции факториала'''
    
    def test_5_fact(self):
        ans = fact(5)
        self.assertEqual(ans, 120)


unittest.main()