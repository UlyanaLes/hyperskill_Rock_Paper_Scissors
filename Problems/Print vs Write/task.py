numbers = [1234, 5678, 90]
# save this list in `file_with_list.txt`
outfile = open('file_with_list.txt', 'w', encoding='utf-8')
print(numbers, file=outfile, end='')
outfile.close()
