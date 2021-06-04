a = ['a', 'b', 'g']
b = [0, 1, 2, 3, 4, 5]
g = dict(zip(a, b))
f = {'a': 0, 'b': 1, 'h': 5}
unique_dict = {}
for k, v in g.items():
    unique_dict[k] = v
    for key, value in f.items():
        if key not in unique_dict.keys():
            unique_dict[key] = value
print(unique_dict)
