# test_addition.py

import unittest
import xmlrunner  # Optional: only needed for JUnit-style XML reports

# === Function to Test ===
def add_numbers(a, b):
    return a + b

# === Unit Tests ===
class TestAddNumbers(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_mixed(self):
        self.assertEqual(add_numbers(-2, 3), 1)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 5), 5)
        self.assertEqual(add_numbers(5, 0), 5)

# === Run Tests ===
if __name__ == '__main__':
    # Run with JUnit-style report
    with open('junit-report.xml', 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output), verbosity=2)

    # OR run without report:
    # unittest.main()
