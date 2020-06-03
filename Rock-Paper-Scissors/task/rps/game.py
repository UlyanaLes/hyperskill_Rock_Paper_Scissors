from random import choice

infile = open('rating.txt', 'r')
my_users = {}
for line in infile:
    my_list = line.strip().split()
    my_users[my_list[0]] = int(my_list[1])

# print(my_users)
# Write your code here
my_dict = {}
new_list = []
my_set = set()

name = input('Enter your name: ')
# print(name)
print('Hello,', name)

cst_list = input().strip().split(',')
if cst_list == ['']:
    my_dict = {'scissors': 'rock', 'rock': 'paper', 'paper': 'scissors'}
    my_set = ('scissors', 'rock', 'paper')
else:
    my_set = (cst_list)
    for i in range(len(cst_list)):
        if i < len(cst_list):
            new_list = cst_list[i + 1:]
        new_list.extend(cst_list[:i])
        my_dict[cst_list[i]] = new_list[:len(cst_list) // 2]
        # print(new_list)

print("Okay, let's start")
# print(my_dict)
# print(my_set)
user_choose = input()
comp_choose = choice(my_set)

while user_choose != '!exit':
    if user_choose == '!rating':
        print('Your rating:', my_users.get(name, 0))
    elif user_choose in my_set:
        if user_choose == comp_choose:
            print(f'There is a draw ({comp_choose})')
            my_users[name] = my_users.get(name, 0) + 50
        elif comp_choose in my_dict[user_choose]:
            print(f'Sorry, but computer chose {comp_choose}')
        else:
            print(f'Well done. Computer chose {comp_choose} and failed')
            my_users[name] = my_users.get(name, 0) + 100
    else:
        print('Invalid input')
    user_choose = input()
    comp_choose = choice(my_set)
else:
    print('Bye!')

infile.close()
