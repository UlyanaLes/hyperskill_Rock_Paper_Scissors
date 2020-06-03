f_name = "test.txt"
infile = open(f_name, 'w')
my_string = "A string to be written to a file!"

# what to do with the file and the string
print(my_string, file=infile, end='')

infile.close()
