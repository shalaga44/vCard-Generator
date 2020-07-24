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
        hasEnFirstName = False
        for line in getLinesIn(self.generator.getVcardText()):
            if isNewContact(self, line):
                self.contact = self.testContacts.pop(0)
            if isLineFirstName(self, line):
                if getVcardLineContent(line) == self.contact.username:
                    hasEnFirstName = True
                else:
                    raise Exception("First Name Didn't Match")
        self.assertTrue(hasEnFirstName)

    def test_has_en_Name(self):
        hasName = False
        for line in getLinesIn(self.generator.getVcardText()):
            if isNewContact(self, line):
                self.contact = self.testContacts.pop(0)
            if isLineName(self, line):
                if getVcardLineContent(line) == getContactNameParsed(self.contact):
                    hasName = True
                else:
                    raise Exception("Contact Name Didn't Match")

        self.assertTrue(hasName)


class NameTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.generator = VCARDGenerator()
        self.testContacts = []
        super().setUp()

    def test_has_en_Name1(self):
        self.contact = generateSimpleSingleEnContact(1)
        self.generator.makeVcardFromContacts([self.contact])
        hasName = False
        for line in getLinesIn(self.generator.getVcardText()):
            if isLineName(self, line):
                generatorName = getVcardLineContent(line)
                if generatorName == getContactNameParsed(self.contact):
                    hasName = True
                else:
                    raise Exception("Contact Name Didn't Match")

        self.assertTrue(hasName)

    def test_has_en_2_Name(self):
        self.contact = generateSimpleSingleEnContact(2)
        self.generator.makeVcardFromContacts([self.contact])
        hasName = False
        for line in getLinesIn(self.generator.getVcardText()):
            if isLineName(self, line):
                generatorName = getVcardLineContent(line)
                if generatorName == getContactNameParsed(self.contact):
                    hasName = True
                else:
                    raise Exception("Contact Name Didn't Match")

        self.assertTrue(hasName)

    def test_has_en_3_Name(self):
        self.contact = generateSimpleSingleEnContact(3)
        self.generator.makeVcardFromContacts([self.contact])
        hasName = False
        for line in getLinesIn(self.generator.getVcardText()):
            if isLineName(self, line):
                generatorName = getVcardLineContent(line)
                if generatorName == getContactNameParsed(self.contact):
                    hasName = True
                else:
                    raise Exception("Contact Name Didn't Match")

        self.assertTrue(hasName)


if __name__ == '__main__':
    unittest.main()
