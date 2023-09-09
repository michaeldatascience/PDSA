# A function that returns the length of the value:
cars1 = ['Ford', 'Mitsubishi', 'BMW', 'VW']

def myFunc1(e):
    return len(e)

cars1.sort(key=myFunc1)
cars1.sort(key=myFunc1,reverse=True)
print(cars1)

#Sort a list of dictionaries based on the "year" value of the dictionaries:
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

def myFunc(e):
    return(e['year'])

cars.sort(key=myFunc)
print(cars)
