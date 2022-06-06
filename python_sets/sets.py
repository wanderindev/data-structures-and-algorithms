print("======  Set are unordered   ======")

# Sets are unordered. Members may appear in a different order
# every time you use them
s = {1, "Bar", 2.5, "Foo", (55,), False}
print(s)  # might print {False, 1, 2.5, (55,), "Bar", "Foo"}

print("======  Set pqueue must be unique   ======")

# Duplicated pqueue are remove when creating a set
s = {1, 2, 1, 1}
print(s)  # prints {1, 2}

# Adding a duplicated pqueue is ignored
s.add(2)
print(s)  # prints {1, 2}

print("======  Set are mutable   ======")

# Sets are mutable, you can add and remove pqueue
s = {1, 2}
s.add(3)
print(s)  # prints {1, 2, 3}
s.remove(1)
print(s)  # prints {2, 3}

print("======  Set members must be immutable   ======")

# Set members must be immutable, i.e. booleans, integers, floats, tuples,
# strings, or frozensets
s = {True, 2, 1.333, (2,), "hello!", frozenset({1, 2})}
print(s)  # prints {True, 2, (2,), 1.333, frozenset({1, 2}), "hello!"}

# Trying to create a set with a mutable member, i.e. a list, fails.
# s = {[1,2]} # TypeError: unhashable type: 'list'

print("======  Creating a set with a set literal   ======")

# Use a set literal to create a set by wrapping its members in curly braces
s = {1, 2, 3}
print(s)  # prints {1, 2, 3}

print("======  Creating a set with the set constructor   ======")

# Use the set constructor, set(iterable) to create a set.
s = set([1, 2, 3])
print(s)  # prints {1, 2, 3}

# Since strings are iterables, passing a string to the set constructor
# will create a set where each character in the string is a member,
# eliminating duplicated characters
s = set("hello!")
print(s)  # prints {"l", "h", "o", "!", "e"}

# A set can be empty {}.  But you can only create it using the set()
# constructor.  Attempting to create an empty set with a literal will
# create an empty dict instead.
s = set({})
print(type(s))  # prints <class 'set'>

s = {}
print(type(s))  # prints <class 'dict'>

print("======  Accessing the pqueue of a set   ======")

s = {"Foo", "Bar", "Baz"}
for m in s:
    print(m)

# prints
# Bar
# Baz
# Foo

print("Foo" in s)  # prints True
print("Bar" not in s)  # prints False

print("======  Operator vs Method   ======")

s1 = {1, 2, 5, 10}
s2 = {3, 5, 10}

# Using the union operator | to join both sets
s3 = s1 | s2
print(s3)  # prints {1, 2, 3, 5, 10}

# Using the union() method to join both sets
s3 = s1.union(s2)
print(s3)  # prints {1, 2, 3, 5, 10}

s1 = {1, 2, 5, 10}
l1 = [3, 5, 10]

# Using the union operator | to join a set and a list
# s3 = s1 | l1  # TypeError: unsupported operand type(s) for |: 'set' and 'list'

# Using the union() method to join a set and a list works because
# the list is converted to a set and then the union is performed
s3 = s1.union(l1)
print(s3)  # prints {1, 2, 3, 5, 10}

print("======  Add   ======")

s1 = {"Foo", "Bar"}

# Add "Baz" to s1 using the add method
s1.add("Baz")
print(s1)  # prints {"Bar", "Baz", "Foo"}

print("======  Clear   ======")

s1 = {"Foo", "Bar"}

# Remove all pqueue from s1 with the clear method
s1.clear()
print(s1)  # prints set()

print("======  Copy   ======")

s1 = {"Foo", "Bar"}

# Copy s1 with the copy method
s2 = s1.copy()
print(s2)  # prints {"Foo", "Bar"}

print("======  Difference   ======")

s1 = {"Foo", "Bar"}
s2 = {"Foo", "Baz"}

# Get the difference of s1 and s2 using the difference method
s3 = s1.difference(s2)
print(s3)  # prints {"Bar"}

