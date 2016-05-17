cities=["mumbai","new york","paris"]
countries=["India","usa","france"]

z = zip(cities,countries)

print(z)

for a in z:
    print a
#prints ('mumbai', 'India')
#       ('new york', 'usa')
#       ('paris', 'france')


d={city:country for city, country in zip(cities,countries)}

#prints {'paris': 'france', 'new york': 'usa', 'mumbai': 'India'}

print d





