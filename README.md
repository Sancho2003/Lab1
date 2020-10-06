# Лабораторная работа  №1

### Задание
Написать программу на Python, которая:

* Подсчитывает общее количество символов в файле
* Подсчитывает общее количесто символов без пробелов
* Подсчитывает количество символов без знаков препинания
* Подсчитывает количество слов в файле
* Подсчитывает количество предложений
* Результат подсчета должен быть выведен в консоль

**Вход программы:**
Файл `steam_description_data.csv`

**Выход программы:**
Информация о количестве символов, слов и предложений

> **_ВАЖНО:_**
Результат оформить в виде репозитория на гитхабе.

### Решение
* Используем модуль `csv` для чтения файла
* Объединяем полученный список в строку
* При помощи `len()`, `count()` и `split()` определяем длину строки, считаем символы, пробелы, знаки препинания, слова
* При помощи модуля `re` определяем предложения посредством паттерна `([A-Z][^\.!?]*[\.!?])`, ищем совпадения при помощи `re.findall()` и с помощью `len()` считаем их количество



