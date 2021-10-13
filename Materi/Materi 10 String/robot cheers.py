an_letters = 'aefhilmnorsxAEFHILMNORSX'

word = input('i\'ll cheer for you! enter a word: ')
times = int(input('enthusiasm level (1-10): '))

for char in word:
    if char in an_letters:
        print('give me an ' + char + '! ' + char)
    else:
        print('give me a ' + char + '! ' + char)
print('what does that spell?')
for i in range(times):
    print(word, '!!!')