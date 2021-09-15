b = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
s = set()
for dictionary in b:
    for val in dictionary.values():
        s.add(val)
print(s)
