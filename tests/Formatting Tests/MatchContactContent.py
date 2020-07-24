import unittest

from ContactsGenerators.EnglishContactGenerator import generateSimpleSingleEnContact
from Generator import VCARDGenerator
from Utils.Strings import *
from Utils.functions import *


class GeneralTestCases(unittest.TestCase):

    def setUp(self) -> None:
        self.generator = VCARDGenerator()
        self.testContacts = []
        self.testContacts = generateTestEnContact()
        self.generator.makeVcardFromContacts(self.testContacts)

        super().setUp()

    def test_has_cell(self):
        for line in getLinesIn(self.generator.getVcardText()):
            if isNewContact(self, line):
                self.contact = self.testContacts.pop()
            if isCellLine(self, line):
                self.assertEqual(self.generator.vcardCellQ + ":" + self.contact.cell,line)

    def test_has_org(self):
        for line in getLinesIn(self.generator.getVcardText()):
            if isNewContact(self, line):
                self.contact = self.testContacts.pop()
            if isOrgLine(self, line):
                self.assertEqual(self.generator.vcardOrgQ + ":" + self.contact.org, line)


if __name__ == '__main__':
    unittest.main()
