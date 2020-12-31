def show_magicians(magicians):
    for m in magicians:
        print(m)

def make_great(magicians):
    great_magicians = []
    while magicians:
        mage = magicians.pop()
        great_magicians.append("Great " + mage)
    return great_magicians

magicians = ['Seimei', 'Ablafia', 'Agrippa', 'Ashmole']
great_magicians = make_great(magicians[:])
show_magicians(magicians)
show_magicians(great_magicians)
