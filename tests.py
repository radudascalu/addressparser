import pandas as pd
from app import parse_address
import unittest

class TestParseAddress(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestParseAddress, self).__init__(*args, **kwargs)
        self.test_cases = pd.read_csv("testcases.csv") 

    def run_testcases(self, difficulty):
        for idx, test_row in self.test_cases[self.test_cases.difficulty == difficulty].iterrows():
            parsed = parse_address(test_row['address'])
            self.assertEqual(parsed['street'], test_row['street'])
            self.assertEqual(parsed['housenumber'], test_row['housenumber'])

    def test_simple(self):
        self.run_testcases(1)
        
    def test_advanced(self):
        self.run_testcases(2)

if __name__ == "__main__":
    unittest.main()