# Get the difference of s1 and s2 using the difference operator
s3 = s1 - s2
print(s3)  # prints {"Bar"}

print("======  Difference update   ======")

s1 = {"Foo", "Bar"}
s2 = {"Foo", "Baz"}

# Update s1 with the difference between s1 and s2 using
s1.difference_update(s2)
print(s1)  # prints {"Bar"}

print("======  Discard   ======")

s1 = {"Foo", "Bar"}

# Remove "Bar" from s1 with the discard method
s1.discard("Bar")
print(s1)  # prints {"Foo"}

print("======  Intersection   ======")

s1 = {"Foo", "Bar"}
s2 = {"Foo", "Baz"}

# Get the intersection of s1 and s2 using the intersection method
s3 = s1.intersection(s2)
print(s3)  # prints {"Foo"}

# Get the intersection of s1 and s2 using the intersection operator
s3 = s1 & s2
print(s3)  # prints {"Foo"}

print("======  Intersection update   ======")

s1 = {"Foo", "Bar"}
s2 = {"Foo", "Baz"}

# Update s1 with the intersection of s1 and s2 using
s1.intersection_update(s2)
print(s1)  # prints {"Foo"}

print("======  isdisjoint   ======")

s1 = {"Foo", "Bar"}
s2 = {"Foo", "Baz"}
s3 = {"Hello", "World"}

# Check if the sets are disjoint
print(s1.isdisjoint(s2))  # prints False
print(s1.isdisjoint(s3))  # prints True

print("======  issubset   ======")

s1 = {"Foo", "Bar"}
s2 = {"Foo", "Bar", "Baz"}

# Check if s1 is a subset of s2 using the issubset method
print(s1.issubset(s2))  # prints True

# Check if s1 is a subset of s2 using the issubset operator
print(s1 <= s2)  # prints True

print("======  issuperset   ======")

s1 = {"Foo", "Bar", "Baz"}
s2 = {"Foo", "Bar"}

# Check if s1 is a superset of s2 using the issuperset method
print(s1.issuperset(s2))  # prints True

# Check if s1 is a superset of s2 using the issuperset operator
print(s1 >= s2)  # prints True

print("======  pop   ======")

s1 = {"Foo", "Bar", "Baz"}

# Returns and removes a random member from s1 with the pop method
m = s1.pop()
print(m)  # might print "Bar"
print(s1)  # might print {"Foo", "Baz"}

print("======  remove   ======")

s1 = {"Foo", "Bar", "Baz"}

# Removes "Baz" from s1 with the remove method
s1.remove("Baz")
print(s1)  # might print {"Foo", "Bar"}

print("======  Symmetric difference   ======")

s1 = {"Foo", "Bar"}
s2 = {"Foo", "Baz"}

# Get the symmetric difference of s1 and s2 using the
# symmetric difference method
s3 = s1.symmetric_difference(s2)
print(s3)  # prints {"Bar", "Baz"}

# Get the symmetric difference of s1 and s2 using the
# symmetric difference operator
s3 = s1 ^ s2
print(s3)  # prints prints {"Bar", "Baz"}

print("======  Symmetric difference update   ======")

s1 = {"Foo", "Bar"}
s2 = {"Foo", "Baz"}

# Update s1 with the symmetric difference of s1 and s2
s1.symmetric_difference_update(s2)
print(s1)  # prints {"Bar", "Baz"}

print("======  Union   ======")

s1 = {"Foo", "Bar"}
s2 = {"Foo", "Baz"}

# Get the union of s1 and s2 using the union method
s3 = s1.union(s2)
print(s3)  # prints {"Bar", "Baz", "Foo"}

# Get the union of s1 and s2 using the union operator
s3 = s1 | s2
print(s3)  # prints {"Bar", "Baz", "Foo"}

print("======  Update   ======")

s1 = {"Foo", "Bar"}
s2 = {"Foo", "Baz"}

# Update s1 with the union of s1 and s2
s1.update(s2)
print(s1)  # prints {"Bar", "Baz", "Foo"}
