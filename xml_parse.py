import xml.etree.ElementTree as ET
import zipfile
from tkinter.filedialog import askopenfilenames

"""
Это программа - сканер отдельных объектов для дальнейшего корректного размещения граф. объектов
Методика работы вместе с этой программой:
1. Нужен файл в котором уже существует мастер этого элемента(желательно это должен быть корневой файл который никогда не видел ничего кроме образца холста
2. Удаляем все элементы с файла(я надеюсь вы сделали копию))
3. Добавляем элемент который в дальнейшем должен добавляться нашей программой
4. запускаем софт
***ГОТОВО***

Напоминание о способе создания новых фигур:
1. Создаем новое наименование элемента(в свойствах объекта указываем наше имя, желательно что бы поле образец было пустым)
2. Закидываем в набор нашу фигуру и внутри набора так же меняем наименование объекта
***ГОТОВО***
"""

dic = {}
numbers = [str(num) for num in range(10)]
files = askopenfilenames() 
stroka = ''
print(files)
print("Запущено")
with open('new_shape.txt', 'w') as text:
            
    def stick_of_tree(child, pre):
        global text
        text.write(f'\n        #вход в дерево {pre}\n')
        text.write(f'        generation{pre} = generation{pre-1}\n')
        for line in child:
            text.write(f'\n        generation{pre} = generation{pre}.add_child(')
            text.write(f"'{line.tag[53::]}'")
            text.write(', ' + str(line.attrib) + ')')
            if line.tag[53::] != 'Cell':
                stick_of_tree(line, pre+1)


    for file in files:
        with zipfile.ZipFile(file, 'r') as zf:
            # Извлечение содержимого XML файла
            with zf.open('visio/pages/page1.xml') as f:
                tree = ET.parse(f)
                root = tree.getroot()[0][0]
                child = None
                grandson = None
                pragrandson = None
                pragrandson_v2 = None
                pragrandson_v3 = None
                text.write('self.lost_id += 1\n')
                text.write('        el = Append_Element(' + '"' + str(root.tag[53::]) + '"' + ', ')
                text.write(str(root.attrib) + ')')
                text.write('\n        self.adress.append(el)')
                text.write('\n        #вход в дерево 1\n')
                for line in root:
                    text.write('\n        generation1 = el.add_child(')
                    text.write(f"'{line.tag[53::]}'")
                    text.write(', ' + str(line.attrib) + ')')
                    if line.tag[53::] != 'Cell':
                        stick_of_tree(line,2)
                text.write('\n\n')
