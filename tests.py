from check_pwd import check_pwd
import unittest


class TDD(unittest.TestCase):
    # Test for empty string
    def test_1(self):
        empty_pwd = ""
        self.assertFalse(check_pwd(empty_pwd), msg="Error")

    # test a string
    def test_2(self):
        pwd1 = "Lamp362@"
        self.assertTrue(check_pwd(pwd1), msg='Error')

    # test length 8-20 inclusive. Test less than 8
    def test_3(self):
        pwd2 = "lamp"
        self.assertFalse(check_pwd(pwd2), msg='Error')


if __name__ == '__main__':
    unittest.main()
