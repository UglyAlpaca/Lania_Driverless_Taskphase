class SelectionSort:

    def sort(self, words):

        l = len(words)
        for i in range(l - 1):

            min_index = i
            for j in range(i + 1, l):

                if words[j] < words[min_index]:
                    min_index = j

            #words[i], words[min_index] = words[min_index], words[i]
            temp = words[i]
            words[i] = words[min_index]
            words[min_index] = temp

        return words

n = int(input("Enter the number of words in the dictionary: "))
words = [input(f"Enter word {index + 1}: ") for index in range(n)]
obj = SelectionSort()
result = obj.sort(words)
#result = SelectionSort().sort(words)
print("\nSorting the words in alphabetical order using selection sort: ")

for x in result:
    print(x)
