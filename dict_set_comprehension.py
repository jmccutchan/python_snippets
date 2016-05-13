#using list comprehensions instead of map and filter methods
#as a rule of thumb use no more than two expressions in a list comprehension

chile_ranks = {'ghost':1,'habanero':2,'cayenne':3}

#dictionary comprehension to map the ranking of the pepper according to heat
rank_dict = {rank: name for name, rank in chile_ranks.items()}

#comprehension with sets
chile_len_set = {len(name) for name in chile_ranks.keys()}

a = [1,2,3,4,5,6,7,8,9,10]
b = [x for x in a if x > 4 and x % 2 == 0]

print b
print(rank_dict)
print(chile_len_set)

matrix = [[1,2,3],[4,5,6],[7,8,9]]

filtered = [[x for x in row if x % 3 == 0]
            for row in matrix if sum(row) >= 10]

b = [x**2 for row in matrix for x in row]


print b
print filtered

a2 = list(range(100))
b = [x for x in a2 if x % 2 == 0 if x % 3 == 0]
print b

