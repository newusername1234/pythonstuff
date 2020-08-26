import unittest
from arithmetic_arranger import arithmetic_arranger

class UnitTests(unittest.TestCase):
    def test_arrangement(self):
        actual = arithmetic_arranger([
                                        "3 + 855", 
                                        "3801 - 2", 
                                        "45 + 43", 
                                        "123 + 49"
                                    ])
        expected = (
            "  855      3801      45      123\n"
            "+   3    -    2    + 43    +  49\n"
            "-----    ------    ----    -----\n"
            )
        self.assertEqual(actual,expected,'Test failed')

# if __name__ == "__main__":
#     unittest.main()