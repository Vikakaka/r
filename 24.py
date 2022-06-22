import itertools
import matplotlib

nested_lists = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

print("work № 1.1")
iter_l = itertools.chain.from_iterable(nested_lists)
for item in iter_l:
    print(item)
print("--------------------------------------------------------")
print("work № 1.2")
comp_list = [y for x in nested_lists for y in x]
print(comp_list)
print("--------------------------------------------------------")
print("work № 2")
gen_l = matplotlib.cbook.flatten(nested_lists)
print(list(gen_l))
