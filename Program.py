import re
import csv

characters = 0
spaces = 0
punctuation = 0
words = 0
sentences = 0
with open ('steam_description_data.csv', encoding = 'utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        line = ','.join(row)
        characters += len(line)
        spaces += line.count(' ')
        punctuation += line.count('.') + line.count(',') + line.count('?') + line.count('!') + line.count('\'') + line.count('\"') + line.count(';') + line.count(':') + line.count('-') + line.count('(') + line.count(')')
        words += len(line.split()) + len(line.split('.')) + len(line.split(',')) + len(line.split('?')) + len(line.split('!')) + len(line.split('\'')) + len(line.split('\"')) + len(line.split(';')) + len(line.split(':')) + len(line.split('-')) + len(line.split('(')) + len(line.split(')'))
        sentences += len(re.findall(r"([A-Z][^\.!?]*[\.!?])", line))
print('Общее количество символов:', characters)
print('Количество символов без пробелов:', characters - spaces)
print('Количество символов без знаков препинания:', characters - punctuation)
print('Количество слов:', words)
print('Количество предложений:', sentences)
