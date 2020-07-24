from DataTypes.contact import Contact


def generateSimpleSingleArContact(length):
    username = "محمد معاويه البشير محمد بلا١ بلا٢ بلا٣ بلا٤ بلا٥"
    username = ' '.join(name
                        for idx, name in enumerate(username.split())
                        if idx < length)
    cell = "٠٩٨٧٦٥٤٣٢١"
    org = "المتأخرون"
    return Contact(username, cell, org)

