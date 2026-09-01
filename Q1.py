n = int(input("Enter the number of words in the dictionary: "))
#words = [input(f"Enter word {index + 1}: ") for index in range(n)]
words = []
for index in range(n):
    #word = input(f"Enter word {index + 1}: ")
    #word = input("Enter word {}: ".format(index + 1))
    #word = input("Enter word " + str(index + 1) + ": ")
    print("Word" ,index + 1, ":", end = " ")
    word = input()
    words.append(word)

letter_counts = {}
for word in words:
    for character in word.lower():
        if character.isalpha():
            #letter_counts[character] = letter_counts.get(character, 0) + 1
            if character in letter_counts:
                letter_counts[character] += 1
            else:
                letter_counts[character] = 1


print("\nLetter counts:")
print(letter_counts)