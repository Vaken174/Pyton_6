import unittest
import sys

def compute_factorial(number: int) -> int:
    if number < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if number == 0:
        return 1
    
    factorial_result = 1
    for current_multiplier in range(1, number + 1):
        factorial_result *= current_multiplier
        if factorial_result > sys.maxsize:
            raise ValueError(f"Факториал для {number} не поддерживается типом int")
    
    return factorial_result

class FactorialTestCase(unittest.TestCase):
    def test_zero_factorial(self):
        self.assertEqual(compute_factorial(0), 1)

    def test_positive_factorials(self):
        self.assertEqual(compute_factorial(1), 1)
        self.assertEqual(compute_factorial(5), 120)
        self.assertEqual(compute_factorial(10), 3628800)

    def test_negative_input(self):
        with self.assertRaises(ValueError) as error_context:
            compute_factorial(-5)
        self.assertEqual(str(error_context.exception), "Факториал отрицательного числа не определен")

    def test_integer_overflow(self):
        boundary_value = 1
        while True:
            try:
                compute_factorial(boundary_value)
                boundary_value += 1
            except ValueError:
                break
 
        with self.assertRaises(ValueError) as error_context:
            compute_factorial(boundary_value)
        self.assertEqual(str(error_context.exception), 
                        f"Факториал для {boundary_value} не поддерживается типом int")

    def test_max_supported_value(self):
        max_safe_value = 1
        while True:
            try:
                result = compute_factorial(max_safe_value)
                max_safe_value += 1
            except ValueError:
                max_safe_value -= 1
                break
        
        self.assertTrue(isinstance(compute_factorial(max_safe_value), int))

if __name__ == "__main__":
    unittest.main()