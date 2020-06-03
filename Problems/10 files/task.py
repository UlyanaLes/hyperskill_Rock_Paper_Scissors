# write your code here
n_files = 10
files = []

for i in range(n_files):
    file_name = 'file' + str(i + 1) + '.txt'
    # print(file_name)
    with open(file_name, 'w', encoding='utf-8') as f:
        files.append(f)
        f.write(str(i + 1))
