def BinarySearch(bucket, num):
	low = 0
	high = len(bucket)

	while low < high:
		mid = (low + high) // 2

		if bucket[mid] < num:
			low = mid + 1
		elif bucket[mid] > num:
			high = mid - 1	
		else:
			high = mid

	bucket.insert(low, num)

#question 5
n = int(input("Enter number of values:"))
hash_table = [[] for _ in range(10)]

for i in range(n):
	num = int(input(f"Number {i + 1}:"))
	bucket = hash_table[num % 10]
	BinarySearch(bucket, num)

print(hash_table)
