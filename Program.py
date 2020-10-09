import re

f = open('steam_description_data.csv', encoding='utf-8')
characters = 0
spaces = 0
punctuation = 0
words = 0
sentences = 0
for line in f:
    characters += len(line)
    spaces += line.count(' ')
    for i in '.,!?\"\';:-()':
        punctuation += line.count(i)
    words += len(re.findall(r"(\w+'\w+)|(\w+-\w+'\w+)|(\w+-\w+'\w)|\w+", line))
    sentences += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", line))
print('Общее количество символов:', characters)
print('Количество символов без пробелов:', characters - spaces)
print('Количество символов без знаков препинания:', characters - punctuation)
print('Количество слов:', words)
print('Количество предложений:', sentences)
f.close()
