# read test.txt
infile = open('test.txt', 'r', encoding='utf-8')
for line in infile:
    print(line[0])
infile.close()
