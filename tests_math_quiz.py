import unittest
from math_quiz import integer_generation,  operator_generation, operation


class TestMathGame(unittest.TestCase):

    def integer_generation(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num =  integer_generation(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def operator_generation(self):
        rand_operator = operator_generation()
         self.assertIn(rand_operator, operators)
        pass

    def operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 5, '-', '10 - 5', 5),
                (3, 6, '*', '3 * 6', 18),
                (8, 4, '/', '8 / 4', 2),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                result = operation(num1, num2, operator)
                self.assertEqual(result, expected_answer)
                pass

if _name_ == "_main_":
    unittest.main()
