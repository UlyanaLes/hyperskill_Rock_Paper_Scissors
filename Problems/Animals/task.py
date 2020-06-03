# read animals.txt
# and write animals_new.txt
infile = open('animals.txt', 'r', encoding='utf-8')
outfile = open('animals_new.txt', 'w', encoding='utf-8')

for line in infile:
    outfile.write(line.strip() + ' ')

infile.close()
outfile.close()
