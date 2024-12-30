word = input("Input the word that you want to be buterflied: ")
letters = list(word)

flipped_word = letters[::-1]
for x in flipped_word:
    letters.append(x)
    
word = ''.join(letters)
print(word)
