
a = [[1, 2], [3, 4]]
b = [[1, 2], [3, 4]]
c = a                  # same reference
d = a.copy()           # shallow copy (outer list copied, inner lists shared)

print(a == b)  # True  (same values)
print(a is b)  # False (different objects)

print(a is c)  # True  (same reference)

print(a == d)  # True  (values still same)
print(a is d)  # False (new outer object)

# But inner lists are shared in shallow copy:
print(a[0] is d[0])  # True

# Modifying inner list affects both:
a[0][0] = 99
print(a)  # [[99, 2], [3, 4]]
print(d)  # [[99, 2], [3, 4]]  (changed too!)

# To avoid this, use deep copy:
import copy
e = copy.deepcopy(a)

print(a == e)  # True
print(a is e)  # False
print(a[0] is e[0])  # False (fully independent)