import unittest
from utils import generate_password

class TestGeneratePassword(unittest.TestCase):
    def test_password_length(self):
        length = 12
        password = generate_password(length)
        self.assertEqual(len(password), length, "Password length should be equal to the input length")

    def test_password_uppercase(self):
        password = generate_password(12)
        self.assertTrue(any(char.isupper() for char in password), "Password should contain at least one uppercase letter")

    def test_password_lowercase(self):
        password = generate_password(12)
        self.assertTrue(any(char.islower() for char in password), "Password should contain at least one lowercase letter")

    def test_password_digits(self):
        password = generate_password(12)
        self.assertTrue(sum(char.isdigit() for char in password) >= 3, "Password should contain at least 3 digits")

    def test_password_special_characters(self):
        password = generate_password(12)
        self.assertTrue(any(char in ['>', '<'] for char in password), "Password should contain at least one special character in '>' and '<'")

    def test_password_no_spaces(self):
        password = generate_password(12)
        self.assertFalse(any(char.isspace() for char in password), "Password should not contain any spaces")

if __name__ == '__main__':
    unittest.main()