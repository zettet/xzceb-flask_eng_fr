import sys
import unittest

sys.path.append('../')
# pylint: disable=import-error
from machinetranslation import translator

class TestTranslator(unittest.TestCase):
    def test_frechToEnglish_withNoneInput_returnsNone(self):
        translatedText = translator.french_to_english(None)
        self.assertEqual(translatedText, None)

    def test_frechToEnglish_withBonjourInput_returnsHello(self):
        translatedText = translator.french_to_english("Bonjour")
        self.assertEqual(translatedText, "Hello")

    def test_englishToFrench_withNoneInput_returnsNone(self):
        translatedText = translator.english_to_french(None)
        self.assertEqual(translatedText, None)

    def test_englishToFrench_withHelloInput_returnsBonjour(self):
        translatedText = translator.english_to_french("Hello")
        self.assertEqual(translatedText, "Bonjour")

if __name__ == '__main__':
    unittest.main()
