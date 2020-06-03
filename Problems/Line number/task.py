# read sample.txt and print the number of lines
infile = open('sample.txt', 'r', encoding='utf-8')
print(len(infile.readlines()))
infile.close()
