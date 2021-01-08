import pandas as pd
from app import parse_address
import unittest

class TestParseAddress(unittest.TestCase):

    def test_parse_address(self):
        testcases = pd.read_csv("testcases.csv") 
        
        for idx, test_row in testcases.iterrows():
            parsed = parse_address(test_row['address'])
            self.assertEqual(parsed['street'], test_row['street'])
            self.assertEqual(parsed['housenumber'], test_row['housenumber'])

if __name__ == "__main__":
    unittest.main()