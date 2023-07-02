text = input("Enter a string: ").lower()
counts = dict()
#letter = list(text)

for i in text:
    counts[i] = counts.get(i,0) + 1

print(counts)
