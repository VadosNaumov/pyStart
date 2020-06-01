import random
import re
import os

chars = '+-()*!&$#@^%abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def genpassw():
    password = ''
    lengthpsswrd = random.randrange(12, 20)
    ext = True
    while ext:
        for i in range(int(lengthpsswrd)):
            password += random.choice(chars)
        ext = not is_ok(password)
    return password


def is_ok(text):
    match1 = bool(re.search(r'[()\+\-*!&$#@^%]+', text))
    match2 = bool(re.search(r'[abcdefghijklnopqrstuvwxyz]+', text))
    match3 = bool(re.search(r'[ABCDEFGHIJKLMNOPQRSTUVWXYZ]+', text))
    match4 = bool(re.search(r'[1234567890]+', text))
    match = match1 and match2 and match3 and match4
    return match


def email_gen(list_of_names):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + '@company.io' in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + '@company.io')
    return emails


file = open('tafile.txt', 'r')
filenew = open('interimFile.txt', 'w')
filebad = open('badFile.txt', 'w')
emails_book = []
for line in file:
    firstline = bool(re.search(r'EMAIL.+', line))
    if firstline:
        filenew.write(line.rstrip() + ', PASSWORD\n')
        continue
    phoneavail = bool(re.search(r', [A-Z][a-z]+, [A-Z][a-z]+, \d{7}, [A-Z][a-z]+', line))
    if not phoneavail:
        filebad.write(line)
        continue
    listofnamesbook = line.split(', ')
    listofnamesbook.pop(0)
    listofnamesbook.pop()
    listofnamesbook.pop()
    emails_book.append(listofnamesbook)
    filenew.write(line.rstrip() + ', ' + genpassw() + '\n')

file.close()
filenew.close()
filesec = open('interimFile.txt', 'r')
filesecnew = open('tafile.txt', 'w')
mails = email_gen(emails_book)
i = 0
for line in filesec:
    firstline = bool(re.search(r'EMAIL.+', line))
    if firstline:
        filesecnew.write(line)
        continue
    mai = mails[i]
    i += 1
    filesecnew.write(mai + line)

filesec.close()

if os.path.isfile('interimFile.txt'):
    os.remove('interimFile.txt')
else:
    print("Error: %s file not found" % filesec)

filesecnew.close()