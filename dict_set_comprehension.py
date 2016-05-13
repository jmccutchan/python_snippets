#using list comprehensions instead of map and filter methods

chile_ranks = {'ghost':1,'habanero':2,'cayenne':3}

#dictionary comprehension to map the ranking of the pepper according to heat
rank_dict = {rank: name for name, rank in chile_ranks.items()}

#comprehension with sets
chile_len_set = {len(name) for name in chile_ranks.keys()}

print(rank_dict)
print(chile_len_set)

