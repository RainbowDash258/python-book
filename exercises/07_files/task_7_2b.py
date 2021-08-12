# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from sys import argv

filename = argv[1]
file_write = argv[2]

ignore = ["duplex", "alias", "configuration"]
ignore.append("!")

with open(filename) as f, open(file_write, 'w') as w:
    for line in f:
        for ign in ignore:
            if not ign in line:
               continue
            else:
                break
        else:
            w.write(line.rstrip() + '\n')
