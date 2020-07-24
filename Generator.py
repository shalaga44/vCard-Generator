from Utils.functions import *


def isEmpty(text):
    if text.strip == emptyString:
        return True
    return False


class VCARDGenerator:
    def __init__(self):
        self.contacts = []
        self.generalContact = Contact()
        self.isContactsChanged = False
        self.text = emptyString
        self.vcardStartQ = "BEGIN:VCARD"
        self.vcardVersionQ = "VERSION:2.1"
        self.vcardNameQ = "N:"
        self.vcardFirstNameQ = "FN:"
        self.vcardCellQ = "TEL;CELL:"
        self.vcardEmailQ = "EMAIL;HOME:"
        self.vcardOrgQ = "ORG:"
        self.vcardTitleQ = "TITLE:"
        self.vcardNoteQ = "NOTE:"
        self.vcardEndQ = "END:VCARD"

    def makeVcardFromContacts(self, contacts):
        if type(contacts) is not list:
            raise Exception("Contacts Must Be List")
        self.isContactsChanged = True
        self.contacts = contacts

    def getVcardText(self):
        if len(self.contacts) == 0:
            raise Exception("No Contacts")
        if self.isContactsChanged:
            self.generate()
        return self.text

    def generate(self):
        self.isContactsChanged = False
        for contact in self.contacts:
            temText = emptyString

            temText += self.vcardStartQ + newLine
            temText += self.vcardVersionQ + newLine
            temText += self.vcardNameQ + self.getOrdered(contact.username) + newLine
            temText += self.vcardFirstNameQ + contact.username + newLine
            temText += self.vcardCellQ + contact.cell + newLine
            temText += self.vcardEmailQ + contact.email + newLine
            temText += self.vcardOrgQ + contact.org + newLine
            temText += self.vcardTitleQ + contact.title + newLine
            temText += self.vcardNoteQ + contact.note + newLine
            temText += self.vcardEndQ + newLine

            self.text += self.cleanedVcardText(temText)

    def export_as_vcf_file(self, filename: str = None):
        if isUserSpecifiedFileName(filename):
            filename = getFormattedUserFileName(filename)
        else:
            filename = self.getFormattedDefaultFileName()
        self.proceed_export_vcf(filename)

    @staticmethod
    def cleanedVcardText(text):
        cleanText = emptyString
        for t in getLinesIn(text.strip()):
            if t.split(":")[1] != '':
                cleanText += t + newLine
        return cleanText

    @staticmethod
    def getOrdered(text) -> str:
        outSetText = text.split()
        outText = emptyString
        if len(outSetText) == 1:
            outText = f";{outSetText[0]};;;"
        if len(outSetText) == 2:
            outText = f"{outSetText[1]};{outSetText[0]};;;"
        elif len(outSetText) == 3:
            outText = f"{outSetText[2]};{outSetText[0]};{outSetText[1]};;"
        elif len(outSetText) > 3:
            last = outSetText.pop()
            beforeLast = outSetText.pop()
            outText = f"{last}; {' '.join(outSetText)};{beforeLast};;"
        return outText

    def getFormattedDefaultFileName(self) -> str:
        if self.hasOrganization():
            filename = f"{self.getContactsOrganization()}-{date.today()}.vcf"
        else:
            filename = f"Contacts-{date.today()}.vcf"
        return filename

    def hasOrganization(self) -> bool:
        for contact in self.contacts:
            if not isEmpty(contact.org):
                self.generalContact.org = contact.org
                return True
        return False

    def getContactsOrganization(self) -> str:
        return self.generalContact.org

    def proceed_export_vcf(self, filename):
        with open(filename, ioWriteFlag) as f:
            for line in getLinesIn(self.getVcardText()):
                f.write(line + newLine)
