import os
files = os.listdir('files_task3')# получаем список файлов из целевого каталогоа
len_dict = {}# словарь, где ключ - имя файла, значение - количество строк
for file in files:
    file = f'files_task3/{file}'
    with open(file,'rt', encoding="utf-8" ) as f:
        len_dict[file] = (sum(1 for line in f))
len_list_sorted = sorted(len_dict, key = lambda k:len_dict[k])#список для прохода
                                                              #по очереди записи файлов

with open('res.txt','a', encoding="utf-8" ) as f:  #открываем целевой файл на запись
    for k in len_list_sorted:
        with open(k,'rt',encoding="utf-8" ) as x:  #в цикле проходим по изначальным файлам в заданном порядке 
            X = x.read()
            f.write(f"{k}"+'\n')                   #перед записью непосредственно файла добавляем имя источника
            f.write(f"{len_dict[k]}"+'\n')         #также добаляем количество строк этого файла
            f.write(X+'\n')                        #записываем непосредственно сам файл



     
