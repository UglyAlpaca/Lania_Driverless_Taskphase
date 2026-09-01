n = int(input("Enter number of values:"))
hash_table = [[] for _ in range(10)]

for x in range(n):
	num = int(input("Number {}:".format(x + 1)))
	hash_table[num % 10].append(num)

print(hash_table)
