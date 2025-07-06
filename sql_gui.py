import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import math
import itertools
from copy import deepcopy
# from typing import overload


class DB_Win_UI(QMainWindow):
    """ ЮИ интерфейс """
    def __init__(self):
        super().__init__()
        self.resize(QSize(750,680))
        self.centralwidget = QWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.old_table = QTableWidget(self.centralwidget)
        self.old_table.setGeometry(0,0,375,500)
        self.new_table = QTableWidget(self.centralwidget)
        self.new_table.setGeometry(375,0,375,500)
        self.accept_button = QPushButton(self.centralwidget, text = 'Завершить')
        self.accept_button.setGeometry(QRect(620, 600, 100,40))



class DB_Win(DB_Win_UI):
    """ Логический раздел визуализации """
    def __init__(self,data):
        super().__init__()
        self.table = None
        self.data = data
        self.stat_tables = [self.old_table, self.new_table]
        self.old_table.setRowCount(50)
        self.old_table.setColumnCount(50)
        self.new_table.setRowCount(50)
        self.new_table.setColumnCount(50)
        self.buttons_inTables = {} # словарь внутритабличных кнопок
        self.buttons_tables = {} # хранение кнопок для смены таблиц
        self.cashe = {} # хранит решения о сохранении/удалении строки
        self.accept_button.clicked.connect(self.accept_table)
        for column, tables in enumerate(itertools.batched(data.keys(),2)):
            for row,table in enumerate(tables):
                button = QPushButton(self.centralwidget, text=table)
                button.setGeometry(QRect(50 + 150*column,520 + 50*row,140,40))
                button.clicked.connect(self.change_Table)
                self.buttons_tables[button] = table

        self.buttons = {}
        self.show_ITSO()

    def update_tables(self):
        """ Обнуление таблиц для повторного размещения """
        self.convert_ButtonText()
        try:
            self.buttons_inTables[self.table] = deepcopy(self.buttons)
        except TypeError:
            self.update_tables()

        for table in self.stat_tables:
            for row,column in itertools.product(range(50),range(50)):
                table.setItem(row,column,None)
                try:
                    table.setCellWidget(row,0, None)
                except:
                    print('Возникло исключение в обнулении виджетов таблицы')

        self.old_table.setRowCount(50)
        self.old_table.setColumnCount(50)
        self.new_table.setRowCount(50)
        self.new_table.setColumnCount(50)

    def convert_ButtonText(self):
        """ Конвертация из текстового статуса кнопки в кнопку и обратно """
        keys_of_buttons = list(self.buttons.keys()).copy()
        try:
            if type(keys_of_buttons[0]) is str:
                for button in keys_of_buttons:

                    self.buttons[QPushButton(text=button[:-2:])] = self.buttons[button]
                    del self.buttons[button]
            else:
                for i, button in enumerate(keys_of_buttons):
                    if len(str(i)) == 2:
                        text = str(i)
                    else:
                        text = '0'+str(i)
                    self.buttons[button.text()+text] = self.buttons[button]
                    del self.buttons[button]
        except IndexError:
            pass

    def change_Table(self):
        """ Переключение между таблицами по нажатию на соответствующую кнопку"""
        button = self.sender()
        self.update_tables()
        if self.buttons_tables[button] == 'itso':
            self.show_ITSO()
        elif self.buttons_tables[button] == 'dangerous':
            self.show_Dangerous()
        elif self.buttons_tables[button] == 'rooms':
            self.show_Rooms()
        elif self.buttons_tables[button] == 'other_table':
            self.show_OtherTable()

    def unpack_db(self,value):
        """ Преобразование данных в корректный вид """
        list_val = []
        symbols = []
        for sym in value:
            if sym != ',' and sym != ' ' and sym != '[' and sym != ']':
                symbols.append(sym)
            elif len(symbols) != 0:
                list_val.append(''.join(symbols))
                symbols = []
        return list_val


    def show_ITSO(self):
        """ Отображение таблицы итсо"""
        for type_in_data, values in self.data.items(): # выбрали ключ
            if type_in_data == 'itso':
                self.table = type_in_data
                try:
                    self.buttons = deepcopy(self.buttons_inTables[self.table])
                except:
                    self.buttons = {}
                for i, table in enumerate(values): # раскрыли ключ, получили типы таблиц олд или нью
                        if type(table) is not dict:
                            if len(table) == 0: continue
                            else:
                                d = {}
                                for key,values_on_list in table:
                                    d[key] = self.unpack_db(values_on_list)
                                table = deepcopy(d)
                        for row, (type_el,element) in enumerate(list(table.items())):
                            if len(list(self.buttons.keys())) <= row: 
                                self.buttons[QPushButton(text='Исключить')] = type_el,element
                            else:
                                if row == 0:
                                    self.convert_ButtonText()
                            button = list(self.buttons.keys())[row]
                            try:
                                self.stat_tables[1].setCellWidget(row,0,button)
                            except:
                                self.convert_ButtonText()
                                button = list(self.buttons.keys())[row]
                                self.stat_tables[1].setCellWidget(row,0,button)

                            self.stat_tables[i].setItem(row,1,QTableWidgetItem(type_el))
                            for column, count in enumerate(element[:-1:]):
                                self.stat_tables[i].setItem(row,column+2,QTableWidgetItem(str(count)))

        for button in self.buttons.keys():
            button.clicked.connect(self.exclude_include)

    def show_Dangerous(self):
        """ Отображение таблицы ПОУ и КЭО """
        for type_in_data, values in self.data.items(): # выбрали ключ
            if type_in_data == 'dangerous':
                self.table = type_in_data
                try:
                    self.buttons = deepcopy(self.buttons_inTables[self.table])
                except:
                    self.buttons = {}
                for i, table in enumerate(values): # раскрыли ключ, получили типы таблиц олд или нью
                        if not type(table) is dict:
                            if len(table) == 0:
                                continue

                        try:
                            for row, element in enumerate(list(table.values())[0]):
                                # ужасный костыль, пофиксить
                                if len(list(self.buttons.keys())) <= row:
                                    self.buttons[QPushButton(text='Исключить')] = element[0][:4:] + str(element[1]),element
                                else:
                                    if type(list(self.buttons.keys())[0]) is str:
                                        self.convert_ButtonText()
                                # if i == 1:
                                button = list(self.buttons.keys())[row]
                                self.stat_tables[i].setCellWidget(row,0,button)
                                self.stat_tables[i].setItem(row,1,QTableWidgetItem(element[0][:4:] + str(element[1])))
                                self.stat_tables[i].setItem(row,2,QTableWidgetItem(element[0][4::]))
                                
                        except Exception as e:
                            print('Беды при отображении ПОУ и КЭО db:', e)
                            
        for button in self.buttons.keys():
            button.clicked.connect(self.exclude_include)

    def show_Rooms(self):
        """ Отображение таблицы Экспликации помещений, точнее кол-ва помещений"""
        for type_in_data, values in self.data.items(): # выбрали ключ
            if type_in_data == 'rooms':
                self.table = type_in_data
                try:
                    self.buttons = deepcopy(self.buttons_inTables[self.table])
                except:
                    self.buttons = {}
                for i, table in enumerate(values): # раскрыли ключ, получили типы таблиц олд или нью
                    if type(table) is not dict:
                            if len(table) == 0: continue
                            else:
                                pass
                    for row, element in enumerate(table.items()):
                        # ужасный костыль, пофиксить
                        if len(list(self.buttons.keys())) <= row:
                            self.buttons[QPushButton(text='Исключить')] = element[0], element[1]
                        else:
                            if type(list(self.buttons.keys())[row]) == str:
                                self.convert_ButtonText()
                        button = list(self.buttons.keys())[row]
                        self.stat_tables[1].setCellWidget(row,0,button)
                        self.stat_tables[i].setItem(row,1,QTableWidgetItem(str(element[0])))
                        self.stat_tables[i].setItem(row,2,QTableWidgetItem(str(element[1])))

        for button in self.buttons.keys():
            button.clicked.connect(self.exclude_include)

    def show_OtherTable(self):
        pass

    def get_data(self):
        """ Возврат данных после выборки пользователем"""
        return self.newdata

    def get_OldValue(self, values):
        """ Получение старого значения из таблицы бд в случае если пользователь предпочёл оставить данное значение"""
        # Метод является некорректным, обдумать его правку
        for key, value in self.data.items():
            if key == value[0]:
                print('get_OldValue вроде лишний ход событий. Обдумай')
                return  value[1]
        else:
            return  []
                

    def upload_all_tables(self):
        """ Обновление всех таблиц 
        Создано для того, если пользователь не просмотрел все таблицы.
        Метод предупреждает потерю не просмотренных таблиц"""
        for button in self.buttons_tables.keys():
            button.click()

    def accept_table(self):
        """ Определение новых данных после выборки пользователем"""
        self.upload_all_tables()
        self.update_tables()
        self.newdata = {}
        for key, row in self.buttons_inTables.items():
            table = {}
            for status, values in row.items():
                if status[:-2] == 'Включить':
                    old_value = self.get_OldValue(values)
                    if list(old_value) != []:
                        table[values[0]] = old_value
                elif status[:-2] == 'Исключить':
                    table[values[0]] = values[1]
            self.newdata[key] = deepcopy(table)
        
        self.close()

    def exclude_include(self):
        """ Меняет статус кнопок внутри таблиц """
        # А может это не баг?
        button = self.sender()
        if button.text() == 'Исключить':
            button.setText('Включить')
        else:
            button.setText('Исключить')



def create_window(data):
    application = QApplication(sys.argv)
    main_win = DB_Win(data)
    main_win.show()
    application.exec_()
    return main_win.get_data()
