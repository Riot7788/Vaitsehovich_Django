import unittest
from django.test import TestCase
# from .queue import QueueTest

from .queue import UniqueQueue

import random




# class TestStringMethods(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')
#
#     def test_isupper(self):
#         self.assertTrue('FOO'.isupper())
#         self.assertFalse('Foo'.isupper())
#
#     def test_split(self):
#         s = 'hello world'
#         self.assertEqual(s.split(), ['hello', 'world'])
#         # check that s.split fails when the separator is not a string
#         with self.assertRaises(TypeError):
#             s.split(2)
#
# if __name__ == '__main__':
#     unittest.main()

# # TDD
# class TestQueue(TestCase):
#
#     def test_queue_exist(self):
#         q = QueueTest(strategy="LIFO")
#
#     def test_exist_strategy_fifo_and_lifo(self):
#         with self.assertRaises(TypeError):
#             q = QueueTest(strategy="LFA")
#
#     def test_add_some_value_to_queue(self):
#         q = QueueTest(strategy="FIFO")
#         first_values = 4
#         q.add(first_values)
#         get_value = q.pop()
#         self.assertEqual(get_value, first_values)
#
#     # очередь работает правильно при добавлении
#     # нескольких значений и их извлечении в порядке "FIFO"
#     def test_add_queue_multi_value(self):
#         q = QueueTest(strategy="FIFO")
#         test_values = [4,3,2]
#
#         for ind in range(len(test_values)):
#             q.add(test_values[ind])
#
#         for ind in range(len(test_values)):
#             get_value = q.pop()
#             self.assertEqual(get_value, test_values[ind])
#
#     # проверяет, что значение, добавленное первым, извлекается первым
#     def test_add_value_mega_values(self):
#         q = QueueTest(strategy="FIFO")
#         first_value = 44
#         q.add(first_value)
#
#         for i in range(20):
#             value = random.randint(1,10)
#             q.add(value)
#
#         get_value = q.pop()
#         self.assertEqual(get_value, first_value)
#
#     # проверяет, что метод pop корректно возвращает None
#     def test_empty_values(self):
#         q = QueueTest(strategy="FIFO")
#         first_value = 44
#         q.add(first_value)
#         get_value = q.pop()
#         self.assertEqual(get_value, first_value)
#         get_value = q.pop()
#         self.assertIsNone(get_value)


class TestHomeWorkQueue(TestCase):

    def test_queue_exist(self):
        q = UniqueQueue(strategy="LIFO")
        self.assertIsInstance(q, UniqueQueue)

    def test_add_unique_elements(self):
        q = UniqueQueue(strategy="FIFO")
        q.add(1)
        q.add(2)
        q.add(1)  # Добавление дубликата
        self.assertEqual(q.length(), 2)
        self.assertEqual(q.pop(), 1)
        self.assertEqual(q.pop(), 2)
        self.assertIsNone(q.pop())  # Проверка извлечения после очистки очереди

    def test_add_elements(self):
        q = UniqueQueue(strategy="LIFO")
        q.add(1)
        q.add(2)
        self.assertEqual(q.length(), 2)

    def test_length_empty_queue(self):
        q = UniqueQueue(strategy="LIFO")
        self.assertEqual(q.length(), 0)

    def test_last_empty_queue(self):
        q = UniqueQueue(strategy="LIFO")
        self.assertIsNone(q.last())

    def test_last_single_element(self):
        q = UniqueQueue(strategy="LIFO")
        q.add(1)
        self.assertEqual(q.last(), 1)

    def test_last_multiple_elements(self):
        q = UniqueQueue(strategy="LIFO")
        q.add(1)
        q.add(2)
        q.add(3)
        self.assertEqual(q.last(), 3)

    def test_to_get_length(self):
        q = UniqueQueue(strategy="FIFO")
        test_values = [4, 3, 2]

        # Проверка после каждого добавления элемента
        for ind in range(len(test_values)):
            q.add(test_values[ind])
            self.assertEqual(q.length(), ind + 1)
            self.assertEqual(q.last(), test_values[ind])
