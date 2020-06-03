# write your code here
with open('salary.txt', 'r') as infile, \
        open('salary_year.txt', 'w', encoding='utf-8') as outfile:
    for line in infile:
        print(int(line) * 12, file=outfile)
