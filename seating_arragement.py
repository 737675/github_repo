#Seating Arragement Problem

from itertools import permutations

def seating(guests):
    for p in permutations(guests):
     if all(p[i-1] in guests[p[i]] and p[(i+1)%len(p)]in guests[p[i]] for i in range(len(p))):
            return p
    return "No valid arrangement."

guests = {
    'Alice': ['Bob', 'Carol'],
    'Bob': ['Alice', 'David'],
    'Carol': ['Alice', 'David'],
    'David': ['Bob', 'Carol']
}

print(seating(guests))
