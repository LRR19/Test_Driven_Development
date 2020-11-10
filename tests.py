from check_pwd import check_pwd
import unittest


class TDD(unittest.TestCase):
    # Test for empty string
    def test_1(self):
        empty_pwd = ""
        self.assertFalse(check_pwd(empty_pwd), msg="Error")


if __name__ == '__main__':
    unittest.main()
