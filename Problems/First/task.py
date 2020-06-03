# read test_file.txt
infile = open('test_file.txt', 'r', encoding='utf-16')
print(infile.readline())
infile.close()
