import cv2 as cv
import numpy
from skimage.morphology import skeletonize
import numpy as np
from itertools import product

class Shape_room:
    """ Класс для определения присутствия помещения по контуру от стен"""
    def __init__(self,img, evacuation=False):
        global skelets

        self.img = img
        if evacuation:
            self.show_evacuation_way()
            
    def get_contours(self):
        """ Возврат списка фигур помещений"""
        self.prepare_image()
        self.get_rooms()
        return self.list_contours
    
            
    def prepare_image(self):
        """ Преобразование в серое изображение с дальнейшим отображением по трешхолдду для получения чётких контуров"""
        self.list_contours = []
        gray = cv.cvtColor(self.img,cv.COLOR_BGR2GRAY)
        _, self.threshold = cv.threshold(gray, 127, 255, cv.THRESH_BINARY)
            
    def get_rooms(self):
        """ Получение фигур помещений"""
        self.contours, _ = cv.findContours( 
        self.threshold, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        
        shapes_rooms = []
        for elem in self.contours:
            shapes_rooms.append(elem)
        
        self.delete_walls_as_rooms(shapes_rooms)
        self.list_contours.append(self.contours)
        
    def delete_walls_as_rooms(self, shapes):
        self.contours = shapes
        self.contours.pop(0)
        self.contours.pop(0)
    
    def show_evacuation_way(self):
        """ Ответвление для генерации путей эвакуации[В РАЗРАБОТКЕ]
        Всё что ниже - эксперимент"""
        self.contours.pop(0)

        skelets_original = self.skeletonize_walls(self.threshold)
        skelets = skelets_original.astype(np.uint8)
        
        skelets *= 255
        self.garbage_disposal()
        

        cv.imwrite('input.jpg', skelets)
        self.threshold = np.add(self.threshold,skelets_original.astype(np.uint8))
        cv.imwrite('inputthreshold.jpg', self.threshold)
        
        cv.imshow('th',self.threshold)
        cv.imshow('sk', skelets)
        
        cv.setMouseCallback('sk', self.get_line)
        

        while 1:
            cv.imshow('sk', skelets)
            cv.waitKey(0)

    def get_line(self,event,x,y,flags,param):
        """ Реализован на момент отладки для получения координат линий т.к. они не срастаются"""
        if event == cv.EVENT_LBUTTONDOWN:
            while skelets[y,x] == 0:
                y += 1
            for line in self.lines:
                if [y,x] in line.points:
                    line.get_cords()
        if event == cv.EVENT_RBUTTONDOWN:
            while skelets[y,x] == 0:
                x += 1
            for line in self.lines:
                if [y,x] in line.points:
                    line.get_cords()
    
    def garbage_disposal(self):
        """ Поиск линии пути для дальнейшего соединения в отрезки"""
        self.lines = []
        self.new_lines = []
        sy,sx = self.threshold.shape[:2]
        for y,x in product(range(sy-1), range(sx-1)):
            if skelets[y,x] > 150:
                self.search_lines(y,x)
                
        self.connect_diagonal_lines()
        
    def unvisible_deleted_lines(self):
        " Скрытие удалённых линий"
        for line in self.new_lines:
            for point in line.points:
                skelets[*point] = 0 
        
        
    def delete_wrong_lines(self):
        """ Удаляет несоединённые новые линии."""
        for line in self.new_lines:
            neigh = line.neighbors
            if None in neigh:
               self.lines.remove(line)
        
        self.unvisible_deleted_lines()
        del self.new_lines
        
    def update_neighbors(self):
        """ Переопределение соседних линий эвакуации """
        for line in self.lines:
            line.neighbors = line.get_new_neighbors(self.lines)
    
    def check_neighbors(self):
        """ Рекурсивная проверка всех соседей для определения разрыва линий"""
        for line in self.lines:
            line.check_neighbors(self.lines)
    
    def skip_diagonal_for_neighbor(self,diagonal_line):
        """ Метод ищет горизонтального\вертикального соседа """
        for neighbor in diagonal_line.neighbors:
            if 0 in neighbor.way:
                return neighbor
            
    def get_points(self, line):
        """ Превращение путей в прямые с соединением других линий кратным 45 град"""
        # добавить определение длины стартовых и конечных линий
        p1_neighbor, p2_neighbor = line.neighbors
        new_way = [None, None]
        alter_way = [None, None]
        
        inverse = False
        if p1_neighbor != None:
            if 0 not in p1_neighbor.way:
                p1_neighbor = self.skip_diagonal_for_neighbor(p1_neighbor)
            for point in [p1_neighbor.point1, p1_neighbor.point2]:
                    # if point in [[905, 427],[905, 446]]:
                    if [abs(w) for w in [np.array(line.point1) - np.array(point)][0].tolist()] == [abs(w) for w in line.way]:
                        newPoint = point
                        new_way = np.array(line.way) * np.array([abs(w) for w in p1_neighbor.way])
                        break
            else:
                newPoint = line.point1
                new_way = np.array(line.way) * np.array([abs(w) for w in p1_neighbor.way])
        else:
            newPoint = line.point1
        
        if p2_neighbor != None:
            if 0 not in p2_neighbor.way:
                p2_neighbor = self.skip_diagonal_for_neighbor(p2_neighbor)
            for point in [p2_neighbor.point1, p2_neighbor.point2]:
                # if point in [[905, 427],[905, 446]]:
                if [abs(w) for w in [np.array(line.point2) - np.array(point)][0].tolist()] == [abs(w) for w in line.way]:
                    alterpoint = point
                    alter_way = np.array(line.way) * np.array([abs(w) for w in p2_neighbor.way])
                    break
                        
            else:
                alterpoint = line.point2
                alter_way = np.array(line.way) * np.array([abs(w) for w in p2_neighbor.way])
        else:
            alterpoint = line.point2

        # if newPoint in [[886, 427], [905, 427]]:
        #     pass
        if None in new_way or None in alter_way:
            if None in new_way and None in alter_way:
                new_way = [line.way[0], 0] 
                alter_way = [0, line.way[1]]
            elif None in new_way:
                for index, w in enumerate(alter_way):
                    if w == 0:
                        new_way[index] = line.way[index]
                    else:
                        new_way[index] = 0
            elif None in alter_way:
                for index, w in enumerate(new_way):
                    if w == 0:
                        alter_way[index] = line.way[index]
                    else:
                        alter_way[index] = 0
                        
        difference = np.array(newPoint) - np.array(alterpoint)
        # определение направления, координат и кол-ва шагов нашей линии
        difference = [abs(p) if p != 0 else p for p in difference]
        y,x = newPoint
        success = True
        new_points = []
        """
{[990, 736]} [990, 851] правый верх
==================================================

[1012, 447] {[1012, 714]} левый низ
==================================================
        
        """
        if new_way.tolist() == alter_way.tolist():
            if newPoint == [990, 736] or [1012, 714] == alterpoint:
                raise Exception('Неисправленная ошибка с несоединённой линией')
                pass
            alter_way = alter_way[::-1]
        thisline = [[[y,x]],new_way]
        skelets[y,x] = 150
        new_points.append([y,x])
        
        for step in range(difference[0]):
            skelets[y,x] = 150
            y += new_way[0]
            x += new_way[1]
            new_points.append([y,x])
            if self.threshold[y,x] < 150:
                print('ERROR')
                success = False
                break
        skelets[y,x] = 150
        new_points.append([y,x])
        thisline[0].append([y,x])        
        thisline.append(new_points)
        thisline = GraphicalLine(*thisline)

        new_line = [[[y,x]], alter_way]
        new_line_points = []
        new_line_points.append([y,x])
        skelets[y,x] = 150
        for step in range(difference[1]):
            skelets[y,x] = 150
            y += alter_way[0]
            x += alter_way[1]
            new_line_points.append([y,x])
            if self.threshold[y,x] < 150:
                print('ERROR')
                success = False
                break
        skelets[y,x] = 150
        new_line_points.append([y,x])
        new_line[0].append([y,x])
        new_line.append(new_line_points)
        new_line = GraphicalLine(*new_line)

        thisline.neighbors[1] = new_line
        new_line.neighbors[0] = thisline
        self.lines.remove(line)
        line.active = False
        self.lines.append(thisline)
        self.lines.append(new_line)
        for point in line.points[1:-2]:
            skelets[*point] = 0
        
        # return thisline
        
    def repair_connect(self,y,x,alterpoint, line_way):
        way = [np.array(alterpoint) - np.array([y,x])][0].tolist()
        a,b = [int(abs(w)) for w in line_way[::-1]],  [abs(w) for w in way]
        if a == b:
            y,x = y + way[0], x + way[1]
            skelets[y,x] = 255
            return int(y), int(x), True                
        if [abs(w) for w in line_way] == [abs(w) for w in way]:
            y,x = y + way[0], x + way[1]
            skelets[y,x] = 255
            return int(y), int(x), True
        else:
            if sum(abs(wc) for wc in way) > 2:
                difference_y, difference_x = [abs(w) for w in way]
                way = np.array(way) // np.array(way)
            if 0 not in way:
                for _ in range(max([abs(difference_y), abs(difference_x)])):
                    if difference_y > 0:
                        difference_y -= 1
                        y += way[0]
                    if difference_x > 0:
                        difference_x -= 1
                        x += way[0]
                        skelets[y,x] = 255

                return int(y),int(x), False
            else:
                difference = max([abs(w) for w in way])
                for _ in range(difference):
                    y += way[0]
                    x += way[1]
                skelets[y,x] = 255

                return int(y),int(x), True
            
    def connect_diagonal_lines(self):
        self.lines = sorted(self.lines, key=lambda line: len(line.points))
        self.update_neighbors()
        # min_len = int(input('Минимальная длина пути для соединения:'))     
        min_len = 60   
        for index, line in enumerate(self.lines):
            if None in line.neighbors:
                line.WHERES_MY_NEIGHBOR(self.lines)
            if len(line.points) >= min_len: break
            if line.way[0] != 0 and line.way[1] != 0:
                self.get_points(line)
                # self.lines[index] = self.get_points(line[0][0],line[0][1],line[1],line[2])

        # self.update_neighbors()
        # self.check_neighbors()
        
        
    def search_lines(self,y,x):
        main_y, main_x = y,x
        step = None
        line = [[[y,x],[]], step]
        points = [[y,x]]
        skelets[y,x] = 200
        
        for step_y, step_x in product(range(-1,2),range(-1,2)):
            if (step_y, step_x) == (0,0): continue
            # if skelets[y+step_y,x+step_x] == 255:
            y,x = main_y, main_x
            step = [step_y, step_x]
            cycle = False

            while skelets[y+step_y,x+step_x] > 150:
                skelets[y,x] = 50
                cycle = True    
                y += step[0]
                x += step[1]
                points.append([y,x])
            if cycle:
                skelets[y,x] = 200
                line[1] = step 
                line[0][1] = [y,x]
                line.append(points)
                # points = [[y,x]]
                self.lines.append(GraphicalLine(*line))
                break


        
    def skeletonize_walls(self,threshold):
        skelet = skeletonize(threshold, method='lee')
        return skelet
  
     
class GraphicalLine:
    """ Объект маршрута эвакуации представляет собой отдельное направление линии до поворота """
    def __init__(self,stt_end, way,points):
        self.point1, self.point2 = stt_end
        if self.point1[0] < 0 or self.point1[1] < 0 or self.point2[0] < 0 or self.point2[1] < 0 :
            pass 
        self.way = way
        self.points = points
        self.neighbors = [None,None]
        self.active = True
    
    def get_closer_point(self,line):
        return min(abs(np.array(self.point1) - np.array(line.point1)), abs(np.array(self.point2) - np.array(line.point2)))

    def get_new_neighbors(self,lines):
        r = [None, None]
        for line in lines:
            if line is self: 
                continue
            
            if line.point1 == self.point1 or line.point2 == self.point1:
                r[0] = line
                if None not in r:
                    break
            if line.point1 == self.point2 or line.point2 == self.point2: # 
                r[1] = line
                if None not in r:
                    break
        return r
    
    def check_neighbors(self,lines):
        """ Ищет оборванные линии и отправляет на колизию в случае подтверждения обрыва"""
        original_way = self.way
        p1_neighbor = None
        p2_neighbor = None
        count_neighbors = 2 - self.neighbors.count(None)
        for index,neighbor in enumerate(self.neighbors):
            if neighbor is not None:
                for line in lines:
                    if line.point1 == neighbor.point1 or line.point2 == neighbor.point1:
                        p1_neighbor = line
                        if p2_neighbor is not None and count_neighbors + 1 >= 2:
                            break
                    if line.point1 == neighbor.point2 or line.point2 == neighbor.point2:
                        p2_neighbor = line
                        if p1_neighbor is not None and count_neighbors + 1 >= 2:
                            break
                if [type(p1_neighbor),type(p2_neighbor)] != list(map(lambda point: type(point),self.neighbors)):
                    difference = self.collision(lines)
                    if difference is None:
                        continue
                    if abs(difference):
                                              
                        self.update_line(abs(difference)-1)
                        self.way = original_way
                    """ меня куда то понесло. методы должны отвечать сами за себя, но никак не за другой объект
                        переосмыслить этот и последующие методы возможно neighbor следует заменить на self"""
                    
    def collision(self,lines):
        """ Проверяет на коллизию и в случае подтверждения обновляет линию """
        maxx = max(self.points[0][1], self.points[-1][1])
        minx = min(self.points[0][1], self.points[-1][1])
        maxy = max((self.points[0][0], self.points[-1][0]))
        miny = min((self.points[0][0], self.points[-1][0]))
        if maxx == minx:
            position = 'vertical'
        else:
            position = 'horizontal'
            
        for line in lines:
            anotherline_maxx = max(line.points[0][1], line.points[-1][1])
            anotherline_minx = min(line.points[0][1], line.points[-1][1])
            anotherline_maxy = max((line.points[0][0], line.points[-1][0]))
            anotherline_miny = min((line.points[0][0], line.points[-1][0]))
            if anotherline_maxx == anotherline_minx:
                """ Тут можно вычислить сколько точек нужно удалить """
                anotherline_position = 'vertical'
            else:
                anotherline_position = 'horizontal'
            if position != anotherline_position:
                if position == 'vertical':
                    if maxy > anotherline_maxy and miny < anotherline_miny:
                        if maxx < anotherline_maxx and maxx > anotherline_minx:
                            return miny - anotherline_maxy
                else:
                    if maxx > anotherline_maxx and minx < anotherline_minx:
                        if maxy < anotherline_maxy and maxy > anotherline_miny:
                            return minx - anotherline_maxx
                            
    def update_level_line(self,y,x):
        way = [abs(w) for w in self.way[::-1]]
        if way[0] == 0:
            for index, point in enumerate(self.points):
                skelets[*point] = 0
                self.points[index][0] = y
                skelets[*self.points[index]] = 255
        else:
            for index, point in enumerate(self.points):
                skelets[*point] = 0
                self.points[index][1] = x
                skelets[*self.points[index]] = 255
                                    
    def update_line(self,diff):
        """ Обновляет линию. Можно попробовать выебнуться тем как завернул перебор точек( имеет ввиду взять срез пойнтс с использованием диф)"""
        point1 = np.array(self.point1)
        for _ in range(diff):
            skelets[*point1] = 0
            self.points.remove(point1.tolist())
            point1 += self.way

        skelets[*point1] = 0
        self.points.remove(point1.tolist())
        point2 = point1.tolist()
        
    def get_cords(self):
        print(self.point1, self.point2)
        print('='*50, end='\n\n')

    def WHERES_MY_NEIGHBOR(self,lines):
        stt_end = [self.point1, self.point2]
        for index, neighbor in enumerate(self.neighbors):
            if neighbor is None:
                y,x = stt_end[index]
                for line in lines:
                        if None in line.neighbors:
                            for neighbor_point in [line.point1, line.point2]:
                                for self_point in [self.point1, self.point2]:
                                    if [abs(w) for w in [np.array(self_point) - np.array(neighbor_point)]][0].tolist() == [abs(w) for w in line.way]:
                                        self.neighbors[index] = line
                                    elif sum([[abs(w) for w in [np.array(self_point) - np.array(neighbor_point)]][0] - np.array([2,2])][0].tolist()) < 4:
                                        self.neighbors[index] = line