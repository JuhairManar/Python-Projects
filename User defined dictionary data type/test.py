import unittest
from dict2 import *

class testdict2(unittest.TestCase):

    #testing the key,value pair insertion method
    def storing_key_value_pair_test(self):
        d = dict2()
        d['a'] = 1
        d['b'] = 2
        d['c'] = 3
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 2)
        self.assertEqual(d['c'], 3)

    #testing the accessing value method
    def accessing_values_test(self):
        d = dict2()
        d['a'] = 1
        d['b'] = 2
        d['c'] = 3
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['b'], 2)
        self.assertEqual(d['c'], 3)
        
    # testing the custom expection handling method
    def exception_handling_test(self):
        d = dict2()
        with self.assertRaises(KeyNotFoundError):
            val = d['a']

    # testing the iteration
    def iteration_over_keys(self):
        d = dict2()
        d['a'] = 1
        d[10] = 3
        d['dic'] = 'dictionary'
        keys = []
        for k in d:
            keys.append(k)
        self.assertIn('a', keys)
        self.assertIn(10, keys)
        self.assertIn('dic', keys)
if __name__ == '__main__':
    unittest.main()
