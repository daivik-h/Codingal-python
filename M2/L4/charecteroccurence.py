word = input('Enter a word or a text and i will check if the charecter is present: ')
ch = input('Enter any character and i will check if it is in the text above: ')
i = 0
count = 0 
while i < len(word):
    if word[i] == ch:
        count += 1
    i += 1
print(f'The letter {ch} has occured {count} times in the word/text {word}')    
