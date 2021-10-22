# Ask the user for a string and print out whether this string is a palindrome or not.

sentence = input("Please type a sentence: ")

word = str(sentence)
reverse = sentence[:: -1]

if reverse == sentence:
    print("Your sentence is a Palindrome")
    print(sentence, "Palindrome check is", True)
else:
    print("Your sentence is not a Palindrome")
    print(reverse, "is not the same as \n", sentence)

# Another example for this will be
# def reverse(word):
# x = ''
# for i in range(len(word)):
#    x += word[len(word)-1-i]
#   return x

# word = input('give me a word:\n')
# x = reverse(word)
# if x == word:
#    print('This is a Palindrome')
# else:
# print('This is NOT a Palindrome')


