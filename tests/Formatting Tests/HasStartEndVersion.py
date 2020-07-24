import unittest

from ContactsGenerators.EnglishContactGenerator import generateSimpleSingleEnContact
from Generator import VCARDGenerator
from Utils.Strings import *


class GeneralTestCases(unittest.TestCase):

    def setUp(self) -> None:
        self.generator = VCARDGenerator()
        self.generateTestEnContact()
        super().setUp()

    def test_not_contacts(self):
        self.generator.makeVcardFromContacts([])
        try:
            self.generator.getVcardText()
            self.assertFalse(True)
        except Exception as E:
            self.assertEqual(E.args[0], "No Contacts")

    def test_has_started_and_ended(self):
        isEnded = True
        for line in self.generator.getVcardText().split(newLine):
            if line == self.generator.vcardStartQ and isEnded:
                isEnded = False
            elif line == self.generator.vcardEndQ and not isEnded:
                isEnded = True
        self.assertTrue(isEnded)

    def test_has_version(self):
        hasVersion = False
        for line in self.generator.getVcardText().split(newLine):
            if line == self.generator.vcardVersionQ:
                hasVersion = True
        self.assertTrue(hasVersion)

    def generateTestEnContact(self):
        for nameLength in range(5):
            contact = generateSimpleSingleEnContact(nameLength)
        self.generator.makeVcardFromContacts([contact])
        self.assertFalse(emptyString, self.generator.getVcardText())


if __name__ == '__main__':
    unittest.main()
