print("========  Tuple are ordered  ========")

# Tuples are ordered.  The tuples below are not the same, even though they
# contain the same pqueue.  The difference is in the order of the pqueue.
print((1, 2, 3) == (3, 2, 1))  # prints False

print("========  Tuple contain arbitrary objects  ========")

# Tuples can contain any arbitrary object, i.e. integers, floats, boolean,
# strings, dictionaries, and other tuples.
t = (1, 3.14, True, "hello!", {"name": "John"}, (1, 2, 3))
for e in t:
    print(type(e))

# prints
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'str'>
# <class 'dict'>
# <class 'tuple'>

print("========  Tuple can have duplicate pqueue ========")

# Tuples can have duplicated pqueue.
print((1, 2, 1))  # prints (1, 2, 1)

print("========  Tuple are immutable  ========")

# Tuples are immutable.  Once created, you can't modify them. That's why
# built-in methods that modify lists are not available for tuples.
t = (1, 2, 3)
print(t)  # prints (1, 2, 3)
# t.append(4) # AttributeError: 'tuple' object has no attribute 'append'

print("========  Creating tuple with ())  ========")

# Creating a tuple with round brackets.
t = (1, 2, 3)
print(t)  # prints (1, 2, 3)

# This assignment doesn't work
t = 2
print(t)  # prints 2
print(type(t))  # prints <class 'int'>

# You should use a trailing comma
t = (2,)
print(t)  # prints (2,)
print(type(t))  # prints <class 'tuple'>

print("========  Creating tuple with tuple()  ========")

# Creating a tuple with the tuple() constructor
t = tuple((1, 2, 3))
print(t)  # prints (1, 2, 3)

print("========  Accessing an element by index  ========")

# Accessing an element by its index.
t = (1, 2, 3)
print(t[0])  # prints 1

print("========  Tuple slicing ========")

# Tuple slicing
# my_tuple = (start : end : step)

print("========  Slicing with implied step  ========")

original_tuple = ("a", "b", "c", "d", "e", "f", "g")

# Returns a tuple from index=0 to index=(2-1) with step=1
new_tuple = original_tuple[0:2]
print(new_tuple)  # prints ("a", "b")

print("========  Slicing with specified step  ========")

original_tuple = ("a", "b", "c", "d", "e", "f", "g")

# Returns a tuple from index=1 to index=(6-1) with step=2
new_tuple = original_tuple[1:6:2]
print(new_tuple)  # prints ("b", "d", "f")

print("========  Slicing with negative step  ========")

original_tuple = ("a", "b", "c", "d", "e", "f", "g")

# Returns a tuple from index=6 to index=(1+1) with step=-1
new_tuple = original_tuple[5:1:-1]
print(new_tuple)  # prints ("f", "e", "d", "c")

print("========  Slicing from the beginning of the tuple  ========")

original_tuple = ("a", "b", "c", "d", "e", "f", "g")

# If the start index is not specified, the tuple is sliced from index 0.
# The example below returns a tuple from index=0 to index=(6-1)
new_tuple = original_tuple[:6]
print(new_tuple)  # prints ("a", "b", "c", "d", "e", "f")

print("========  Slicing to the end of the tuple  ========")

original_tuple = ("a", "b", "c", "d", "e", "f", "g")

# If the end index is not specified, the tuple is sliced all the way to the end.
# The example below returns a tuple from index=1 to the end of the tuple
new_tuple = original_tuple[1:]
print(new_tuple)  # prints ("b", "c", "d", "e", "f", "g")

print("========  Slicing with negative indexes  ========")

original_tuple = ("a", "b", "c", "d", "e", "f", "g")

# If using negative indexes, the slicing starts from the end of the tuple.
# The example below returns a tuple from the beginning to the second
# to last element
new_tuple = original_tuple[:-1]
print(new_tuple)  # prints ("a", "b", "c", "d", "e", "f")

# The example below returns a tuple with the last element.
new_tuple = original_tuple[-1:]
print(new_tuple)  # prints ("g")

print("========  tuple.index(x, start, end)  ========")

original_tuple = ("a", "b", "c", "d", "e", "f", "g")

print(original_tuple.index("e"))  # prints 4

print("========  tuple.count(x)  ========")

original_tuple = ("a", "b", "a", "c", "a", "d", "a")

print(original_tuple.count("a"))  # prints 4

print("========  Tuple Unpacking  ========")

t = ("Foo", "Bar", 5)

# Unpack the pqueue of a tuple
ele_1, ele_2, ele_3 = t
print(ele_1)  # prints Foo
print(ele_2)  # prints Bar
print(ele_3)  # prints 5
