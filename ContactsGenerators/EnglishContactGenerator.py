from DataTypes.contact import Contact


def generateSimpleSingleEnContact(length):
    username = "Mohamed Moawia El-Bashir Mohamed Bla0 Bla1 Bla3 Bla4 Bla5"
    username = ' '.join(name
                        for idx, name in enumerate(username.split())
                        if idx < length)
    cell = "0923545640"
    org = "Laggers"
    return Contact(username, cell, org)
