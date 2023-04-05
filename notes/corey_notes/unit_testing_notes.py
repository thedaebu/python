## unit testing
# unit testing docs - https://docs.python.org/3/library/unittest.html

# import unittest
import unittest
import working_files.sample_functions as sample_functions

class TestCalc(unittest.TestCase):

    # code in setUpClass will be run once at beginning
    @classmethod
    def setUpClass(cls):
        print('set up class')

    # code in tearDownClass will be run once at end
    @classmethod
    def tearDownClass(cls):
        print('tear down class')

    # code in setUp will run before every test
    def setUp(self):
        print('set up test')

    # code in tearDown will run after every test
    def tearDown(self):
        print('tear down test')

    # methods for test must begin with prefix 'test_'
    def test_add(self):
        self.assertEqual(sample_functions.add(1, 5), 6)
        self.assertEqual(sample_functions.add(1, -1), 0)
        self.assertEqual(sample_functions.add(-1, -1), -2)

    def test_divide(self):
        # different assertion tests may require different argument forms
        self.assertRaises(ValueError, sample_functions.divide, 1, 0)
        # context manager can be used for assertions
        with self.assertRaises(ValueError):
            sample_functions.divide(1, 0)

# unit tests can be run by running file
if __name__ == '__main__':
    unittest.main()