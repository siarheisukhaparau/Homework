a = {"d": 1, "a": 2, "c": 3, "z": 4, "f": 5}
b = list(a.keys())
b.sort()
c = {}
for i in b:
    c[i] = a[i]
# for i in b:
#     for j in a.keys():
#         if i == j:
#             c[i] = a.get(i)
print(c)
