# read sums.txt
infile = open('sums.txt', 'r', encoding='utf-8')
for line in infile:
    print(sum(map(int, line.strip().split())))

infile.close()
