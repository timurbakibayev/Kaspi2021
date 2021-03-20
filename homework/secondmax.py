"""
  Дан список чисел, необходимо найти второе "по старшенству" число. Другими словами,
  необходимо найти второй максимум.
  Например:
    [1,2,3,4,5] ответ 4
    [2,3,4,3,4] ответ 4
    [2,3,4,3] ответ 3
    [1,2] ответ 1

    Список всегда содержит минимум 2 элемента.
"""
import unittest

def second_max(numbers):
    #  Incorrect solution!!!
    maximum = numbers[0]
    for n in numbers:
        if n>maximum:
            maximum = n
    sec_maximum = numbers[0]
    for n in numbers:
        if n>sec_maximum and n != maximum:
            sec_maximum = n
    return sec_maximum


class TestSecondMax(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(second_max([1,2,3,4,5]),4)

    def test_two_equal(self):
        self.assertEqual(second_max([1,2,3,5,5]),5)

    def test_all_eq(self):
        self.assertEqual(second_max([1,1,1,1]),1)

    def test_complex(self):
        self.assertEqual(second_max([1,2,3,4,3,2,5]),4)

    def test_negative(self):
        self.assertEqual(second_max([1,-1,-2,-3]),-1)

    def test_first_is_max(self):
        self.assertEqual(second_max([5,4,3,2,1]),4)

    def test_first_is_second_max(self):
        self.assertEqual(second_max([4,5,3,2,1]),4)


if __name__ == '__main__':
    unittest.main()
