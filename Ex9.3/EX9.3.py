dictionary_email = dict()
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('Error, file does not exist.')
    exit()

for line in fhand:
    line = line.rstrip()
    line = line.strip()
    if not 'From' in line:
        continue

    line = line.split()
    if len(line) <= 2:
        continue
    email = line[1]
    email = email.split()

    for mail in email:
        if mail not in dictionary_email:
            dictionary_email[mail] = 1
        else:
            dictionary_email[mail] += 1
print(dictionary_email)






