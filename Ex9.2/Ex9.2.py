counts = dict()
text = open('mbox-short.txt')
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
    print(counts)



