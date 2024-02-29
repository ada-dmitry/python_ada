import json
import unittest

def input_digit():
    try:
        with open('answer.json') as f:
            x = json.load(f)
            print(f'Ваше любимое число: {x}')
    except FileNotFoundError:
        x = int(input('Введите ваше любимое число: '))
        with open('answer.json', 'w') as f:
            json.dump(x, f)
    

def output_digit():
    with open('answer.json') as f:
        x = json.load(f)
    print(f'Ваше любимое число: {x}')

input_digit()

output_digit()

class InputTest(unittest.TestCase):
    '''Тесты для функции ввода с клавиатуры'''
    def test_