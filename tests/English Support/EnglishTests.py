import unittest

from Generator import VCARDGenerator
from Utils.functions import *
from ContactsGenerators.EnglishContactGenerator import *


class GeneralTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = VCARDGenerator()
        self.testContacts = generateTestEnContact()
        self.generator.makeVcardFromContacts(self.testContacts)
        super().setUp()

    def test_has_en_first_name(self):
        for line in getLinesIn(self.generator.getVcardText()):
            if isNewContact(self, line):
                self.contact = self.testContacts.pop(0)
            if isLineFirstName(self, line):
                self.assertEqual(self.contact.username, getVcardLineContent(line))

    def test_has_en_Name(self):
        for line in getLinesIn(self.generator.getVcardText()):
            if isNewContact(self, line):
                self.contact = self.testContacts.pop(0)
            if isLineName(self, line):
                self.assertEqual(getContactParsedText(self.contact.username), getVcardLineContent(line))


class NameTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = VCARDGenerator()
        self.testContacts = []
        super().setUp()

    def test_has_en_1_Name(self):
        self.contact = generateSimpleSingleEnContact(1)
        self.generator.makeVcardFromContacts([self.contact])
        for line in getLinesIn(self.generator.getVcardText()):
            if isLineName(self, line):
                generatorName = getVcardLineContent(line)
                self.assertEqual(getContactParsedText(self.contact.username), generatorName)

    def test_has_en_2_Name(self):
        self.contact = generateSimpleSingleEnContact(2)
        self.generator.makeVcardFromContacts([self.contact])
        for line in getLinesIn(self.generator.getVcardText()):
            if isLineName(self, line):
                generatorName = getVcardLineContent(line)
                self.assertEqual(getContactParsedText(self.contact.username), generatorName)


def test_has_en_3_Name(self):
    self.contact = generateSimpleSingleEnContact(3)
    self.generator.makeVcardFromContacts([self.contact])
    for line in getLinesIn(self.generator.getVcardText()):
        if isLineName(self, line):
            generatorName = getVcardLineContent(line)
            self.assertEqual(getContactParsedText(self.contact.username), generatorName)


if __name__ == '__main__':
    unittest.main()
