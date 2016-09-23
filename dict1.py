names = raw_input('enter a list of names:').split()
print names
counts = dict()

for name in names:
    counts[name] = counts.get(name,0) + 1

print counts