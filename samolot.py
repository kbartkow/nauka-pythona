#zadanie z samolotem
samolot = {'name' : 'boeing' ,
           'przebieg' : 1000,
           'type' : 'pasazerski' }
# in python3 samolot.items()
for key, value in samolot.iteritems() :
    print("{0}:{1}".format(key, value))

#
for key in samolot:
    print("{0}:{1}".format(key, samolot[key]))
