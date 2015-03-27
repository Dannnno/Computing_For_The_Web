from __future__ import print_function

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {1: 'a', 2: 'b', 3:'c'}

def test_mutability(some_iterable):
	if some_iterable != my_tuple:
		some_iterable[2] = 'd'
	else:
		some_iterable += (5, 3, 6)
	return some_iterable

print("Original values:", my_list, my_tuple, my_dict)
print("Mutated list:", test_mutability(my_list), my_list)
print("Unmutated tuple:", test_mutability(my_tuple), my_tuple)
print("Mutated dictionary:", test_mutability(my_dict), my_dict)
