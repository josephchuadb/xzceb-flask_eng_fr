'''
Unit Test for translator
'''
import unittest
from translator import english_to_french, french_to_english

class TestFrenchToEnglish(unittest.TestCase):
    '''
    Unit test for translating french to french
    '''
    def test_french_to_english(self):
        '''
        Unit test for translating french to french
        '''
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")

class TestEnglishToFrench(unittest.TestCase):
    '''
    Unit test for translating english to french
    '''
    def test_english_to_french(self):
        '''
        Unit test for translating english to french
        '''
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")

unittest.main()