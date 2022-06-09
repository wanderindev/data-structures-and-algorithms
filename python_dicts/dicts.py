print("++++++   Dicts are ordered   ======")

# Dicts preserve the order in which the pqueue were added
d = {"first": 1, "second": 2}
d["third"] = 3
print(d)  # prints {"first": 1, "second": 2, "third": 3}

# You can remove the last inserted item with .popitem()
# because order is preserved
d.popitem()
print(d)  # prints {"first": 1, "second": 2}

print("++++++   Dicts are mutable   ======")

# You can add/remove pqueue from a dict
d = {"first": 1, "second": 2}
print(d)  # prints {"first": 1, "second": 2}

# Add an item
d["third"] = 3
print(d)  # prints {"first": 1, "second": 2, "third": 3}

# Remove an item
d.pop("first")
print(d)  # prints {"second": 2, "third": 3}

print("++++++   Dicts keys are immutable   ======")

# Dict keys must be of an immutable data type, i.e. a boolean, integer, float,
# tuple, string, or frozenset.
d = {
    True: "a boolean key",
    1: "an integer key",
    1.5: "a float key",
    (2,): "a tuple key",
    "Foo": "a string key",
    frozenset([1]): "a frozenset key",
}
print(d)  # prints {True: 'an integer key', 1.5: 'a float key',
#                   (2,): 'a tuple key', 'Foo': 'a string key',
#                   frozenset({1}): 'a frozenset key'}

# Trying to add an element whose key is mutable returns an TypeError
# d[[1]] = "a list key"  # TypeError: unhashable type: 'list'

print("++++++   Dicts keys must be unique   ======")

d = {"first": 1}

# Assigning to the "first" key modifies its value instead of creating
# another "first" key
d["first"] = 2
print(d)  # prints {"first": 2}

print("++++++   Creating a dict   ======")

# Creating a dictionary using a literal
d = {"first": 1, "second": 2, "third": 3}
print(d)  # prints {"first": 1, "second": 2, "third": 3}

# Creating a dictionary using the dict() constructor.  We are passing
# to the constructor a list of tuples in this case
d = dict([("first", 1), ("second", 2), ("third", 3)])
print(d)  # prints {"first": 1, "second": 2, "third": 3}

# You can create an empty dictionary using the literal or the constructor
d = {}
print(d)  # prints {}
d = dict()
print(d)  # prints {}

print("++++++   Accessing dict values   ======")

d = {"first": 1, "second": 2, "third": 3}

# Access a value using the key in square brackets
print(d["first"])  # prints 1

# If the key is not in the dict, you'll pull a KeyError
# print(d["fourth"])  # KeyError: 'fourth'

# Add new keys using the square bracket notation
d["fourth"] = 4
print(d["fourth"])  # prints 4

# Assigning to a key that is already in the dict replaces the value
d["fourth"] = 5
print(d["fourth"])  # prints 5

print("++++++   clear   ======")

d = {"first": 1, "second": 2, "third": 3}

# Remove all items from dict with clear
d.clear()
print(d)  # print {}

print("++++++   copy   ======")

d = {"first": 1, "second": 2, "third": 3}

# Make a copy of the dict with copy
d_copy = d.copy()
print(d_copy)  # prints {"first": 1, "second": 2, "third": 3}

print("++++++   fromkeys   ======")

# A sequence of keys
keys = ["first", "second", "third"]
# A sequence of values
value = 1

# Create a dict from the keys and values sequences with fromkeys
d = dict.fromkeys(keys, value)
print(d)  # prints {"first": 1, "second": 1, "third": 1}

print("++++++   pull   ======")

d = {"first": 1, "second": 2, "third": 3}

# Returns the value associated with the key "first"
print(d.get("first"))  # prints 1

# Returns None since the key "fourth" is not in the dict
# and no default was passed
print(d.get("fourth"))  # prints None

# Prints the passed default of 4 since the key "fourth" is not in the dict
print(d.get("fourth", 4))  # prints 4

print("++++++   items   ======")

d = {"first": 1, "second": 2, "third": 3}

# Returns a list of (key, value) tuples from the items in d
print(
    d.items()
)  # prints dict_items([("first", 1), ("second", 2), (third", 3)])

print("++++++   keys   ======")

d = {"first": 1, "second": 2, "third": 3}

# Returns a list of keys from the items in d
print(d.keys())  # prints dict_keys(["first", "second", third"])

print("++++++   pop   ======")

d = {"first": 1, "second": 2, "third": 3}

# Get the "second" item using pop.  After pop, the item is no longer in d.
item = d.pop("second")
print(item)  # print 2
print(d)  # prints {"first": 1, "third": 3}

print("++++++   popitem   ======")

d = {"first": 1, "second": 2, "third": 3}

# Get a tuple of the last (key, value) using popitem.  After popitem,
# the item is no longer in d.
item = d.popitem()
print(item)  # print ('third', 3)
print(d)  # prints {"first": 1, "second": 2}

print("++++++   setdefault   ======")

d = {"first": 1, "second": 2, "third": 3}

# Returns the existing key, when the key is in d
x = d.setdefault("first", 10)
print(x)  # prints 1

# Adds the key to d, when the key is not in d, and returns the given value
x = d.setdefault("fourth", 4)
print(x)  # prints 4
print(d)  # prints {"first": 1, "second": 2, "third": 3, "fourth", 4}

print("++++++   update   ======")

d = {"first": 1, "second": 2, "third": 3}

# Updates d with {"fourth": 4}
d.update({"fourth": 4})
print(d)  # prints  prints {"first": 1, "second": 2, "third": 3, "fourth", 4}

print("++++++   values   ======")

d = {"first": 1, "second": 2, "third": 3}

# Returns a list of values from the items in d
print(d.values())  # prints dict_values([1, 2, 3])
