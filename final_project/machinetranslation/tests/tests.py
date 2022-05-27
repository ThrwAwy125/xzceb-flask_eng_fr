import unittest
import translator

class TestTranslatorMethods(unittest.TestCase):

    def test_hello_en(self):
        self.assertEqual(translator.englishToFrench('Hello'),'Bonjour')

    def test_hello_fr(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'),'Hello')

    def test_null_en(self):
        self.assertEqual(translator.englishToFrench(None),'')

    def test_null_fr(self):
        self.assertEqual(translator.frenchToEnglish(None),'')

if __name__ == '__main__':
    unittest.main()