
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPointF, QSize, QSizeF, QRectF,QRect, QPoint, Qt, QTimer, QThreadPool, QThread, pyqtSlot
from PyQt5.QtGui import QImage, QPainter, QPen, QBrush, QColor, QTransform,QPolygonF,QFont, QKeySequence
from PyQt5.QtWidgets import QDialog, QWidget, QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QLabel, QLineEdit,QVBoxLayout, QMenu, QAction, QCompleter, QGraphicsTextItem, QGraphicsPolygonItem, QAbstractGraphicsShapeItem, QGraphicsItem
from math import sin,cos,radians
from copy import deepcopy
import numpy as np
import json
import itertools
import math
from typing import Dict, List, Tuple, Any
import cv_for_numbers
import xml_structV2
import placement_of_objects
from copy import deepcopy

# QGraphicsItem
class Room(QGraphicsPolygonItem):
    
    """ Является классом графического объекта "Помещение" """
    def __init__(self, polygon, pen=QPen(QColor('black')), brush=QBrush(QColor('yellow'))):
        super().__init__()
        self.active = True
        self.name = None
        self.setPolygon(polygon)
        self.isVisible = True
        self.setPen(pen)
        self.setBrush(brush)
    
    def hide_room(self):
        self.setBrush(QBrush(QColor('black')))
        self.active = False
        self.update()    

    def visible_room(self):
        color = 'green' if self.name is not None else 'yellow'
        self.setBrush(QBrush(QColor(color)))
        self.active = True
        self.update()    
        window.update_all_rooms(append_room=self)
        
    def paint(self, painter, option, widget = ...):
        return super().paint(painter, option, widget)
    
    def change_status(self):
        self.active = not self.active
    
    def get_info(self):
        return self.name, self.active


class QGraphicsScene(QGraphicsScene):
    def __init__(self,*args):
        super().__init__(*args)
        self.cursor = QtGui.QCursor()

    def mouseMoveEvent(self, a0):
        window.mouseMoveEvent(self.cursor.pos())

class StartWindow(QDialog):
    """ Является первым и ключевым виджетом с возможностью выбора запускаемых функций"""
    def __init__(self):
        super().__init__()

        self.resize(400,400)
        self.centralwidget = QtWidgets.QWidget(self)
        self.help_message = QLabel(parent=self, text='Выбор действий:')
        self.help_message.setGeometry(QRect(150,50,90,30))
        self.all_operations = {'Экспликация' : False, 'ИТСО' : False, 'ПОУ и КЭО': False, 'Подсчёт' : False, 'Transfer': False, 'Пути эвакуации': False}
        
        self.flag_Explication = QtWidgets.QCheckBox(self)
        self.flag_Explication.setText('Экспликация помещений, размещение таблицы экспликаций')
        self.flag_Explication.setGeometry(QRect(50,100,350,30))
        self.flag_Explication.stateChanged.connect(lambda: self.registration_way('Экспликация'))
        
        self.flag_ITSO = QtWidgets.QCheckBox(self)
        self.flag_ITSO.setText('Подсчёт, размещение таблицы ИТСО')
        self.flag_ITSO.setGeometry(QRect(50,130,300,30))
        self.flag_ITSO.stateChanged.connect(lambda: self.registration_way('ИТСО'))
        
        self.flag_dangerous = QtWidgets.QCheckBox(self)
        self.flag_dangerous.setText('Работа с ПОУ и КЭО')
        self.flag_dangerous.setGeometry(QRect(50,160,300,30))
        self.flag_dangerous.stateChanged.connect(lambda: self.registration_way('ПОУ и КЭО'))
        
        self.flag_Count_elements = QtWidgets.QCheckBox(self)
        self.flag_Count_elements.setText('Только подсчёт элементов с переводом в Excel')
        self.flag_Count_elements.setGeometry(QRect(50,190,300,30))
        self.flag_Count_elements.stateChanged.connect(lambda: self.registration_way('Подсчёт'))
        
        self.flag_Excel_To_Word = QtWidgets.QCheckBox(self)
        self.flag_Excel_To_Word.setText('Перенос данных из Excel в Word')
        self.flag_Excel_To_Word.setGeometry(QRect(50,220,300,30))
        self.flag_Excel_To_Word.stateChanged.connect(lambda: self.registration_way('Transfer'))
        
        self.flag_evakuation = QtWidgets.QCheckBox(self)
        self.flag_evakuation.setText('Маршрут эвакуации(тест)')
        self.flag_evakuation.setGeometry(QRect(50,250,300,30))
        self.flag_evakuation.stateChanged.connect(lambda: self.registration_way('Пути эвакуации'))
        
        self.button_OK = QtWidgets.QPushButton(text='Продолжить',parent=self)
        self.button_OK.pressed.connect(self.accept_choice)
        self.button_OK.setGeometry(QRect(135,300,150,40))

        self.button_exit = QtWidgets.QPushButton(text="Покинуть программу",parent=self)
        self.button_exit.pressed.connect(self.closeEvent)
        self.button_exit.setGeometry(QRect(135,350,150,40))


    def accept_choice(self):
        global all_operations
        
        all_operations = self.all_operations
        """ Отправляемые параметры """
        self.hide()
        if not all_operations['Подсчёт'] and not all_operations['Transfer']:
            self.scaning_shemes(*xml_structV2.start(self.all_operations))
        else:
            self.parse_info = None

        self.hide()
        self.thread().exit()
        

    def scaning_shemes(self,rooms_charact: Dict, shapes_worklists: Dict, elements_ITSO: Tuple, list_table_POU_KEO: Dict, 
                other_table_elements: List, split_tables: int, sql, files_list: Tuple, pos_tabels: Dict):
        
        global files
        global table_POU_KEO
        
        self.files_list_of_rooms_charact = rooms_charact
        self.shapes_worklists = shapes_worklists
        self.elements_ITSO =elements_ITSO
        self.table_POU_KEO = list_table_POU_KEO
        self.other_table_elements = other_table_elements
        self.split_tables = split_tables
        self.sql = sql
        files = files_list
        table_POU_KEO = list_table_POU_KEO
        self.parse_info = self.files_list_of_rooms_charact, self.shapes_worklists, self.elements_ITSO, self.table_POU_KEO , self.other_table_elements
        


    def registration_way(self,choice):
        """
        Метод изменения статуса выбора пользователя
        """
        self.all_operations[choice] = not self.all_operations[choice]

    def closeEvent(self,event):
        sys.exit()


