import itertools
import math
from sets import Set

cubes = {}
cube_list = []
"""
def fill_reverse_cube_set(upperbound):
    for i in range(upperbound + 1):
        reverse_cube_set[i**3] = i


def gen_cubes(upperbound):
    return [i**3 for i in range (300,upperbound)]
def tup_to_int(x):
    string = ""
    for e in x:
        string += e
    return int(string)

def is_cube(x):
    return x in reverse_cube_set
"""

#each of the permutations ahs the same minimal permutation
#(i.e. the permuatation gained by sorting the digits in ascending order)!
def find_cube_perm_counts(upperbound) :
    for i in range(300,upperbound):
        cube = i**3
        cube_list.append(cube)
        permutationKey = "".join(sorted(str(cube)))
        if cubes.has_key(permutationKey) :
            cubes[permutationKey].append(cube)
            if len(cubes[permutationKey]) == 5:
                print cubes[permutationKey][0]
                break
        else:
            cubes[permutationKey] = [cube]
#cubes = gen_cubes(100000)
#fill_reverse_cube_set(100000)
#cube_set = Set(cubes)
#cube_set.intersection(Set([1,2,3,4]))

"""for cube in cubes:
    count = 0
    found_perms = []
    for j in Set(itertools.permutations( str(cube) , len( str(cube) ) )):
        if not (j[0] == '0' or j <= cube):
            j = tup_to_int(j)

            if is_cube(j) and j not in found_perms:
                count += 1
                found_perms.append(j)
    if count > 4:
        print cube"""

"""count = 0
cube = 345**3
found_perms = []
for j in itertools.permutations( str(cube) , len( str(cube) ) ):
    if not (j[0] == '0' or j <= cube):
        j = tup_to_int(j)
        if is_cube(j) and j not in found_perms:
            count += 1
            found_perms.append(j)"""


find_cube_perm_counts(1000000)
