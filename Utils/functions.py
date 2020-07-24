from datetime import date

from ContactsGenerators.EnglishContactGenerator import *
from ContactsGenerators.ArabicContactGenerator import *
from Utils.Strings import *


def isNewContact(self, line):
    if line[:len(self.generator.vcardStartQ)] == self.generator.vcardStartQ:
        return True
    else:
        return False


def isCellLine(self, line):
    if line[:len(self.generator.vcardCellQ)] == self.generator.vcardCellQ:
        return True
    else:
        return False


def isLineName(self, line):
    if line[:len(self.generator.vcardNameQ)] == self.generator.vcardNameQ:
        return True
    else:
        return False


def isLineFirstName(self, line):
    if line[:len(self.generator.vcardFirstNameQ)] == self.generator.vcardFirstNameQ:
        return True
    else:
        return False


def isProbablyArabicText(text):
    isArabic = False
    for s in text:
        # The range 0600 - 06E0 is the code point range of Arabic characters and symbols
        # http://www.tamasoft.co.jp/en/general-info/unicode.html
        if 1536 <= ord(s) <= 1760:
            return True
    return isArabic


def encodeVcardArabic(text: str) -> str:
    enText = text.encode("UTF-8")
    hexTextList = str(enText).split("\\x")[1:-1] + [str(enText).split("\\x")[-1][:-1]]
    joinedHexText = "=" + "=".join(hexTextList).replace(" ", "=20")
    return joinedHexText


def decodeVcardArabic(text: str) -> str:
    hexTextList = text.split("=")[1:]
    joinedHexText = " ".join(hexTextList)
    enText = bytes.fromhex(joinedHexText)
    return enText.decode("UTF-8")


def supString(s1, s2):
    return s1.replace(s2, emptyString)


def encodedArabicList(textList: str) -> list:
    encodedList = []
    for text in textList:
        encodedList.append(encodeVcardArabic(text))
    return encodedList


def encodedArabicFirstName(contact: Contact) -> str:
    nameList = contact.username.split()
    encodedNameList = encodedArabicList(nameList)
    out = "=20".join(encodedNameList)
    return VcardCharsetQ + out


def getSupportedTextOf(text: str):
    if isProbablyArabicText(text):
        return VcardCharsetQ + encodeVcardArabic(text)
    else:
        return text


def isOrgLine(self, line):
    if line[:len(self.generator.vcardOrgQ)] == self.generator.vcardOrgQ:
        return True
    else:
        return False


def generateTestArContacts(count=7):
    testContacts = []
    for nameLength in range(1, count, 1):
        contact = generateSimpleSingleArContact(nameLength)
        testContacts.append(contact)
    return testContacts


def generateTestEnContact(count=7):
    testContacts = []
    for nameLength in range(1, count, 1):
        contact = generateSimpleSingleEnContact(nameLength)
        testContacts.append(contact)
    return testContacts


def getLinesIn(text) -> str:
    for line in text.split(newLine):
        yield line


def getContactParsedText(text: str) -> str:
    nameList = text.split()
    if len(nameList) == 1:
        return f";{nameList[0]};;;"
    elif len(nameList) == 2:
        return f"{nameList[1]};{nameList[0]};;;"
    elif len(nameList) == 3:
        return f"{nameList[2]};{nameList[0]};{nameList[1]};;"
    else:
        return f"{nameList[-1]}; {' '.join(nameList[0:-2])};{nameList[-2]};;"


def getVcardLineContent(line) -> str:
    return ":".join(line.split(":")[1:])


def isUserSpecifiedFileName(filename) -> bool:
    if filename is not None:
        return True
    return False


def getFormattedUserFileName(filename) -> str:
    if filename.endswith(".vcf"):
        filename = f'{filename[:-4]}-{date.today()}.vcf'
    else:
        filename += f'-{date.today()}.vcf'
    return filename
