class BinarySearch:

    def search(self, words, target):

        low = 0
        high = len(words) - 1

        while low <= high:

            mid = (low + high) // 2

            if words[mid] > target:
                high = mid - 1

            elif words[mid] < target:
                low = mid + 1

            else:
                return mid

        return -1

n = int(input("Enter the number of words in the dictionary: "))
words = [input(f"Enter word {index + 1}: ") for index in range(n)]
target = input("Enter word to search: ")
result = BinarySearch().search(words, target)

if result != -1:
    print(target ,"found at position", result + 1)
else:
    print(target, "not found")