import sqlite3 as sql
from copy import deepcopy
import json

import sql_gui

class Base_data:
    def __init__(self,file):
        """ Подключение к/создание базы данных """
        print(f'{file}/project.db')
        self.con = sql.connect(f'{file}project.db')
        self.cur = self.con.cursor()
        self.cashe_project = {}
        self.cashe_addElements = []
        self.directories = {'itso': ('type','count'), 'dangerous': ('type_element', 'name_element'), 
                            'rooms': ('file','count'), 'other_elements': ('file','shape'), 
                            'added_elements':('file','id_list','name', 'type')}

    def get_info_tables(self):
        """ Получение информации о уже существующих таблицах"""
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        self.tables = list(map(lambda x: x[0], self.cur.fetchall()))
        self.info_tables = {}
        for table in self.tables:
            self.cur.execute(f"SELECT * FROM {table}")
            self.info_tables[table] = self.cur.fetchall()
        return self.info_tables

    def check_db(self):
        """ Проверка несоответствий новых и старых данных """
        _ = self.get_info_tables()
        self.incorrects = {}
        for table in self.cashe_project.keys():
            try:
                original = self.info_tables[table]
            except KeyError: # в случае отсутствия таблицы
                self.cur.execute(f"CREATE TABLE {table}{self.directories[table]}")
                self.info_tables[table] = {}
                original = self.info_tables[table]

            if original != self.cashe_project[table] and self.cashe_project[table] != {}: # в случае несоответствия таблиц
                self.incorrects[table] = [self.info_tables[table], self.cashe_project[table]]
        del_list = []

        for key in del_list:
            del self.incorrects[key]
        self.visual_changes()

    def preparing_sameData(self):
        """ Метод - костыль до тех пор пока не настрою единый уровень вложения в словари"""
        print(self.incorrects)
        keys = self.incorrects.keys()
        for key in keys:
            data = self.incorrects[key]
            for index_table, values in enumerate(data): 

                    if key == 'rooms' and index_table == 1:
                        for floor, rooms in values.items():
                            self.incorrects[key][1][floor] = len(rooms)
                    try:
                        if type(values[0]) is not dict:
                            d = {}
                            for key_List, val_List in values:
                            
                                try:
                                    d[key_List].append(val_List)
                                except:
                                    d[key_List] = eval(val_List)
                            self.incorrects[key][index_table] = deepcopy(d)
                            continue
                    except: pass
                    try:
                        self.incorrects[key][index_table] = values[0]
                    except:
                        self.incorrects[key][index_table] = values
                    if key == 'dangerous' and index_table == 1:
                        self.incorrects['dangerous'][1] = self.incorrects['dangerous'][1]['all_table']
                        d = {}
                        for key, value in self.incorrects['dangerous'][1]:
                            try:
                                d[key[:3]].append([key, value])
                            except:
                                d[key[:3]] = [[key,value]]
                        self.incorrects['dangerous'] = self.incorrects['dangerous'][0], deepcopy(d)

    def visual_changes(self):
        """ визуализация изменений таблиц """
        self.preparing_sameData()
        self.data = sql_gui.create_window(self.incorrects)

    def update(self):
        """ Обновление данных таблиц путём примитивного удаления всех значений и вставки новых"""
        self.data['added_elements'] = self.cashe_addElements
        for key in self.data.keys():
            if key == 'itso':
                if self.data[key] != {}:
                    self.cur.execute(f"DELETE FROM 'itso'")
                    values = self.data[key]
                    for type, counts in values.items():
                        self.cur.execute(f"INSERT INTO {key} {(self.directories[key])} VALUES (?,?)", (type,json.dumps(counts)))

            elif key == 'rooms':
                if self.data[key] != {}:
                    self.cur.execute(f"DELETE FROM 'rooms'")
                    values = self.data[key]

                    for name_file, counts in values.items():
                        self.cur.execute(f"INSERT INTO {key} {(self.directories[key])} VALUES (?,?)", (name_file, json.dumps(counts)))

            elif key == 'dangerous':
                if self.data[key] != {}:
                    self.cur.execute(f"DELETE FROM 'dangerous'")
                    values = self.data[key]

                    for type_num, value in values.items():
                        if type_num!= 'all_table':
                            self.cur.execute(f"INSERT INTO {key} {(self.directories[key])} VALUES(?,?)", (type_num,str(value)))

            elif key == 'added_elements':
                values = self.data[key]
                if 'added_elements' not in self.info_tables:
                    self.cur.execute(f"CREATE TABLE 'added_elements' {self.directories[key]}")

                for info in values:
                    self.cur.execute(f"INSERT INTO {key} {(self.directories[key])} VALUES {info}")
            else: pass

        self.con.commit()

    def cashe(self,key,*value):
        """ Кэширование всех данных для бд"""
        if key == 'itso':
            value = value[0][0]
        elif key == 'dangedous':
            value = value[0][0][0]
        elif key == 'rooms':
            value = value[0]
        elif key == 'added_elements':
            self.cashe_addElements.append(value)
        self.cashe_project[key] = deepcopy(value)
    
    def close(self):
        """ Фиксация и закрытие соединения """
        self.con.commit()
        self.con.close()