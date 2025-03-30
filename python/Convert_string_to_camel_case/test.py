from Convert_string_to_camel_case import to_camel_case
import unittest

class TestToCamelCase(unittest.TestCase):
    def test_to_camel_case(self):
        self.assertEqual(to_camel_case("the-stealth-warrior"), "theStealthWarrior")
        self.assertEqual(to_camel_case("The_Stealth_Warrior"), "TheStealthWarrior")
        self.assertEqual(to_camel_case("A-B-C"), "ABC")
        self.assertEqual(to_camel_case("a-b-c"), "aBC")
        self.assertEqual(to_camel_case(""), "")
        self.assertEqual(to_camel_case("hello world"), "helloWorld")
        self.assertEqual(to_camel_case("hello_world"), "helloWorld")
        self.assertEqual(to_camel_case("hello-world"), "helloWorld")

if __name__ == '__main__':
    unittest.main()

