print("========  List are ordered  ========")

# Lists are ordered.  The lists below are not the same, even though they
# contain the same pqueue.  The difference is in the order of the pqueue.

print([1, 2, 3] == [3, 2, 1])  # prints False

print("========  List contain arbitrary objects  ========")

# Lists can contain any arbitrary object, i.e. integers, floats, boolean,
# strings, dictionaries, and other lists.
l = [1, 3.14, True, "hello!", {"name": "John"}, [1, 2, 3]]
for e in l:
    print(type(e))

# prints
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'str'>
# <class 'dict'>
# <class 'list'>

print("========  List can have duplicate pqueue ========")

# Lists can have duplicated pqueue.
print([1, 2, 1])  # prints [1, 2, 1]

print("========  List are mutable  ========")

# Lists are mutable
l = [1, 2, 3]
print(l)  # prints [1, 2, 3]
l.append(4)
print(l)  # prints [1, 2, 3, 4]

print("========  List are dynamic  ========")

# Lists are dynamic
l = [1, 2, 3]
print(len(l))  # prints 3
l.append(4)
print(len(l))  # prints 4
l.pop()
print(len(l))  # prints 3

print("========  Creating list with []  ========")

# Creating a list with square brackets.
l = [1, 2, 3]
print(l)  # prints [1, 2, 3]

print("========  Creating list with list()  ========")

# Creating a list with the list() constructor
l = list((1, 2, 3))
print(l)  # prints [1, 2, 3]

print("========  Accessing an element by index  ========")

# Accessing an element by its index.
l = [1, 2, 3]
print(l[0])  # prints 1

print("========  List slicing ========")

# List slicing
# my_list = [start : end : step]

print("========  Slicing with implied step  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

# Returns a list from index=0 to index=(2-1) with step=1
new_list = original_list[0:2]
print(new_list)  # prints ["a", "b"]

print("========  Slicing with specified step  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

# Returns a list from index=1 to index=(6-1) with step=2
new_list = original_list[1:6:2]
print(new_list)  # prints ["b", "d", "f"]

print("========  Slicing with negative step  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

# Returns a list from index=6 to index=(1+1) with step=-1
new_list = original_list[5:1:-1]
print(new_list)  # prints ["f", "e", "d", "c"]

print("========  Slicing from the beginning of the list  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

# If the start index is not specified, the list is sliced from index 0.
# The example below returns a list from index=0 to index=(6-1)
new_list = original_list[0:6]
print(new_list)  # prints ["a", "b", "c", "d", "e", "f"]

print("========  Slicing to the end of the list  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

# If the end index is not specified, the list is sliced all the way to the end.
# The example below returns a list from index=1 to the end of the list
new_list = original_list[1:]
print(new_list)  # prints ["b", "c", "d", "e", "f", "g"]

print("========  Slicing with negative indexes  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

# If using negative indexes, the slicing starts from the end of the list.
# The example below returns a list from the beginning to the second
# to last element
new_list = original_list[:-1]
print(new_list)  # prints ["a", "b", "c", "d", "e", "f"]

# The example below returns a list with the last element.
new_list = original_list[-1:]
print(new_list)  # prints ["g"]

print("========  list.append(x)  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

original_list.append("h")
print(original_list)  # prints  ["a", "b", "c", "d", "e", "f", "g", "h"]

print("========  list.extend(iterable)  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

original_list.extend(["h", "i"])
print(original_list)  # prints  ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

print("========  list.insert(i, x)  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

original_list.insert(6, "h")
print(original_list)  # prints  ["a", "b", "c", "d", "e", "f", "h", "g"]

print("========  list.remove(x)  ========")

original_list = ["a", "b", "a", "c", "a", "d", "a"]

original_list.remove("a")
print(original_list)  # prints ["b", "a", "c", "a", "d", "a"]

# original_list.remove("h")  # returns ValueError: list.remove(x): x not in list

print("========  list.pop(i)  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

elem_b = original_list.pop(1)
print(elem_b)  # prints b
print(original_list)  # prints ["a", "c", "d", "e", "f", "g"]

elem_g = original_list.pop()
print(elem_g)  # prints g
print(original_list)  # prints ["a", "c", "d", "e", "f"]

print("========  list.clear()  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

original_list.clear()
print(original_list)  # prints []

print("========  list.index(x, start, end)  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

print(original_list.index("e"))  # prints 4

print("========  list.count(x)  ========")

original_list = ["a", "b", "a", "c", "a", "d", "a"]

print(original_list.count("a"))  # prints 4

print("========  list.sort()  ========")

original_list = ["a", "d", "a", "g", "c", "b", "f", "e"]

original_list.sort()
print(original_list)  # ["a", "a", "b", "c", "d", "e", "f", "g"]

print("========  list.reverse()  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

original_list.reverse()
print(original_list)  # prints ["g", "f", "e", "d", "c", "b", "a"]

print("========  list.copy()  ========")

original_list = ["a", "b", "c", "d", "e", "f", "g"]

new_list = original_list.copy()
new_list.reverse()
print(original_list == new_list)  # prints False

print("========  List Comprehensions  ========")

print("========  List of squares iterative ========")

list_of_numbers = list(range(11))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_squares = []
for num in list_of_numbers:
    list_of_squares.append(num**2)
print(list_of_squares)  # prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("========  List of squares comprehension ========")

list_of_numbers = list(range(11))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_squares = [num**2 for num in list_of_numbers]
print(list_of_squares)  # prints [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("========  List of evens iterative ========")

list_of_numbers = list(range(11))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_evens = []
for num in list_of_numbers:
    if num % 2 == 0:
        list_of_evens.append(num)
print(list_of_evens)  # prints [0, 2, 4, 6, 8, 10]

print("========  List of evens comprehension ========")

list_of_numbers = list(range(11))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_of_evens = [num for num in list_of_numbers if num % 2 == 0]
print(list_of_evens)  # prints [0, 2, 4, 6, 8, 10]
