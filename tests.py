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

    # test for length that's greater than 20. PASSED
    def test_3b(self):
        pwd = "lamp1234567891011121314"
        self.assertFalse(check_pwd(pwd), msg='Error')

    # test for lower case
    def test_4(self):
        pwd = "LAMP362@"
        self.assertFalse(check_pwd(pwd), msg='Error')

    # test for upper case
    def test_5(self):
        pwd = "lamp362@"
        self.assertFalse(check_pwd(pwd), msg='Error')

    # test for upper and lower case. PASSED
    def test_6(self):
        pwd = "Lamp362@"
        self.assertTrue(check_pwd(pwd), msg='Error')

    # test for digits
    def test_7(self):
        pwd = "GreenLamp!"
        self.assertFalse(check_pwd(pwd), msg="Error")

    # test for symbols
    def test_8(self):
        pwd = "Lamps362"
        self.assertFalse(check_pwd(pwd), msg='Error')

    # # test for symbols with symbols. PASSED
    # def test_8b(self):
    #     pwd = "Lamps362!@"
    #     self.assertTrue(check_pwd(pwd), msg='Error')
    #
    # # test length under min. PASSED
    # def test_9(self):
    #     pwd = "Lamp3-"
    #     self.assertFalse(check_pwd(pwd), msg='Error')
    #
    # # test min length. PASSED
    # def test_10(self):
    #     pwd = "Lamp362+"
    #     self.assertTrue(check_pwd(pwd), msg='Error')
    #
    # # test max length. PASED
    # def test_11(self):
    #     pwd = "CS362+Fall2020^Break"
    #     self.assertTrue(check_pwd(pwd), msg='Error')
    #
    # # test over max length. PASSED
    # def test_12(self):
    #     pwd = "CS362+Fall2020-Breaks&pets"
    #     self.assertFalse(check_pwd(pwd), msg='Error')
    #
    # # test just letters. PASSED
    # def test_13(self):
    #     pwd = "Lampsarecool"
    #     self.assertFalse(check_pwd(pwd), msg='Error')
    #
    # # test just digits. PASSED
    # def test_14(self):
    #     pwd = "12345678"
    #     self.assertFalse(check_pwd(pwd), msg='Error')
    #
    # # test just symbols. PASSED
    # def test_15(self):
    #     pwd = "-~`!@#$%^&*()_+="
    #     self.assertFalse(check_pwd(pwd), msg='Error')
    #
    # # test digits and symbols. PASSED
    # def test_16(self):
    #     pwd = "-~`!@#$%^&*()_+=26"
    #     self.assertFalse(check_pwd(pwd), msg='Error')
    #
    # # test letters and symbols. PASSED
    # def test_17(self):
    #     pwd = "Lamp-~`!@#"
    #     self.assertFalse(check_pwd(pwd), msg='assertion failed')
    #
    # # test symbols not allowed. PASSED
    # def test_18(self):
    #     pwd = "Lamp123{}"
    #     self.assertFalse(check_pwd(pwd), msg='assertion failed')
    #
    # # test digits and letters. PASSED
    # def test_19(self):
    #     pwd = "Lamps236"
    #     self.assertFalse(check_pwd(pwd), msg='Error')
    #
    # # test symbols and letters. PASSED
    # def test_20(self):
    #     pwd = "Lamps!@#$"
    #     self.assertFalse(check_pwd(pwd), msg='Error')


if __name__ == '__main__':
    unittest.main()
