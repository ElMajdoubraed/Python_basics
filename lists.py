#list
l = [1, 2, 3, 4, 5]
print(l)
print(type(l))

print(l[0])
print(l[1])
print(l[-1])
print(l[0:3])

# Concatenate list
l2 = [6, 7, 8, 9, 10]

print(l+l2)

# lists in list
l3 = [
    l,
    l2,
    [11, 12 ,13]
]
print(l3)
print(l3[1])
print(l3[0][0])

# functions add , remove , insert,  count(item), find item , len(), sort() pop(), index

l.append(0)
print(l)
print(len(l))
l.remove(2)
print(l)
print(len(l))
l2.insert(0,15)
print(l2)

print(l2.count(15))


print(8 in l)

l2.sort()
print(l)

# tuple

fruits = ('apple', 'banana', 'orange')
print(type(fruits))
print(len(fruits))
#Once a tuple is created, you cannot change its values


# set

set1 = {'raed', 'elmajdoub', 21}
print(set1)
print(type(set1))
set1.add('Python')
print(set1)
#Sets are unordered.  Set elements are unique. Duplicate elements are not allowed.
#A set itself may be modified, but the elements contained in the set must be of an immutable type