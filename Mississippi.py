word = "mississippi"
count = 0

res = {}
for keys in word:
    res[keys] = res.get(keys,0)+1
print(res)