class MainWindow(QMainWindow):
    """ Коренное окно для визуализации схемы, разметки наименований, расположения таблиц на схеме"""
    def __init__(self):
        super().__init__()
        
    def __init_main_win__(self, rooms_charact={'test':[],'2 floor':[]}, shapes_of_lists = [1655.511811023622, 1169.291338582677], table_itso=[], table_dangerous = [], table_other_elements = []):
        self.position_for_numbers = {} # координаты расстановки номеров
        self.table_dangerous = table_dangerous
        self.other_elements = table_other_elements
        self.table_ITSO = list(table_itso)
        self.deleted_shape = None
        self.shapes_of_lists = shapes_of_lists
        self.resize(1000, 1000)

        self.threadpool = QThreadPool()

        self.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(self) #
        self.setCentralWidget(self.centralwidget) #
        self.centralwidget.resize(QSize(int(self.width()),int(self.height())))
        self.centralwidget.setLayout(QVBoxLayout())
        
        self.dict_namefile_and_scene = {name : QGraphicsScene() for name in rooms_charact.keys()}
        self.workspace_for_holst = self.dict_namefile_and_scene[list(self.dict_namefile_and_scene.keys())[0]] # рабочий лист        
        self.worksheet = QGraphicsView()  # создание рабочей области 
        self.worksheet.resize(self.width(),self.height())
        self.centralwidget.layout().addWidget(self.worksheet)
        self.worksheet.setScene(self.workspace_for_holst)
        
        pen = QPen(QColor('black'))
        brush = QBrush(QColor('white'))
        self.down_toolbar = QtWidgets.QToolBar(self)
        self.down_toolbar.setFixedHeight(35)
        self.down_toolbar.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft) # указание компоновки слева направо
        self.addToolBar(QtCore.Qt.ToolBarArea.BottomToolBarArea, self.down_toolbar)
        self.fileBar = QtWidgets.QToolBar(self)
        self.fileBar.setFixedWidth(100)
        self.addToolBar(QtCore.Qt.ToolBarArea.LeftToolBarArea,self.fileBar)
        
        self.cur = QtGui.QCursor()

        self.up_tools = QtWidgets.QToolBar(self)
        self.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.up_tools)
        self.up_tools.setFixedHeight(50)
        self.up_tools.setMovable(False)
        
        self.actual_namefile = QLabel(str(list(self.dict_namefile_and_scene.keys())[0]),self)
        self.actual_namefile.setAlignment(Qt.AlignTop)
        self.up_tools.addWidget(self.actual_namefile)
        
        self.buttons = {}
        for name in rooms_charact.keys():
            elem = self.dict_namefile_and_scene[name]
            button_for_file = QtWidgets.QPushButton(name,self.fileBar)
            self.fileBar.addWidget(button_for_file)
            self.buttons[button_for_file] = elem
            button_for_file.clicked.connect(self.select_file)
            elem.setBackgroundBrush(QColor('darkGray'))
            elem.setSceneRect(QRectF(0., 0., float(self.shapes_of_lists[name][0]), float(self.shapes_of_lists[name][1])))
            elem.addRect(0, 0, self.shapes_of_lists[name][0], self.shapes_of_lists[name][1], pen,brush)
        
        button_exit = QtWidgets.QPushButton('Завершить', self.fileBar)
        self.fileBar.addWidget(button_exit)
        button_exit.clicked.connect(self.room_numbering)
        self.worksheet.scale(.5,.5)  # Устанавливаем начальный масштаб
        
        self.gui_zoom()
        self.setup_visible()

        self.its_button = list(self.buttons.keys())[0]
        self.its_button.setFlat(True)
        self.list_tables = {file: [] for file in self.dict_namefile_and_scene.keys()}
        self.visible_table = False

        self.rooms_charact = self.convert_cords(rooms_charact)
        self.show_walls()
        try:
            self.show_doors()
            self.show_stairs()
        except:
            pass
        self.check_wrong_rooms()


    def create_dialog_menu(self):
        dialog = StartWindow()
        dialog.show()
        dialog.thread().exec_()
        
        info = dialog.parse_info
        return info
    
    def load_dict(self):
        with open('list_words.json', encoding='utf-8') as f:
            self.words = json.load(f,)
    
    
    def next_etap(self):
        """ Метод используется для возможности пропуска прописи экспликации
        Так же этот метод является корневым методом для завершения работы гуи визуализации и следовательно является
        переходом к следующему этапу"""
        if not self.visible_table:
            for nameFile in self.position_for_numbers.keys():
                for indexroom in range(len(self.position_for_numbers[nameFile])):
                    self.position_for_numbers[nameFile][indexroom][-1] = ''
                self.show_tabels(self.dict_namefile_and_scene[nameFile], nameFile) 
            self.visible_table = True
        else: 
            self.close()
            self.thread().exit()

    @pyqtSlot()
    def show_tabels(self, this_scene, thisfile):
        """ Является методом инициализации всех существующих таблиц с их последющей визуализацией на схеме"""
        self.list_tables[thisfile] = {}
        if all_operations['Экспликация']:
            self.list_tables[thisfile][QColor('darkcyan').name()] = self.table_rooms = Rooms([this_scene,thisfile],self.position_for_numbers[thisfile],self.shapes_of_lists[thisfile])
        self.move_stat = None
        if all_operations['ИТСО']:
            self.list_tables[thisfile][QColor('darkBlue').name()] = self.ITSO = ITSO([this_scene,thisfile], self.table_ITSO,self.shapes_of_lists[thisfile])
        
        if all_operations['ПОУ и КЭО']:
            self.list_tables[thisfile][QColor('red').name()] = self.DANGEROUS = Dangerous([this_scene,thisfile], self.table_dangerous,self.shapes_of_lists[thisfile])
        self.list_tables[thisfile][QColor('green').name()] = self.table_elements = Other_elements([this_scene,thisfile], self.other_elements,self.shapes_of_lists[thisfile])
        
        for t in self.list_tables[thisfile].values(): 
            try:
                t.post()
            except Exception as e: print(e)
        """
        elements = {}
        elements[thisfile] = self.position_for_numbers[thisfile]
        sql.cashe('rooms', elements) нет sql в общем доступе. Хз нужно или нет. Обдумаю"""

    def select_file(self):
        """ Смена файла по нажатию на кнопку из левого балуна"""
        self.its_button.setFlat(False)
        self.its_button = self.sender()
        self.its_button.setFlat(True)
        self.worksheet.setScene(self.buttons[self.its_button])
        self.actual_namefile.setText(self.its_button.text())


    def visible_doors(self):
        """ Вызываемый метод по нажатию на кнопку 'Отобразить двери' ведётся проверка статуса кнопки(активна/неактивна)
         Тут же и лежит отрисовка дверей """
        if not self.visible_doors_button.isFlat():
            self.placement_doors_on_scene = {}
            self.placement_mndoors_on_scene = {}
            self.visible_doors_button.setFlat(True)
            for scene, doors in self.doors_on_scene.items():
                placement_doors = []
                main_doors = []
                for door in doors:
                    if isinstance(door[0],QRectF):
                        placement_doors.append(scene.addEllipse(*door))
                    else:
                        if door[4].color() == QPen(QColor('red')):
                            main_doors.append(scene.addLine(*door))
                        placement_doors.append(scene.addLine(*door))
                self.placement_doors_on_scene[scene] = placement_doors
                self.placement_mndoors_on_scene[scene] = main_doors
        else:
            self.visible_doors_button.setFlat(False)
            for scene, doors in self.placement_doors_on_scene.items():
                for door in doors:
                    scene.removeItem(door)
            del self.placement_doors_on_scene

    
    def visible_stairs(self):
        """ Вызываемый метод по нажатию на кнопку 'Отобразить лестницы' ведётся проверка статуса кнопки(активна/неактивна)
         Тут же и лежит отрисовка лестниц """
        if not self.visible_stairs_button.isFlat():
            self.placement_stairs_on_scene = {}
            self.visible_stairs_button.setFlat(True)
            try:
                for scene, stairs in self.stairs_on_scene.items():
                    placement_stairs = []
                    for stair in stairs:
                        placement_stairs.append(scene.addPolygon(*stair))
                    self.placement_stairs_on_scene[scene] = placement_stairs
            except Exception as e:
                print('траблы с дверьми', e)
                
        else:
            self.visible_stairs_button.setFlat(False)
            for scene, stairs in self.placement_stairs_on_scene.items():
                for stair in stairs:
                    scene.removeItem(stair)
            del self.placement_stairs_on_scene


    def go_naming_rooms(self):
        """ Активация режима 'Нумерация и экспликация' 
        Запускается инициализация доп. гуи в верхнем тулбаре
        На этом этапе подгружается изменяемый в json - словарь помещений"""
        self.load_dict()

        try:
            self.index_file
        except:
            # элементы гуи
            self.index_file, self.index_room = 0,0
            self.out = QtWidgets.QPushButton('Выйти', self.fileBar)
            self.out.clicked.connect(self.next_etap)
            self.fileBar.addWidget(self.out)
            self.out.setGeometry(QRect(100,200,100,10))
            self.name_room_lab = QLabel('Наименование', self)
            self.input_name = QLineEdit()
            self.input_name.installEventFilter(self)
            self.input_name.setCompleter(QCompleter(self.words['words']))
            self.up_tools.addWidget(self.name_room_lab)
            self.up_tools.addWidget(self.input_name)
            self.input_name.completer().activated.connect(self.select_v)
            self.input_name.returnPressed.connect(self.save_name_room)
            self.position_for_numbers[list(self.position_for_numbers.keys())[0]][0][-1].setBrush(QBrush(QColor('red')))
            list(self.buttons.keys())[0].click()
            
    def select_v(self):        
        """ Используется при нажатии на ENTER в режиме 'Нумерация и экспликация' - очищает вводную строку"""
        QTimer.singleShot(0, self.input_name.clear)

    def time_travel_for_naming_rooms(self):
            """ Часть  eventFilter должна была отвечать за смену цвета при отмене действия"""
            """Не канает, выдаёт ошибку"""
            if self.index_room > 0:
                self.index_room -= 1
                self.position_for_numbers[self.name_file][self.index_room+1][-1].setBrush(QColor('green'))
                self.position_for_numbers[self.name_file][self.index_room][-1].setBrush(QColor('red'))
                pass

    def save_name_room(self): 
        """ Коренной метод при наименовании помещений
        Отвечает за цветовое выделение помещения, 
        тут же хавается наименование с выравниванием первого символа на верхний регистр
          Тут же лежит логика перемещения по помещениям и файлам  """

        self.name_file = list(self.position_for_numbers.keys())[self.index_file]
        self.visible_table = True
                
        if len(self.position_for_numbers[self.name_file]) > self.index_room:
            try:
                self.position_for_numbers[self.name_file][self.index_room][-1].setBrush(QColor('green'))
                self.position_for_numbers[self.name_file][self.index_room][-1] = self.input_name.text().capitalize()
            except AttributeError: pass
            self.input_name.clear()
            if self.index_room != len(self.position_for_numbers[self.name_file]) - 1:
                self.index_room += 1
            else:
                self.index_room = 0
                if self.index_file != len(list(self.position_for_numbers.keys())) -1:
                    self.index_file += 1
                    self.name_file = list(self.position_for_numbers.keys())[self.index_file]
                    button_next_file = list(self.buttons.keys())[list(self.dict_namefile_and_scene.values()).index(self.dict_namefile_and_scene[self.name_file])] 
                    button_next_file.click()
                    self.index_room = 0
                else:
                    for nameFile in self.position_for_numbers.keys():
                        self.show_tabels(self.dict_namefile_and_scene[nameFile], nameFile)
                    # self.show_tabels()
            try:
                self.position_for_numbers[self.name_file][self.index_room][-1].setBrush(QColor('red'))
            except: 
                pass


    def room_numbering(self):
        """ Пробегаем по формам помещений, добавляем им нумерацию по левому верхнему краю и сейвим в список для 
        указания наименования и дальнейшего использования на этапе размещения таблиц и иных элементов"""
        font = QtGui.QFont('Arial',10)

        for name, attrib in self.dict_namefile_and_scene.items():
            try:
                x,y = self.polygons[name][2:4]
                marked_rooms = [] # меченные фигуры
                numbering = []

                for room in reversed(self.dict_rooms_on_scene[attrib]):
                    min_y = y
                    r = room.polygon()
                    
                    for point in room.polygon(): # Определение верхнего левого края помещения
                        if min_y > point.y():
                            min_y = point.y()
                            min_x = point.x()
                        elif min_y == point.y():
                            if min_x > point.x():
                                min_x = point.x()
                    
                    marked_rooms.append(room)
                    attrib.addText(str(len(marked_rooms)), font).setPos(QPointF(min_x, min_y))
                    numbering.append([min_x+10,min_y+10,str(len(marked_rooms)),room])
                self.position_for_numbers[name] = numbering
            except:
                pass    
        self.go_naming_rooms()
        del self.words


    def get_rooms(self):
        """ Возвращает инфу о таблицах и позиции нумерации после закрытия данного окна"""
        list_tables = {file: [] for file in self.list_tables.keys()}
        for file, tTable in self.list_tables.items():
            try:
                list_tables[file] = [table for table in list(self.list_tables[file].values())]
            except Exception as e:
                print('Произошла ошибка возврата данных из визуала', e)
        return list_tables
        


    def show_walls(self):
        """ Отрисовка стен на схеме"""
        # Вероятно следует создать общий метод создания дверей и стен
        pen = QPen(QColor('black'))
        brush = QBrush(QColor('darkGray'))
        self.polygon()
        self.walls_on_scene = {}
        for key,scene in self.dict_namefile_and_scene.items():
            walls = []
            for cord in self.rooms_charact[key]['walls']:
                x1,y1,x2,y2 = cord[0],cord[1],cord[2],cord[3]
                walls.append(scene.addLine(x1,y1,x2,y2,QPen(QColor('black'),cord[4])))
            self.walls_on_scene[scene] = walls
        self.go_image()

    def show_doors(self):
        """ Буфферизация информации о расположении и виде двери для ускоренной отрисовки
        Юзается только раз"""
        self.main_doors_on_scene = {}
        self.doors_on_scene = {}
        for key,scene in self.dict_namefile_and_scene.items():
            min_height = min(list(h[2] for h in self.rooms_charact[key]['doors']))
            self.max_height_door = max(list(h[2] for h in self.rooms_charact[key]['doors']))
            doors = []
            main_doors = []
            for characters in self.rooms_charact[key]['doors']: # Подбираем градус перпендикулярного поворота линии 
                rooms_lenght = 0
                x, y, height = characters[0] - characters[2] * .5, characters[1] - characters[2] * .5, characters[2]
                wall = scene.itemAt(QPointF(x,y), QTransform())
                if wall in self.walls_on_scene[scene]:
                    line = wall.line()
                    angle = line.angle() 
                    angle_wall = angle * (3.14 / 180)
                    angle_door = 90 * (3.14 / 180)
                    x1 = (height*2) * cos(-angle_wall+angle_door) + x
                    y1 = (height*2) * sin(-angle_wall+angle_door) + y
                    x2 = (height*2) * cos(-angle_wall-angle_door) + x
                    y2 = (height*2) * sin(-angle_wall-angle_door) + y
                    if type(scene.itemAt(QPointF(x1,y1),QTransform())) is Room:
                        rooms_lenght += 1
                    if type(scene.itemAt(QPointF(x2,y2), QTransform())) is Room:
                        rooms_lenght += 1
                else:
                    for ay, ax in itertools.product(range(0,10,2), range(0,10,2)):
                        wall = scene.itemAt(QPointF(x+ax,y+ay), QTransform())
                        if wall in self.walls_on_scene[scene]:
                            x,y = x + ax, y + ay
                            line = wall.line()
                            angle = line.angle() 
                            angle_wall = angle * (3.14 / 180)
                            angle_door = 90 * (3.14 / 180)
                            x1 = (height*2) * cos(-angle_wall+angle_door) + x
                            y1 = (height*2) * sin(-angle_wall+angle_door) + y
                            x2 = (height*2) * cos(-angle_wall-angle_door) + x
                            y2 = (height*2) * sin(-angle_wall-angle_door) + y
                            if type(scene.itemAt(QPointF(x1,y1),QTransform())) is Room:
                                rooms_lenght += 1
                            if type(scene.itemAt(QPointF(x2,y2), QTransform())) is Room:
                                rooms_lenght += 1
                            break
                    else:
                        doors.append([QRectF(x,y,15.,15.),QPen(QColor('white')), QBrush(QColor('white'))]) 
                if rooms_lenght == 1:
                    pen = QPen(QColor('red'),min_height)
                    main_doors.append([x1,y1,x2,y2,pen])
                else:
                    pen = QPen(QColor('yellow'),min_height)
                try:
                    doors.append([x1, y1, x2, y2, pen])
                except: 
                    pass
            self.main_doors_on_scene[scene] = main_doors
            self.doors_on_scene[scene] = doors


    def show_stairs(self):
        """ Буфферизация информации о расположении лестниц для облегчённого рендеринга"""
        self.stairs_on_scene = {} 
        for key,scene in self.dict_namefile_and_scene.items():
            stairs = []
            for characters in self.rooms_charact[key]['stairs']:
                x,y,angle = characters[0], characters[1], characters[2] if characters is not None else 0
                points = [[x-self.max_height_door, y - self.max_height_door],[x, y - self.max_height_door*1.5],[x + self.max_height_door,y - self.max_height_door],
                          [x + self.max_height_door, y + self.max_height_door], [x - self.max_height_door, y + self.max_height_door]]
                points = [QPointF(x,y) for x,y in points]
                stairs.append((QPolygonF(points), QPen(QColor('black')), QBrush(QColor('yellow'))))
            self.stairs_on_scene[scene] = stairs


    def check_wrong_rooms(self):
        """ Отображение 'глухих помещений' на схеме
        Иногда софт может ошибаться из за метода show_doors """
        self.visible_doors_button.setFlat(False)
        self.visible_doors()
        self.path_of_rooms = []

        self.finished_rooms = {scene: [] for scene in self.main_doors_on_scene.keys()}
        for scene,doors in self.placement_mndoors_on_scene.items():
            for door in doors:
                self.path_of_rooms = []
                for room in door.collidingItems():
                    if type(room) is Room:
                        self.path_of_rooms.append(room)
                        self.doors_loop(scene, room)
                        
            try:
                if len(self.finished_rooms[scene]) != len(self.dict_rooms_on_scene[scene]):
                    for stair in self.stairs_on_scene[scene]:
                        room = scene.itemAt(stair[0].value(0), QTransform())
                        if room not in self.finished_rooms[scene] and type(room) is Room:
                            self.path_of_rooms.append(room)
                            self.doors_loop(scene,room)
            except:
                pass

    def doors_loop(self, scene,main_room):
        """ По принципу лабиринта определяет помещения в которые можно попасть либо от лестницы
        либо от двери которая соединена с 1 помещением"""
        try:
            for item in main_room.collidingItems():
                if item in self.placement_doors_on_scene[scene]:
                    for room in item.collidingItems():
                        if room not in self.path_of_rooms and room not in self.finished_rooms[scene] and type(room) is Room:
                            self.path_of_rooms.append(room)
                            self.doors_loop(scene,room)
            main_room.setBrush(QColor('gray'))
        except Exception as e:
            print('doors_loop ERROR', e)
        try:
            self.finished_rooms[scene].append(room)
        except:
            pass
        

    def go_image(self):
        """ Трансформация отображенного чертежа в формат картинки для дальнейшего сканирования,
          с целью определения контуров помещений """
        self.room_point_shapes = {}
        if all_operations['Пути эвакуации']:
            self.sd()
            self.show_rect_doors()
        for name,scene in self.dict_namefile_and_scene.items():
            self.name_file = name
            image = QImage(scene.sceneRect().size().toSize(), QImage.Format_RGB888)
            image.fill(QtCore.Qt.transparent)
            painter = QPainter(image)
            scene.render(painter)
            painter.end()

            # Сохранение изображения в файл
            image.save('\\images\\' + name +".png")
            self.check_room_shape(image)
        self.show_room_shapes()


    def sd(self):
        """ Буфферизация информации о параметрах дверей
        Юзается только раз"""
        self.main_doors_on_scene = {}
        self.doors_on_scene = {}
        for key,scene in self.dict_namefile_and_scene.items():
            min_height = min(list(h[2] for h in self.rooms_charact[key]['doors']))
            self.max_height_door = max(list(h[2] for h in self.rooms_charact[key]['doors']))
            doors = []
            for characters in self.rooms_charact[key]['doors']: # Подбираем градус перпендикулярного поворота линии 
                rooms_lenght = 0
                x, y, height = characters[0] - characters[2] * .5, characters[1] - characters[2] * .5, characters[2]
                doors.append([QRectF(x-5.,y-5.,10.,10.),QPen(QColor('white')), QBrush(QColor('white'))]) 
            self.doors_on_scene[scene] = doors


    def show_rect_doors(self):
        """ Отображение двери как квадрата. Используется на планах эвакуации """
        self.visible_doors_button.setFlat(True)
        for scene, doors in self.doors_on_scene.items():
            placement_doors = []
            for door in doors:
                placement_doors.append(scene.addEllipse(*door))
        
            
    def check_room_shape(self,img):
        """ Получение размеров помещения"""
        """  Converts a QImage into an opencv MAT format  """
        
        incomingImage = img.convertToFormat(QImage.Format.Format_RGBA8888)
        width = incomingImage.width()
        height = incomingImage.height()

        ptr = incomingImage.bits()
        ptr.setsize(height * width * 4)
        arr = np.frombuffer(ptr, np.uint8).reshape((height, width, 4))
        rooms_shapes = cv_for_numbers.Shape_room(arr)
        list_shapes = rooms_shapes.get_contours()
        self.room_point_shapes[self.name_file] = list_shapes


    def show_room_shapes(self):
        """ Удаление псевдо помещений.  Метод check_room_shape получает только лишь контуры всех фигур
        Данный метод удаляет фигуры которые связаны либо с самим холстом, либо со стеной"""
        self.dict_rooms_on_scene = {}
        for name, scene in self.dict_namefile_and_scene.items():
            self.list_of_shapes = []
            for shape in self.room_point_shapes[name]:
                for list_point in shape:
                    list_point = list_point.tolist()
                    self.points = []
                    for point in list_point:
                        self.points.append(QPointF(*map(float,point[0])))
                    self.list_of_shapes.append(self.points)
            self.room_shapes = [] 
            for points in self.list_of_shapes:
                item = Room(polygon=QPolygonF(points),pen=QPen(QColor('black')),brush=QBrush(QColor('yellow')))
                scene.addItem(item)
                self.room_shapes.append(item)
            for item_scene in self.walls_on_scene[scene]:
                item = scene.itemAt(item_scene.line().p1(), QTransform())
                try:
                    if type(item) is Room:
                        item.hide_room()
                except Exception as e:
                    print('СТЕНА НЕ УДАЛЕНА', e)
            self.dict_rooms_on_scene[scene] = self.room_shapes
            self.remove_missing_room()
        
    def update_all_rooms(self, append_room=None):
        """ Должны пробегать по сценам и проверять присутствует ли тот же объект в координатах
        указанного объекта, в случае если есть совпадение возвращаем объект в словарь к ключу сцены"""
        dict_rooms_on_scene = {}
        for scene in list(self.dict_rooms_on_scene.keys()):
            dict_rooms_on_scene[scene] = []
            for room in self.dict_rooms_on_scene[scene]:
                    if room.active:
                        dict_rooms_on_scene[scene].append(room)
        self.dict_rooms_on_scene = dict_rooms_on_scene
            
    def remove_missing_room(self):
        """ Исключение глухого помещения из списка помещений, который мы сами пометили как глухое"""
        for key, scene in self.dict_namefile_and_scene.items():
            for characters in self.rooms_charact[key]['slab']:
                item = scene.itemAt(QPointF(*characters),QTransform())
                if type(item) is Room:
                    item.hide_room()

        self.update_all_rooms()

    def convert_cords(self,rooms_charact):
        """ Конвертирование координат x и y между форматами vsdx и обычными координатами в обе стороны"""
        """ Для чего конвертация координат: Visio переделал направление y как в математике. По факту у ПК график идёт вниз на возрастание, но у Visio вверх"""

        keys_of_rooms = list(rooms_charact.keys()) 
        if isinstance(rooms_charact[keys_of_rooms[0]], list):
            try:
                for room in keys_of_rooms:
                    list_cords = rooms_charact[room]
                    for row, i in itertools.product(range(len(list_cords[0])), range(len(list_cords[0][row]))):
                        if i % 2 == 1:
                            rooms_charact[room][0][row][i] = -list_cords[0][row][i] + self.shapes_of_lists[room][1]
            except:
                for room in keys_of_rooms:
                    list_cords = rooms_charact[room]
                    for index,cords in enumerate(list_cords):
                        for i in range(len(cords)):
                            if i % 2 == 1 and rooms_charact[room][index][i] != rooms_charact[room][index][-1]:
                                rooms_charact[room][index][i] = -cords[i] + self.shapes_of_lists[room][1]

        elif isinstance(rooms_charact[keys_of_rooms[0]], dict):
            for name_floor in keys_of_rooms:
                for type_element in rooms_charact[name_floor]:
                    for row in range(len(rooms_charact[name_floor][type_element])):
                        for i in range(len(rooms_charact[name_floor][type_element][row])):
                            change_element = rooms_charact[name_floor][type_element][row][i]
                            if i % 2 == 1:
                                rooms_charact[name_floor][type_element][row][i] = -change_element + self.shapes_of_lists[name_floor][1]
        else:
            raise TypeError
        
        return rooms_charact
    

    def polygon(self):
        """ Определение контура здания"""
        self.polygons = {name : [self.shapes_of_lists[name][0], self.shapes_of_lists[name][1], -1., -1.] for name in self.rooms_charact.keys()}
        for name,cord_polygon in self.polygons.items():

            try:
                self.max_x,self.min_x = max(list(map(max,[x[0:3:2] for x in self.rooms_charact[name]['walls']]))), \
                                            min(list(map(min,[x[0:3:2] for x in self.rooms_charact[name]['walls']])))
                self.max_y, self.min_y = max(list(map(max,[y[1:4:2] for y in self.rooms_charact[name]['walls']]))),\
                    min(list(map(min,[y[1:4:2] for y in self.rooms_charact[name]['walls']])))
            
                self.polygons[name] = self.min_x, self.min_y, self.max_x, self.max_y
            except:
                self.polygons[name] = [shape // 2 for shape in self.shapes_of_lists[name]]


    def get_key(self, search_value):
        for key, value in self.dict_namefile_and_scene.items():
            if value == search_value:
                return key
        return ''
    

# ниже всё касаемое мыши
    def contextMenuEvent(self,e):
        """ Контекстное меню при нажатии на помещение"""
        self.worksheet.setMouseTracking(True)
        context = QMenu(self)
        element_scene = self.worksheet.scene().itemAt(self.worksheet.mapToScene(self.worksheet.mapFromParent(self.centralwidget.mapFromParent(self.position_mouse))), QTransform())
        if type(element_scene) is Room:
            if element_scene.active:
                delete = QAction('Удалить',self)
                context.addAction(delete)
                delete.triggered.connect(element_scene.hide_room)
            else:
                delete = QAction('Удалить полностью',self)
                context.addAction(delete)
                delete.triggered.connect(lambda : self.cashe_elements(element_scene))
                recovery = QAction('Восстановить',self)
                context.addAction(recovery)
                recovery.triggered.connect(element_scene.visible_room)
            enter_room = QAction('Указать входным помещением')
            context.addAction(enter_room)
            enter_room.triggered.connect(lambda: self.doors_loop(self.worksheet.scene(),element_scene))
        if type(element_scene) == QtWidgets.QGraphicsRectItem and element_scene.brush().color().name() != '#ffffff':
            for file, scene in self.dict_namefile_and_scene.items():
                if scene == self.worksheet.scene():
                    break
            type_table = self.list_tables[file][element_scene.brush().color().name()]
            moveTable = QAction('Взять', self)
            context.addAction(moveTable)
            moveTable.triggered.connect(lambda : self.change_moveStatus(type_table))
            toOne = QAction('В 1 столбец', self)
            context.addAction(toOne)
            toOne.triggered.connect(lambda : type_table.resize(1))
            toTwo = QAction('В 2 столбца',self)
            context.addAction(toTwo)
            toTwo.triggered.connect(lambda : type_table.resize(2))
            toThree = QAction('В 3 столбца',self)
            context.addAction(toThree)
            toThree.triggered.connect(lambda : type_table.resize(3))
        return_button = QAction('Отменить последнее действие',self)
        context.addAction(return_button)
        return_button.triggered.connect(self.return_deleted_element)
        context.exec(e.globalPos())

    def change_moveStatus(self, table):
        if self.move_stat is None:
            self.move_stat = table
        else:
            self.move_stat = None

    def cashe_elements(self,element):
        """ Буфферизация информации о удаленных помещениях"""
        """Вероятно этот метод устарел"""
        if self.position_for_numbers != {}:
            namefile = self.get_key(self.worksheet.scene())
            for index in range(len(self.position_for_numbers[namefile])):
                if self.position_for_numbers[namefile][3] == element:
                    self.position_for_numbers[namefile].pop(index)
                self.position_for_numbers[namefile][index][2] = str(index+1)
            for item in element.collidingItems():
                if type(item) is QGraphicsTextItem:
                    self.worksheet.scene().removeItem(item)
                    break
        self.deleted_shape = element
        self.dict_rooms_on_scene[self.worksheet.scene()].remove(element)
        self.worksheet.scene().removeItem(element)
        self.worksheet.scene().update()


    def return_deleted_element(self):
        """ Отмена удаления помещения"""
        if self.deleted_shape != None:
            self.worksheet.scene().addItem(self.deleted_shape)
            self.dict_rooms_on_scene[self.worksheet.scene()].append(self.deleted_shape)
            self.deleted_shape = None
    

    def mouseMoveEvent(self, mouse_pos):
        try:
            mouse_pos = self.worksheet.mapToScene(self.worksheet.mapFromGlobal(mouse_pos))
            if not self.move_stat is None:
                self.move_stat.move(mouse_pos.x(), mouse_pos.y())
        except:
            pass

    def updateAnchorViewCenter(self):
        pos = self.worksheet.mapFromGlobal(self.cur.pos())
        self.worksheet.centerOn(pos)
        self.worksheet.update()
    
    def wheelEvent(self, event):
            """ Условия для зума при комбинации CTRL + Средняя кнопка мыши(её вращение)"""
            if event.angleDelta().y() > 0 and QtGui.QGuiApplication.keyboardModifiers() & QtCore.Qt.ControlModifier:
                self.updateAnchorViewCenter()
                self.zoomIn()
            elif event.angleDelta().y() < 0 and QtGui.QGuiApplication.keyboardModifiers() & QtCore.Qt.ControlModifier:
                # Прокрутка вниз при зажатой Ctrl
                self.updateAnchorViewCenter()
                self.zoomOut()

    def show_path(self):
        for door in self.main_doors_on_scene[self.worksheet.scene()]:
            pass
        

# ниже идут элементы гуи
    def setup_visible(self):
        """ Нижний тулбар с функциональными кнопками"""
        self.visible_path = QtWidgets.QPushButton(self.down_toolbar)
        self.visible_path.setGeometry(self.width()//2 - 320,0,150,30)
        self.visible_path.setFont(QFont('Arial',8))
        self.visible_path.setText('Отобразить путь')
        self.visible_path.clicked.connect(self.show_path)
        
        
        self.visible_doors_button = QtWidgets.QPushButton(self.down_toolbar)
        self.visible_stairs_button = QtWidgets.QPushButton(self.down_toolbar)
        self.visible_doors_button.setGeometry(self.width()//2,0,150,30)
        self.visible_doors_button.setFont(QFont('Arial',8))
        self.visible_doors_button.setText('Отобразить двери')
        self.visible_stairs_button.setGeometry(self.width()//2 - 160,0,150,30)
        self.visible_stairs_button.setFont(QFont('Arial',8))
        self.visible_stairs_button.setText('Отобразить лестницы')
        self.visible_doors_button.clicked.connect(self.visible_doors)
        self.visible_stairs_button.clicked.connect(self.visible_stairs)
        

    def gui_zoom(self):
        """ Кнопки зума на нижнем и левом тулбарах"""
        self.zoomInButton = QtWidgets.QPushButton(text="+",parent=self.down_toolbar)
        self.zoomOutButton = QtWidgets.QPushButton(text="-", parent=self.down_toolbar)
        self.zoomOutButton.setGeometry(QRect(self.width()-95,0,35,35))
        
        self.zoomInButton.clicked.connect(self.zoomIn)
        self.zoomOutButton.clicked.connect(self.zoomOut)

    def zoomIn(self):
        factor = 1.25  # Фактор увеличения
        self.worksheet.scale(factor, factor)

    def zoomOut(self):
        factor = 1 / 1.25  # Фактор уменьшения
        self.worksheet.scale(factor, factor)
        
# хот кеи и иной функционал

    def keyPressEvent(self,event):
        """ Нериализованная отмена действия по комбинации клавиш при наименовании помещений"""
        if event.key() == (Qt.Key_Control and Qt.Key_Y):
            self.time_travel_for_naming_rooms()




class Table:
    """ Отец всех таблиц. Данный класс кочует из этого файла в файл placement_of_objects с переопределением типов данных"""
    # Обдумать уйти от кастомных методов в наследуемых классах путём подготовки одинаковых данных
    def __init__(self,scene,width,height,cell_height):
        self.scene = scene
        self.original_width = width
        self.original_height = height
        self.height = height
        self.cell_height = cell_height
        self.max_sym = 41
        self.shapes_of_lists = window.shapes_of_lists

    def resize(self,row):
        self.scene[0].removeItem(self.rect)
        self.height = self.original_height
        start = math.ceil(len(self.elements)/row) if math.ceil(len(self.elements)/row) != len(self.elements) else 0
        column = 1
        for index_element in range(start,len(self.elements)):
            if start != 0:
                if index_element + 1 - start * column > 0:
                    column += 1
            self.elements[index_element][-1] = column
        
        self.width = self.original_width * row
        self.table_height()
        self.rect = self.scene[0].addRect(QRectF(float(self.x),float(self.y),self.width,self.height), QPen(QColor('black')), QBrush(QColor(self.color)))
    
    def cells_height(self):
        for index, element in enumerate(self.elements):
            if len(element[-1]) > self.max_sym:
                cell_height = self.cell_height * 1.51
            else:
                cell_height = self.cell_height
            self.elements[index] = [element, cell_height, 1]
    
    def table_height(self):
        self.rows_height = {i:self.height for i in range(1,7)}
        for element in self.elements:
            self.rows_height[element[-1]] += element[-2]
        self.height = max(self.rows_height.values())


    def post(self):
        """ Реализация подбора кол-ва столбцов и строк + определение высоты строки"""
        if len(self.elements) > 0: 
            
            self.elements = deepcopy(self.original_elements)
            self.cells_height()
            for row in range(1,6):
                self.width = self.original_width * row
                self.height = self.original_height
                if math.ceil(len(self.elements)/row) >= 3:
                    start = math.ceil(len(self.elements)/row) if math.ceil(len(self.elements)/row) != len(self.elements) else 0
                    column = 1
                    # делим индекс 
                    for index_element in range(start,len(self.elements)):
                        if start != 0:
                            if index_element + 1 - start * column > 0:
                                column += 1

                        self.elements[index_element][-1] = column
                    if row == 1:
                        elements = deepcopy(self.elements)
                        
                    if self.set_position() == True:
                        break
            else:
                try:
                    self.elements = elements
                except: self.elements = []
                self.width = self.original_width
                self.height = self.original_height
                self.x, self.y = self.default_pos
            
            self.rect = self.scene[0].addRect(QRectF(float(self.x),float(self.y),self.width,self.height),QPen(QColor('black')), QBrush(QColor(self.color)))
        
    def move(self,x,y):
        self.scene[0].removeItem(self.rect)
        self.rect = self.scene[0].addRect(QRectF(float(x),float(y),self.width,self.height),QPen(QColor('black')), QBrush(QColor(self.color)))
        self.x, self.y = x,y


    def set_position(self):
        """ Ведёт поиск свободного пространства для сформированной таблицы. В случае неудачи метод возвращается в post и меняет параметры и так по циклу,
        до тех пор пока таблица не будет иметь менее 3х строк в столбце. При таком расскладе программа отводит таблицу в сторону от чертежа для ручной вправки"""
        self.table_height()
       
        for self.y, self.x in itertools.product(range(221, int(self.shapes_of_lists[self.scene[1]][1]) - 52 - int(self.height),10),
                                                range(52, int(self.shapes_of_lists[self.scene[1]][0]) - 102 - int(self.width),10)):
            check_rect = self.scene[0].addRect(QRectF(float(self.x),float(self.y),self.width,self.height))
            if len(check_rect.collidingItems()) == 1:
                self.scene[0].removeItem(check_rect)
                """Притирочные моменты."""
                self.y += self.cell_height * 1.7
                self.aroundrect = self.scene[0].addRect(QRectF(float(self.x-40),float(self.y),self.width,self.height), QPen(QColor('black')), QBrush(QColor('green')))
                """ Концепция реализована не полностью. Необходимо что бы софт проверял растояние в 3х точках"""
                if len(self.aroundrect.collidingItems()) > 1 and self.x + self.width + 40 < self.shapes_of_lists[self.scene[1]][0]:
                    self.x += 40
                self.scene[0].removeItem(self.aroundrect)
                self.aroundrect = self.scene[0].addRect(QRectF(float(self.x),float(self.y - 40),self.width,self.height))
                if len(self.aroundrect.collidingItems()) > 1 and self.y + self.height < self.shapes_of_lists[self.scene[1]][1]:
                    self.y += 40
                self.scene[0].removeItem(self.aroundrect)
                
                return True
            else:
                self.scene[0].removeItem(check_rect)
        
    def get_shape(self):
        """ Получение размеров таблицы. """
        return self.x, self.y, self.width, self.height


    def vsdx_format(self, place,text):
        ''' Отзеркаливает координату по y и определяет подпись 1 столба'''
        try:
            self.place = place
            self.text = text
            self.y = -self.y + self.shapes_of_lists[self.scene[1]][1]  
            if self.elements is ITSO:
                return
            try:
                for index, info in enumerate(self.elements):
                    self.elements[index][0][1] = -info[0][1] + self.shapes_of_lists[self.scene[1]][1]  
            except Exception as e: print('исключение при конвертации в всдх', e)
            self.second_text = '№' if self.text == 'Экспликация помещений' else 'Обозначение'
            
            del self.shapes_of_lists
            del self.scene
            del self.color

        except AttributeError as e:
            print('Отсутствует таблица!', e)

    def add_header(self,file):
        """ Добавление заголовка таблицы на чертеж Visio"""
        try:
            self.x += self.width // 2
            self.file = file
            # Тут должно вычитаться ещё половина высоты заголовка
            self.place.append_heading(x=self.x, y=self.y+self.cell_height*.5, width=self.width, height=self.cell_height*1.7, text=self.text)
            self.y -= self.cell_height * 1.7 
            try:
                for self.column in range(int(self.elements[-1][-1])): 
                    self.place.append_title(x=self.x + ((self.column) * self.original_width) - self.width*.5 + self.first_cell[0]*.5, y = self.y + self.cell_height * .5, width= self.first_cell[0], height= self.cell_height*1.4, text= self.second_text)
                    self.place.append_title(x= self.x + ((self.column) * self.original_width) - self.width*.5 + self.first_cell[0] + self.second_cell[0] * .5, y = self.y + self.cell_height * .5, width= self.second_cell[0], height= self.cell_height * 1.4, text= 'Наименование')
            except IndexError:
                self.place.append_title(x=self.x - self.width*.5 + self.first_cell[0]*.5, y = self.y + self.cell_height * .5, width= self.first_cell[0], height= self.cell_height*1.4, text= self.second_text)
                self.place.append_title(x= self.x - self.width*.5 + self.first_cell[0] + self.second_cell[0] * .5, y = self.y + self.cell_height * .5, width= self.second_cell[0], height= self.cell_height * 1.4, text= 'Наименование')
            self.y -= self.cell_height * .7
            self.y_firstRow = self.y        
            self.add_table()
        except AttributeError:
            pass # В случае отсутствия таблицы    

    def add_table(self):
        """ Добавление тела таблицы на схему Visio"""
        """" Тут будет биться список с данными [значение,высота ячейки]"""
        self.column = 1
        for i,self.line in enumerate(self.elements): 
            if self.line[-1] != self.column:
                self.y = self.y_firstRow
                self.column = self.line[-1]
            self.y -= self.line[1] * .5
            self.place.append_rect(x=self.x + ((self.column - 1)  * self.original_width)-self.width*.5 + self.first_cell[0] * .5, y = self.y + self.cell_height * .5, width= self.first_cell[0], height=self.line[1])
            try:
                self.objects[self.line[0]]()
            except KeyError as e:
                print(str(self.line) + ' не размещён', e) 

            self.place.append_rect(x=self.x + ((self.column - 1)  * self.original_width) - self.width*.5 + self.first_cell[0] + self.second_cell[0]*.5, y = self.y + self.cell_height * .5, width= self.second_cell[0], height= self.line[1], text=self.line[0])
            self.y -= self.line[1] * .5



class Rooms(Table):
    """ Класс таблицы Экспликация помещений """
    def __init__(self,scene,elements,pos):
        self.type = 'Rooms'
        self.default_pos = pos[0] + 200, pos[1] + 200
        self.color = 'darkcyan'
        self.original_elements = deepcopy(elements)
        self.elements = elements
        self.width = 197.7623540266463 
        self.height = 27.86333911651002 + 25.33030828773638
        self.first_cell = 36.36414563311183, 25.33030828773638
        self.second_cell = 161.3761444091797, 25.33030828773638
        self.cell_height = 12.66515414386819
        self.scene = scene
        super().__init__(scene,self.width,self.height,self.cell_height)


    def add_table(self):
        """" Кастом отцовского метода
        Тут будет биться список с данными [значение,высота ячейки]"""
        self.column = 1
        for i,self.line in enumerate(self.elements): 
            if self.line[-1] != self.column:
                self.y = self.y_firstRow
                self.column = self.line[-1]
            self.y -= self.line[1] * .5
            self.place.append_number_room(*self.line[0])
            self.place.append_rect(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5, y = self.y + self.cell_height * .5, width= self.first_cell[0], height=self.cell_height, text=self.line[0][2])
            self.place.append_rect(x=self.x + ((self.column - 1) * self.original_width) - self.width*.5 + self.first_cell[0] + self.second_cell[0] * .5, y = self.y + self.cell_height * .5, width= self.second_cell[0], height= self.cell_height, text=self.line[0][3])
            self.y -= self.line[1] * .5


class ITSO(Table):
    """ Класс таблицы ИТСО """
    def __init__(self,scene,elements,pos):
        self.type = 'ITSO'
        self.default_pos = pos[0] + 450, pos[1] + 200
        self.color = 'darkBlue'
        self.width = 320.1237335205092
        self.height = 42.86667556386156 + 23.22727879354197
        self.first_cell = 72.0, 23.22727879354197
        self.second_cell = 248.1237335205092, 23.22727879354197
        self.cell_height = 19.48485252902798
        self.scene = scene
        self.original_elements = deepcopy(list(elements))
        self.elements = list(elements)
        self.objects = {
                'Камера' : lambda   : self.place.append_cam(x=self.x + ((self.column - 1) * self.original_width) -self.width*.5 + self.first_cell[0] * .5,y=self.y + self.cell_height * .5 ),
                'Видеорегистратор': lambda   : self.place.append_videoreg(x=self.x + ((self.column - 1) * self.original_width) -self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Видеомонитор': lambda   : self.place.append_monitor(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'WI-FI-роутер': lambda   : self.place.append_WIFI(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Источник бесперебойного питания типа UPS': lambda   : self.place.append_ibp_220(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Блок контроля и индикации': lambda   : self.place.append_bki(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Пульт контроля и управления': lambda   : self.place.append_pku(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'ППКОП (контроллер) системы ОПС ': lambda   : self.place.append_PPKOP(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Извещатель пож дымовой ': lambda   : self.place.append_smoker(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Извещатель пож дымовой радиоканальный': lambda   : self.place.append_radio_smoker(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Извещатель пож ручной': lambda   : self.place.append_rpi(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                "Извещатель пож ручной радиоканальный" : lambda: self.place.append_radio_rpi(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Речевой оповещатель СОУЭ': lambda   : self.place.append_say_o(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Речевой оповещатель СОУЭ радиоканальный': lambda: self.place.append_radio_say_o(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Световой оповещатель (табло «Выход»)': lambda   : self.place.append_exit(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Световой радиоканальный оповещатель (табло «Выход»)': lambda: self.place.append_radio_exit(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Пожарный кран с рукавом': lambda   : self.place.append_PK(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Пожарный щит': lambda   : self.place.append_pch(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Огнетушитель': lambda   : self.place.append_fire(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Оперативная связь': lambda   : self.place.append_phone(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Прибор управления СЭО с микрофоном': lambda   : self.place.append_soue_micro(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Световой оповещатель': lambda   : self.place.append_signalization(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Релейный блок': lambda   : self.place.append_rele_block(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Светозвуковой оповещатель': lambda   : self.place.append_svetozvuk(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Извещатель пож дымовой линейный': lambda   : self.place.append_lineiniy(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Извещатель пож тепловой': lambda   : self.place.append_temp(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Звуковой оповещатель (сирена)': lambda   : self.place.append_sirena(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Блок речевого оповещения СОУЭ': lambda   : self.place.append_soue(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Кнопка тревожной сигнализации': lambda   : self.place.append_kts(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Радиоприемник тревожной сигнализации ': lambda   : self.place.append_radio_sys(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Радиоприемник пожарной сигнализации': lambda   : self.place.append_radio_sys_fire(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Устройство оконечное объектовое СПИ': lambda   : self.place.append_spi(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Источник бесперебойного питания': lambda   : self.place.append_ibp(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Считыватель ключей ТМ': lambda   : self.place.append_TM(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Кнопка': lambda   : self.place.append_button(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Вызывная видеопанель видеодомофона': lambda   : self.place.append_panel_video(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Монитор видеодомофона ': lambda   : self.place.append_monitor_domofon(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Электромагнитный замок': lambda   : self.place.append_electro(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Механический доводчик': lambda   : self.place.append_dovodchik(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Извещатель охранный ИК пассивный «штора»': lambda   : self.place.append_stora(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Извещатель охранный акустический': lambda   : self.place.append_akustik(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Металлодетектор': lambda   : self.place.append_metal(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Металлодетектор стационарный (арочный)': lambda: self.place.append_ellipse_detector(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Извещатель охранный магнитоконтактный': lambda   : self.place.append_magnit(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Извещатель охранный ИК пассивный объемный': lambda   : self.place.append_obiem(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                "Извещатель совмещённый": lambda   : self.place.append_sovm(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Прожектор системы дежурного освещения': lambda   : self.place.append_projector(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Светильник системы дежурного освещения': lambda   : self.place.append_svet(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Шлагбаум': lambda   : self.place.append_shlakbaum(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Точка доступа': lambda   : self.place.append_TD(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Электромеханический замок': lambda   : self.place.append_electricity_zamok(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Речевой оповещатель СЭО': lambda   : self.place.append_say_SEO(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Объектовая станция РСПИ «ОС ПАК „Стрелец мониторинг“': lambda   : self.place.append_strelec_monitoring(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5, y= self.y + self.cell_height * .5),
                "Система дистанционного управления": lambda   : self.place.append_dist_system(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5, y= self.y + self.cell_height * .5),
                'Расширитель зон': lambda : self.place.append_more_radio(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5, y= self.y + self.cell_height * .5),
                'Турникет': lambda: self.place.append_turnstile(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5, y= self.y + self.cell_height * .5),
                'Кодонаборная панель': lambda: self.place.append_code_collection_panel(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5, y= self.y + self.cell_height * .5),
                'Панель вызова домофона': lambda: self.place.append_homecall_panel(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5, y= self.y + self.cell_height * .5),
                'Панель приёма домофона': lambda: self.place.append_accepter_homecall_panel(x=self.x + ((self.column - 1) * self.original_width)-self.width*.5 + self.first_cell[0] * .5, y= self.y + self.cell_height * .5)
                
                        }
        super().__init__(scene,self.width,self.height,self.cell_height)

    def vsdx_format(self, place,text):
        ''' Определение подписи 1 столба '''
        self.text = text
        self.second_text = 'Обозначение'


class Dangerous(Table):
    """ Класс таблицы ПОУ и КЭО"""
    def __init__(self,scene,elements,pos):
        self.type = 'Dangerous'
        self.default_pos = pos[0] + 800, pos[1] + 200
        self.color = 'red'
        self.width = 320.1237335205092
        self.height = 42.86667556386156 + 29.22727879354197
        self.first_cell = 72.0, 29.22727879354197
        self.second_cell = 248.1237335205092, 29.22727879354197
        self.cell_height = 19.48485252902798
        self.scene = scene
        self.original_elements = deepcopy(elements)
        self.objects = {
            'КЭО': lambda num: self.place.append_KEO(x=self.x + ((self.column - 1) * self.original_width) -self.width*.5 + self.first_cell[0] * .5, y=self.y + self.first_cell[1] * .33, num = num),
            'ПОУ': lambda num: self.place.append_POU(x=self.x + ((self.column - 1) * self.original_width) -self.width*.5 + self.first_cell[0] * .5, y=self.y + self.first_cell[1] * .33, num = num)
                        }
        super().__init__(scene,self.width,self.height,self.cell_height)

    def resize(self,row):
        """ Изменение размера таблицы """
        self.scene[0].removeItem(self.rect)
        self.height = self.original_height
        start = math.ceil(len(self.elements['all_table'])/row) if math.ceil(len(self.elements['all_table'])/row) != len(self.elements['all_table']) else 0
        column = 1
        for index_element in range(start,len(self.elements['all_table'])):
            if start != 0:
                if index_element + 1 - start * column > 0:
                    column += 1
            self.elements['all_table'][index_element][-1] = column
        self.width = self.original_width * row
        self.table_height()
        self.rect = self.scene[0].addRect(QRectF(float(self.x),float(self.y),self.width,self.height), QPen(QColor('black')), QBrush(QColor(self.color)))

    def table_height(self):
        self.rows_height = {i:0 for i in range(1,7)}
        for element in self.elements['all_table']:
            self.rows_height[element[-1]] += element[-2]
        self.height = max(self.rows_height.values())

    def cells_height(self):
        for index, element in enumerate(self.original_elements['all_table']):
            if len(element[0]) > self.max_sym:
                cell_height = self.cell_height * 1.51
            else:
                cell_height = self.cell_height
            self.elements['all_table'][index] = [element, cell_height, 1]
    
    def table_height(self):
        self.rows_height = {i:0 for i in range(1,7)}
        for element in self.elements['all_table']:
            self.rows_height[element[-1]] += element[-2]
        self.height = max(self.rows_height.values())


    def post(self):
        if len(self.original_elements['all_table']) > 0:
            self.elements = deepcopy(self.original_elements)
            self.cells_height()
            for row in range(1,6):
                self.width = self.original_width * row
                self.height = self.original_height
                if math.ceil(len(self.elements['all_table'])/row) >= 3:
                    start = math.ceil(len(self.elements['all_table'])/row) if math.ceil(len(self.elements['all_table'])/row) != len(self.elements['all_table']) else 0
                    column = 1
                    for index_element in range(start,len(self.elements['all_table'])):
                        if start != 0:
                            if index_element + 1 - start * column > 0:
                                column += 1
                        self.elements['all_table'][index_element][-1] = column
                    
                    if self.set_position() == True:
                        break
                    if row == 1:
                        elements = deepcopy(self.elements)
            else:
                self.elements = elements
                self.width = self.original_width
                self.height = self.original_height
                self.x, self.y = self.default_pos

            self.rect = self.scene[0].addRect(QRectF(float(self.x),float(self.y),self.width,self.height), QPen(QColor('black')), QBrush(QColor(self.color)))


    def add_header(self,file):
        try:
            self.x += self.width // 2

            try:
                self.file = file
                self.place.append_heading(x=self.x, y=self.y+self.cell_height*.5, width=self.width, height=self.cell_height*1.7, text=self.text)
                self.y -= self.cell_height * 1.7
                for self.column in range(int(self.elements[list(self.elements.keys())[-1]][-1][-1])):
                    self.place.append_title(x=self.x + ((self.column) * self.original_width) - self.width*.5 + self.first_cell[0]*.5, y = self.y + self.cell_height * .5, width= self.first_cell[0], height= self.cell_height*1.4, text= self.second_text)
                    self.place.append_title(x= self.x + ((self.column) * self.original_width) - self.width*.5 + self.first_cell[0] + self.second_cell[0] * .5, y = self.y + self.cell_height * .5, width= self.second_cell[0], height= self.cell_height * 1.4, text= 'Наименование')
                self.y -= self.cell_height * .7
                self.y_firstRow = self.y
                self.add_table()
            except IndexError:
                print('ПОУ или КЭО отсутствуют')    
        except: 
            pass
        
    def add_table(self):
        """ Аналог родительского метода т.к. есть необходимость вызывать второй метод"""
        self.column = 1
        for i,self.line in enumerate(self.elements['all_table']):
            if self.line[-1] != self.column:
                self.y = self.y_firstRow
                self.column = self.line[-1]
            self.y -= self.line[1] * .5
            # Тут будет биться список с данными [значение,высота ячейки]
            self.place.append_rect(x=self.x + ((self.column - 1) * self.original_width) -self.width*.5 + self.first_cell[0] * .5, y = self.y + self.cell_height * .5, width= self.first_cell[0], height=self.cell_height)
            try:
                self.objects[self.line[0][0][:3]](self.line[0][1])
            except KeyError:
                print(self.line , ' не размещён') 
            self.place.append_rect(x=self.x + ((self.column - 1) * self.original_width) - self.width*.5 + self.first_cell[0] + self.second_cell[0] * .5, y = self.y + self.cell_height * .5, width= self.second_cell[0], height= self.cell_height, text=self.line[0][0][4:])
            self.y -= self.line[1] * .5
        
        self.change_elements_text()


    def change_elements_text(self):
        """ Меняет наименования размещённых пользователем ПОУ и КЭО в соответствии с нумерацией"""
        elements_in_file = self.elements[self.file]
        for key in elements_in_file.keys():
            for element in elements_in_file[key]:
                i = 0
                for elem in self.elements['all_table']:
                    if key == elem[0][0][:3:]:
                        i += 1
                        if elem[0][0] == element[2]:
                            break

                vsdx_elem = self.place.adress[element[1]][-1]
                if int(self.place.adress[element[1]].attrib['ID']) == int(element[0]):
                    if element[3] == 'text':
                        vsdx_elem.text = element[2][:4] + str(i)
                    elif element[3] == 'tail':
                        vsdx_elem[0].text = element[2][:4] + str(i)

                else:
                    print(f'Айди объекта не совпадает для изменения текста\n {self.file} \n {element}')

    

class Other_elements(Table):
    """ Класс таблицы остальных элементов(заборы, мусорки, решётки  итд)"""
    def __init__(self,scene,elements,pos):
        self.type = 'other_table'
        self.default_pos = pos[0] + 1050, pos[1] + 200
        self.color = 'green'
        self.width = 320.1237335205092
        self.height = 42.86667556386156 + 29.22727879354197
        self.first_cell = 72.0, 29.22727879354197
        self.second_cell = 248.1237335205092, 29.22727879354197
        self.cell_height = 19.48485252902798
        self.scene = scene
        self.original_elements = deepcopy(list(elements))
        self.elements = list(elements)
        self.objects = {
                'Мусорный бак': lambda   :self.place.append_trash(x=self.x + ((self.column - 1) * self.original_width) -self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Забор': lambda   :self.place.append_fence(x=self.x + ((self.column - 1) * self.original_width) -self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5),
                'Решётка': lambda   :self.place.append_grid(x=self.x + ((self.column - 1) * self.original_width) -self.width*.5 + self.first_cell[0] * .5,y= self.y + self.cell_height * .5)
                        }
        super().__init__(scene,self.width,self.height,self.cell_height)



def start_visualization():
    """ Запуск окна визуализации данных"""
    global window
    global sql
    global app
    window = MainWindow()
    info = window.create_dialog_menu()
    if not all_operations['Подсчёт'] and not all_operations['Transfer']:
        window.__init_main_win__(*info)
        window.thread().exec()
        window.get_rooms()
        vsdx_files = placement_of_objects.Visio_master(files, table_POU_KEO, window.get_rooms(),all_operations)  
        vsdx_files.post_tables()
    elif all_operations['Transfer']:
        """ Будет переброс инфы из ексель в ворд"""
        print(all_operations)
        xml_structV2.start(all_operations)
    print('мисион комплитед')
    app.exit()
    del app


if __name__ == '__main__':
    while 1:
        app = QApplication(sys.argv)
        start_visualization()