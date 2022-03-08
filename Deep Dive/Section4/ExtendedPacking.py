
# extended unpacking on the left

l = [1, 2, 3, 4]
a, b, *c = l
print(a, b, c)

# slicing to get same result
el1 = l[0]
el2 = l[1]
el3 = l[2:]

print(el1, el2, el3)


# extended unpacking on the right

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l_join = [*l1, *l2]

# more extended unpacking
s1 = 'abc'
s2 = 'def'
[*s1, *s2]

print(s1, s2)


# standard for loop through set (no ordering, so result will vary)
s = {10, -99, 3, 'd'}

for c in s:
    print(c)

# unpacking with a set (prob not useful, b/c no ordering)
a, b, c, d = s
print(a, b, c, d)

s1 = {1, 2, 3}
s2 = {4, 5, 6}
s_join = {*s1, *s2}

print(s_join)

# unpack 2 dictionaries, remember only keys are unpacked in dictionaries unless you use **

d1 = {'key1': 1, 'key2': 2}
d2 = {'key3': 3, 'key4': 4}
d3 = {*d1, *d2}                         # only keys return
print(d3)

d4 = {**d1, **d2}                       # now, keys AND values are unpacked
print(d4)

