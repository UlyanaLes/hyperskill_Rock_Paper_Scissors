# create the planets.txt
outfile = open('planets.txt', 'w', encoding='utf-8')
my_list = ['Mercury\n',
           'Venus\n',
           'Earth\n',
           'Mars\n',
           'Jupiter\n',
           'Saturn\n',
           'Uranus\n',
           'Neptune\n']

outfile.writelines(my_list)
outfile.close()
