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
        hasCell = False
        for line in getLinesIn(self.generator.getVcardText()):
            if isNewContact(self, line):
                self.contact = self.testContacts.pop()
            if isCellLine(self, line):
                if line == self.generator.vcardCellQ + self.contact.cell:
                    hasCell = True
                else:
                    raise Exception("Phone Cell Didn't Match")
        self.assertTrue(hasCell)

    def test_has_org(self):
        hasOrg = False
        for line in getLinesIn(self.generator.getVcardText()):
            if isNewContact(self, line):
                self.contact = self.testContacts.pop()
            if isOrgLine(self, line):
                if line == self.generator.vcardOrgQ + self.contact.org:
                    hasOrg = True
                else:
                    raise Exception("Org Name Didn't Match")

        self.assertTrue(hasOrg)


if __name__ == '__main__':
    unittest.main()
