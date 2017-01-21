# Ближайшие бары

Данный скрипт предоставляет данные о барах Москвы, основываясь на данных с портала data.mos.ru
В данный момент скрипт выводит:
* самый большой бар;
* самый маленький бар;
* самый близкий бар (текущие gps-координаты ввести с клавиатуры).


# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python
Enter json file path: moscowBars.json
Biggest bar is :Спорт бар «Красная машина»
Smallest bar is :БАР. СОКИ
Enter your latitude: 34.7
Enter your longitude: 55.1
Nearest bar is : Staropramen
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)


