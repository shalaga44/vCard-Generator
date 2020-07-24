import unittest

from Generator import VCARDGenerator
from Utils.functions import *


class GeneralTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = VCARDGenerator()
        self.testContacts = generateTestArContacts()
        self.generator.makeVcardFromContacts(self.testContacts)
        super().setUp()

    def test_isArabicText(self):
        arabicContact = generateSimpleSingleArContact(5)
        englishContact = generateSimpleSingleEnContact(5)

        self.assertTrue(isProbablyArabicText(arabicContact.username))
        self.assertTrue(isProbablyArabicText(arabicContact.cell))
        self.assertTrue(isProbablyArabicText(arabicContact.org))
        self.assertFalse(isProbablyArabicText(englishContact.org))
        self.assertFalse(isProbablyArabicText(englishContact.cell))
        self.assertFalse(isProbablyArabicText(englishContact.username))

    def test_encode_decode_arabic(self):
        arabicContact = generateSimpleSingleArContact(1)

        self.assertEqual(arabicContact.username,
                         decodeVcardArabic(encodeVcardArabic(arabicContact.username)))
        self.assertEqual(arabicContact.cell,
                         decodeVcardArabic(encodeVcardArabic(arabicContact.cell)))
        self.assertEqual(arabicContact.org,
                         decodeVcardArabic(encodeVcardArabic(arabicContact.org)))

        if __name__ == '__main__':
            unittest.main()
