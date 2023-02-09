'''
Unit Test for translator
Author: Joseph Chua Debao
'''
import unittest
from translator import french_to_english, english_to_french

class TestFrenchToEnglish(unittest.TestCase):
    '''
    Unit test for translating french to french
    '''
    def french_to_english(self):
        '''
        Unit test for translating french to french
        '''
        self.assertEqual(french_to_english(""), "")
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Hello'), 'Bonjour')

class TestEnglishToFrench(unittest.TestCase):
    '''
    Unit test for translating english to french
    '''
    def english_to_french(self):
        '''
        Unit test for translating english to french
        '''
        self.assertEqual(english_to_french(""), "")
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()
