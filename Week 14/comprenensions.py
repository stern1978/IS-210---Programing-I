
#LIST
numbers = []
for number in xrange(100):
    numbers.append(number)

numbers = [num for num in xrange(100)]
#above are the same


#DICT
mydict = {
    'one' : 'banana',
    'two' : 'banana',
    'three' : 'banana',
    'grapefruit' : 'Yuck'
}

mydict2 = {
    'one' : 'Yes',
    'two' : 'No',
    'three' : 'Maybe',
    'grapefruit' : 'Make is so'
}

multiplier = 3
print {mydict2[key]: value for key, value in mydict.iteritems()}
