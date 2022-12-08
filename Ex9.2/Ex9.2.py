counts = dict()
fname = input('Enter a file name: ')
try:
    text = open(fname)
except:
    print(f'File cannot be open: {fname}')
    exit()
for line in text:
    line = line.rstrip()
    line = line.split()
    if not 'From' in line:
        continue

    cword = line[2]
    cword = cword.split()
    for word in cword:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
my_list = list(counts.items())
print(my_list)
