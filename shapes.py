import xml.etree.ElementTree as ET


class Append_Element(ET.Element):
    """
    Создан для добавления элементов в xml структуру vsdx файла
    Предварительно используется для создания таблицы обозначения в документе.
    """
    def __init__(self, tag: str, attrib: dict[str, str] = ..., **extra: str) -> None:
        super().__init__(tag, attrib, **extra)
    
    def add_child(self, *args):
        child = Append_Element(*args)
        self.append(child)
        return child
    
class Sql:
    def __init__(self):
        print('класс - заглушка т.к. переосмысляю необходимость кеширования элементов')
    
    def cashe(self, *args):
        pass
    
class Shapes():
    """Набор и добавление фигур. Лучше обратиться к коду файла"""
    def __init__(self,adress,masters,file) -> None:
        self.adress = adress
        self.lost_id = 0
        self.sql = Sql()
        self.file = file
        try:
            for id,line in enumerate(self.adress[-1]):
                if line.tag[53::] == 'Shapes':
                    if self.adress[-1][id][-1].tag[53::] == 'Shapes':
                        for i,line in enumerate(self.adress[-1][id][-1][0]):
                            self.lost_id = int(self.adress[-1][id][-1][0][i].attrib['ID'])
                        break
                    else: 
                        self.lost_id = int(self.adress[-1][id][-1].attrib['ID'])
            if self.lost_id == 0:
                self.lost_id = int(self.adress[-1].attrib['ID'])
        except TypeError:
            self.lost_id = int(self.adress[-1].attrib['ID'])
        
        self.masters = masters
        self.lost_id += 2000

    def append_kvadrat(self,x = None, y = None, width = None, height = None, text = None):
        #вход в дерево 1
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id,'Квадратная ячейка', "Таблица")
        el = Append_Element('Shape', {'ID':f'{self.lost_id}', 'Type':'Shape', 'LineStyle':'3', 'FillStyle':'3', 'TextStyle':'3'})
        self.adress.append(el)
        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': f'{width}'})
        child = el.add_child('Cell', {'N': 'Height', 'V': f'{height}'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': f'{width*.5}', 'F': 'Width*0.5'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': f'{height*.5}', 'F': 'Height*0.5'})
        child = el.add_child('Cell', {'N': 'Angle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LineWeight', 'V': '0.01666666666666667'})
        child = el.add_child('Cell', {'N': 'LineColor', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LinePattern', 'V': '1'})
        child = el.add_child('Cell', {'N': 'Rounding', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LineCap', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LineColorTrans', 'V': '0'})
        child = el.add_child('Cell', {'N': 'CompoundType', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LeftMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'RightMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'TopMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'BottomMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'FillForegnd', 'V': '1'})
        child = el.add_child('Cell', {'N': 'FillBkgnd', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FillPattern', 'V': '1'})
        child = el.add_child('Cell', {'N': 'ShdwForegnd', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShdwPattern', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FillForegndTrans', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FillBkgndTrans', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShdwForegndTrans', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShapeShdwType', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShapeShdwOffsetX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShapeShdwOffsetY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShapeShdwObliqueAngle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShapeShdwScaleFactor', 'V': '1'})
        child = el.add_child('Cell', {'N': 'ShapeShdwBlur', 'V': '0'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '0.02'})
        child = el.add_child('Section', {'N': 'Character'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'Font', 'V': 'Century Gothic'})
        pragrandson = grandson.add_child('Cell', {'N': 'Color', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Style', 'V': '34'})
        pragrandson = grandson.add_child('Cell', {'N': 'Size', 'V': '0.1944444444444444', 'U': 'PT'})
        pragrandson = grandson.add_child('Cell', {'N': 'AsianFont', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'ComplexScriptFont', 'V': 'Arial'})
        child = el.add_child('Section', {'N': 'Paragraph'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'IndLeft', 'V': '0.1968503937007874'})
        pragrandson = grandson.add_child('Cell', {'N': 'HorzAlign', 'V': '0'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0', 'F': 'No Formula'})
        grandson = child.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': f'{width*0}', 'F': 'Width*0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': f'{height*0}', 'F': 'Height*0'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': f'{width*1}', 'F': 'Width*1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Height*0'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': f'{width*1}', 'F': 'Width*1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': f'{height*1}', 'F': 'Height*1'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': f'{width*0}', 'F': 'Width*0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': f'{height*1}', 'F': 'Height*1'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '5'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Geometry1.X1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Geometry1.Y1'})
        child = el.add_child('Text', {})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('cp', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        grandson = child.add_child('pp', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson.tail = text


    def append_number_room(self, x = None, y = None, text = None, master = None):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, 'Нумерация', "Чертёж")
        # ЭТО РУЧНОЙ ВВОД
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Нумерация', 'Name': 'Нумерация', 'Type': 'Shape', 'Master': f'{self.masters['Нумерация']}'})
        self.adress.append(el)

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Text', {})
        child.text = text
        
    def append_cam(self, x = None, y = None, width = None, height = None, text = None, master = None):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Камера", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'Type': 'Shape', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '22.98364262867074'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '10.26532192233901'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '11.49182131433537', 'F': 'Width*0.5'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '5.132660961169506', 'F': 'Height*0.5'})
        child = el.add_child('Cell', {'N': 'Angle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FillForegnd', 'V': '#00b0f0', 'F': 'THEMEGUARD(RGB(0,176,240))'})
        child = el.add_child('Cell', {'N': 'FillBkgnd', 'V': '#2dc6ff', 'F': 'THEMEGUARD(SHADE(FillForegnd,LUMDIFF(THEME("FillColor"),THEME("FillColor2"))))'})
        child = el.add_child('Section', {'N': 'Character'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'Font', 'V': 'Century Gothic'})
        pragrandson = grandson.add_child('Cell', {'N': 'Style', 'V': '34'})
        pragrandson = grandson.add_child('Cell', {'N': 'Size', 'V': '0.1944444444444444', 'U': 'PT'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.1111099567737729'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '1.571151012346546E-6'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.7777775071713282'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '1.571151012346546E-6'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.7777775071713282'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.9999999732240177'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.1111099567737729'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.9999999732240177'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '5'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.1111099567737729'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '1.571151012346546E-6'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '1'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.7777774891934469'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.5000007855755062'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '1'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '1.571151012346546E-6'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.7777774891934469'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.5000007855755062'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '2'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '1'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.1111099567737778'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.5000007855755062'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '-1.301625814743227E-6'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.5000007855755062'})




    def append_videoreg(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Видеорегистратор", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Видеорегистратор', 'Name': 'Видеорегистратор', 'Type': 'Group', 'Master': f'{self.masters['Видеорегистратор']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson

    def append_monitor(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Видеомонитор", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Видеомонитор', 'Name': 'Видеомонитор', 'Type': 'Group', 'Master': f'{self.masters['Видеомонитор']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson


    def append_WIFI(self, x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "WI-FI-роутер", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'WI-FI-роутер', 'Name': 'WI-FI-роутер', 'Type': 'Group', 'Master': f'{self.masters['WI-FI-роутер']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 3
        pragrandson = grandson
    
    
    def append_ibp_220(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Источник бесперебойного питания типа UPS", "Таблица ИТСО")
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Источник бесперебойного питания типа UPS', 'Name': 'Источник бесперебойного питания типа UPS', 'Type': 'Shape', 'Master': f'{self.masters['Источник бесперебойного питания типа UPS']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})


    
    def append_bki(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Блок контроля и индикации", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Блок контроля и индикации', 'Name': 'Блок контроля и индикации', 'Type': 'Group', 'Master': f'{self.masters['Блок контроля и индикации']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '12'})
        #вход в дерево 3
        pragrandson = grandson


    def append_pku(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Пульт контроля и управления", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Пульт контроля и управления', 'Name': 'Пульт контроля и управления', 'Type': 'Group', 'Master': f'{self.masters['Пульт контроля и управления']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson



    def append_PPKOP(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "ППКОП (контроллер) системы ОПС ", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'ППКОП (контроллер) системы ОПС ', 'Name': 'ППКОП (контроллер) системы ОПС ', 'Type': 'Group', 'Master': f'{self.masters['ППКОП (контроллер) системы ОПС ']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson


    def append_smoker(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Извещатель пож. дымовой", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель пож. дымовой ', 'Name': 'Извещатель пож. дымовой ', 'Type': 'Group', 'Master': f'{self.masters['Извещатель пож дымовой ']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson

    def append_radio_smoker(self,x,y):
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель пож дымовой радиоканальный', 'Name': 'Извещатель пож дымовой радиоканальный', 'Type': 'Shape', 'Master': f'{self.masters['Извещатель пож дымовой радиоканальный']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})



    def append_rpi(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Извещатель пож. ручной", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель пож. ручной', 'Name': 'Извещатель пож. ручной', 'Type': 'Group', 'Master': f'{self.masters['Извещатель пож ручной']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson

    def append_radio_rpi(self,x,y):
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель пож ручной радиоканальный', 'Name': 'Извещатель пож ручной радиоканальный', 'Type': 'Shape', 'Master': f'{self.masters['Извещатель пож ручной радиоканальный']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})

    def append_radio_say_o(self,x,y):
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Речевой оповещатель СОУЭ радиоканальный', 'Name': 'Речевой оповещатель СОУЭ радиоканальный', 'Type': 'Shape', 'Master': f'{self.masters['Речевой оповещатель СОУЭ радиоканальный']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})



    def append_say_o(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Речевой оповещатель", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Речевой оповещатель', 'Name': 'Речевой оповещатель', 'Type': 'Group', 'Master': f'{self.masters['Речевой оповещатель СОУЭ']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 3
        pragrandson = grandson


    def append_exit(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Световой оповещатель (табло «Выход»)", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Световой оповещатель (табло «Выход»).308', 'Name': 'Световой оповещатель (табло «Выход»).308', 'Type': 'Shape', 'Master': f'{self.masters['Световой оповещатель (табло «Выход»)']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})


    def append_radio_exit(self,x,y):
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Световой радиоканальный оповещатель (табло «Выход»)', 'Name': 'Световой радиоканальный оповещатель (табло «Выход»)', 'Type': 'Shape', 'Master': f'{self.masters['Световой радиоканальный оповещатель (табло «Выход»)']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})


    def append_PK(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, 'Пожарный крас с рукавом', "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Пожарный кран с рукавом', 'Name': 'Пожарный кран с рукавом', 'Type': 'Foreign', 'Master': f'{self.masters['Пожарный кран с рукавом']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})


    def append_pch(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Пожарный щит", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Пожарный щит', 'Name': 'Пожарный щит', 'Type': 'Shape', 'Master': f'{self.masters['Пожарный щит']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})


    def append_fire(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Огнетушитель", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Огнетушитель', 'Name': 'Огнетушитель', 'Type': 'Foreign', 'Master': f'{self.masters['Огнетушитель']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})


    def append_phone(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Оперативная связь", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Оперативная связь', 'Name': 'Оперативная связь', 'Type': 'Foreign', 'Master': f'{self.masters['Оперативная связь']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})


    def append_soue_micro(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Прибор управления СЭО с микрофоном", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Прибор управления СЭО с микрофоном', 'Name': 'Прибор управления СЭО с микрофоном', 'Type': 'Group', 'Master': f'{self.masters['Прибор управления СЭО с микрофоном']}'})  
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Group', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Shapes', {})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Foreign', 'MasterShape': '11'})
        #вход в дерево 3
        pragrandson = grandson


    def append_soue(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Блок речевого оповещения СОУЭ", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Блок речевого оповещения СОУЭ', 'Name': 'Блок речевого оповещения СОУЭ', 'Type': 'Group', 'Master': f'{self.masters['Блок речевого оповещения СОУЭ']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson


    def append_signalization(self, x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Световой оповещатель", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Световой оповещатель', 'Name': 'Световой оповещатель', 'Type': 'Group', 'Master': f'{self.masters['Световой оповещатель']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '16.53547342139314'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '11.14751017172572'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '8.267736710696569', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '5.573755085862861', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '50'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '8.360632628794285', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '11.14751017172577', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '11.14751017172572', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '5.573755085862885', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Ellipse', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '5.573755085862885', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '11.14751017172577', 'U': 'DL', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '5.573755085862861', 'U': 'DL', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '5.573755085862885', 'U': 'DL', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '11.14751017172572', 'U': 'DL', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '1'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '5.573755085862885', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '8.918008137380616', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '8.918008137380578', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '2'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '5.573755085862885', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.786877542931443', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '2.786877542931431', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.786877542931443', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '2.786877542931431', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.043710198149687', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '2.043710198149678', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '8.360632628794285', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.573755085862972', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '6.874297939230993', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '6.8742979392309', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '3.437148969615496', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '3.43714896961545', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.874297939230925', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '3.437148969615496', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '3.43714896961545', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '6.874297939230831', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '1.393438771465742', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.57375508586275', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '2.786877542931484', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '1.393438771465742', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '2.786877542931484', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '5.57375508586275', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '5.57375508586275', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Connection'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Connection', 'IX': '0'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.786877542931484', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.786877542931484', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '15.23493056802511', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '2.601085706736052', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '1.300542853368026', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '13.93438771465709', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndX', 'V': '16.53547342139314', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Connection'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Connection', 'IX': '0'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.786877542931559', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.601085706736052', 'F': 'Inh'})


    def append_rele_block(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Релейный блок", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Релейный блок', 'Name': 'Релейный блок', 'Type': 'Group', 'Master': f'{self.masters['Релейный блок']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '27.82152230971131'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '10.98217985909653'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '13.91076115485565', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '5.491089929548266', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '50'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '13.72772482387074', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '21.96435971819324', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '10.98217985909653', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '10.98217985909662', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '21.96435971819324', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '21.96435971819324', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '10.98217985909653', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '10.98217985909653', 'F': 'Inh'})
        
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '10.98217985909676', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.863862411935332', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '16.47326978864472', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '2.745544964774133', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '8.236634894322361', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '1.372772482387066', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '5.491089929548186', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '16.47326978864472', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '2.745544964774133', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '20.59158723580611', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '8.236634894322222', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '4.118317447161111', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '16.473269788645', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndX', 'V': '24.70990468296722', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '8.236634894322222', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '1.372772482387161', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '2.745544964774198', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '1.372772482387099', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '2.745544964774259', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Connection'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Connection', 'IX': '0'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.745544964774198', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.745544964774198', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '26.26571349633927', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '3.111617626744085', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '1.555808813372043', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '24.70990468296722', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndX', 'V': '27.82152230971131', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '5.491089929548266', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Connection'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Connection', 'IX': '0'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.745544964774191', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '3.111617626744085', 'F': 'Inh'})


    
    def append_svetozvuk(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Светозвуковой оповещатель", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Светозвуковой оповещатель', 'Name': 'Светозвуковой оповещатель', 'Type': 'Group', 'Master': f'{self.masters['Светозвуковой оповещатель']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '16.53547342139314'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '11.14751017172572'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '8.267736710696569', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '5.573755085862861', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '50'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '8.360632628794285', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '11.14751017172577', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '11.14751017172572', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '5.573755085862885', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '11.14751017172577', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '11.14751017172577', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '11.14751017172572', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '11.14751017172572', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '8.360632628794285', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '11.14751017172577', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '11.14751017172572', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '5.573755085862885', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Ellipse', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '5.573755085862885', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '11.14751017172577', 'U': 'DL', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '5.573755085862861', 'U': 'DL', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '5.573755085862885', 'U': 'DL', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '11.14751017172572', 'U': 'DL', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '1'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '5.573755085862885', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '8.918008137380616', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '8.918008137380578', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '2'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '5.573755085862885', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.786877542931443', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '2.786877542931431', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.786877542931443', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '2.786877542931431', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.043710198149687', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '2.043710198149678', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '8.360632628794285', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.573755085862972', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '6.874297939230993', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '6.8742979392309', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '3.437148969615496', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '3.43714896961545', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.874297939230925', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '3.437148969615496', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '3.43714896961545', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '6.874297939230831', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '1.393438771465742', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.57375508586275', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '2.786877542931484', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '1.393438771465742', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '2.786877542931484', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '5.57375508586275', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '5.57375508586275', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Connection'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Connection', 'IX': '0'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.786877542931484', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.786877542931484', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '15.23493056802511', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '2.601085706736052', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '1.300542853368026', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '13.93438771465709', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndX', 'V': '16.53547342139314', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '5.573755085862861', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Connection'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Connection', 'IX': '0'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.786877542931559', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.601085706736052', 'F': 'Inh'})


    def append_lineiniy(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Извещатель пож дымовой линейный", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель пож дымовой линейный', 'Name': 'Извещатель пож дымовой линейный', 'Type': 'Shape', 'Master': f'{self.masters['Извещатель пож дымовой линейный']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})





    def append_temp(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Извещатель пож. тепловой", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель пож. тепловой', 'Name': 'Извещатель пож. тепловой', 'Type': 'Group', 'Master': f'{self.masters['Извещатель пож тепловой']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '17.58534218779732'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '11.22468650284934'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '8.792671093898662', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '5.612343251424671', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '50'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '8.792671093898662', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.612343251424671', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '11.22468650284926', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '11.22468650284934', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '5.612343251424629', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '5.612343251424671', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '11.22468650284926', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '11.22468650284926', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '11.22468650284934', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '11.22468650284934', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '8.792671093898662', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.612343251424671', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '5.612343251424671', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '2.806171625712335', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '8.792671093898662', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '8.418514877137007', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndX', 'V': '8.792671093898662', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '2.806171625712336', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '5.612343251424671', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '8.792671093898662', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '3.50771453214042', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '1.028929596094518', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '1.403085812856056', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '0.5144647980472591', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '0.7015429064280278', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.8418514877137089', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.09353905419039026', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '1.309546758665675', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1.028929596094518', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '1.403085812856056', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '5'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.8418514877137089', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '1.590163921237016', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.612343251424671', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '3.180327842474032', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '1.590163921237016', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '3.180327842474032', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '5.612343251424671', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '5.612343251424671', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '3.180327842474032', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '15.99517826656031', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '5.612343251424671', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '3.180327842474032', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '1.590163921237016', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '14.40501434532329', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '5.612343251424671', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndX', 'V': '17.58534218779732', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '5.612343251424671', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Connection'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Connection', 'IX': '0'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.806171625712411', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '3.180327842474032', 'F': 'Inh'})

# дебаг
    def append_sirena(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Сирена(ВЕРОЯТНО СЭО)", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'Type': 'Shape', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3', 'UniqueID': '{1C3453F8-F062-404E-9A69-EB525A7DFDA6}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '14.1732177734375'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '14.1732177734375'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '7.08660888671875', 'F': 'Width*0.5'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '7.08660888671875', 'F': 'Height*0.5'})
        child = el.add_child('Cell', {'N': 'Angle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LineWeight', 'V': '0.01666666666666667'})
        child = el.add_child('Cell', {'N': 'LineColor', 'V': '#ff0000', 'F': 'THEMEGUARD(RGB(255,0,0))'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'Ellipse', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '7.086597804072653', 'F': 'Width*0.49999921805716'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '7.08655602673764', 'F': 'Height*0.49999627043188'})
        pragrandson = grandson.add_child('Cell', {'N': 'A', 'V': '14.17323196316079', 'U': 'DL', 'F': 'Width*1.0000010011646'})
        pragrandson = grandson.add_child('Cell', {'N': 'B', 'V': '7.08655602673764', 'U': 'DL', 'F': 'Height*0.49999627043188'})
        pragrandson = grandson.add_child('Cell', {'N': 'C', 'V': '7.086597804072653', 'U': 'DL', 'F': 'Width*0.49999921805716'})
        pragrandson = grandson.add_child('Cell', {'N': 'D', 'V': '14.17319018582577', 'U': 'DL', 'F': 'Height*0.99999805353928'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '1'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.1901767531311631'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.6224173236834122'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.4401776446848593'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.6224173236834122'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.4401776446848593'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.372416432129716'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.1901767531311631'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.372416432129716'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '5'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.1901767531311631'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.6224173236834122'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '2'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '1'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.4401776513665957'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.6224173303651486'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.6901785548580847'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.8724182338566295'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '3'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '1'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.4401776513665957'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.372416432129708'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.6901785548580847'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.1224155286382271'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '4'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '1'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.6901785496020282'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.8724182286005811'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.6901785496020282'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.1224155371177247'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '5'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '1'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.3151772022488754'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.6224173303651486'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.3151772022488754'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.7474177761419967'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '6'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '1'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.3151772022488754'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.372416432129716'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.3151772022488754'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.2224158871044377'})


    def append_kts(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Кнопка тревожной сигнализации", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Кнопка тревожной сигнализации', 'Name': 'Кнопка тревожной сигнализации', 'Type': 'Group', 'Master': f'{self.masters['Кнопка тревожной сигнализации']}'})  
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Group', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Shapes', {})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Group', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Shapes', {})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '12'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '13'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '14'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2

    def append_more_radio(self,x,y):
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Расширитель зон', 'Name': 'Расширитель зон', 'Type': 'Group', 'Master': f'{self.masters['Расширитель зон']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson



    def append_radio_sys_fire(self,x,y):
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Радиоприемник пожарной сигнализации', 'Name': 'Радиоприемник пожарной сигнализации', 'Type': 'Shape', 'Master': f'{self.masters['Радиоприемник пожарной сигнализации']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})



    def append_radio_sys(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Радиоприёмник тревожной сигнализации", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Радиоприемник тревожной сигнализации ', 'Name': 'Радиоприемник тревожной сигнализации ', 'Type': 'Group', 'Master': f'{self.masters['Радиоприемник тревожной сигнализации ']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '12'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '13'})
        #вход в дерево 3
        pragrandson = grandson


    def append_spi(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Устройство оконечно объектовое СПИ", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Устройство оконечное объектовое СПИ', 'Name': 'Устройство оконечное объектовое СПИ', 'Type': 'Group', 'Master': f'{self.masters['Устройство оконечное объектовое СПИ']}', 'UniqueID': '{3385DA22-66A1-4222-89C7-C7E39535DAB0}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Group', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Shapes', {})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2



    
    def append_ibp(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Источник бесперебойного питания", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Источник бесперебойного питания', 'Name': 'Источник бесперебойного питания', 'Type': 'Group', 'Master': f'{self.masters['Источник бесперебойного питания']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 3
        pragrandson = grandson


    def append_TM(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Считыватель ключей ТМ", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Считыватель ключей ТМ', 'Name': 'Считыватель ключей ТМ', 'Type': 'Group', 'Master': f'{self.masters['Считыватель ключей ТМ']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson


    def append_button(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Кнопка", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Кнопка', 'Name': 'Кнопка', 'Type': 'Group', 'Master': f'{self.masters['Кнопка']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson

    def append_accepter_homecall_panel(self,x,y):
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Панель приёма домофона', 'Name': 'Панель приёма домофона', 'Type': 'Group', 'Master': f'{self.masters['Панель приёма домофона']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson



    def append_homecall_panel(self,x,y):
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Панель вызова домофона', 'Name': 'Панель вызова домофона', 'Type': 'Group', 'Master': f'{self.masters['Панель вызова домофона']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson


        
    def append_panel_video(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Вызывная видеопанель видеодомофона", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Вызывная видеопанель видеодомофона', 'Name': 'Вызывная видеопанель видеодомофона', 'Type': 'Group', 'Master': f'{self.masters['Вызывная видеопанель видеодомофона']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson


    def append_monitor_domofon(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Монитор видеодомофона", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Монитор видеодомофона ', 'Name': 'Монитор видеодомофона ', 'Type': 'Group', 'Master': f'{self.masters['Монитор видеодомофона ']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson


    def append_electro(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Электромагнитный замок", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Электромагнитный замок', 'Name': 'Электромагнитный замок', 'Type': 'Group', 'Master': f'{self.masters['Электромагнитный замок']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson


    def append_dovodchik(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Механический доводчик", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Механический доводчик', 'Name': 'Механический доводчик', 'Type': 'Group', 'Master': f'{self.masters['Механический доводчик']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson


    def append_stora(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Извещатель охранный ИК пассивный «штора»", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель охранный ИК пассивный «штора»', 'Name': 'Извещатель охранный ИК пассивный «штора»', 'Type': 'Group', 'Master': f'{self.masters['Извещатель охранный ИК пассивный «штора»']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '12.59842519684982'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '12.59842519684996'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '6.29921259842491', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '6.299212598424981', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '50'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '6.29921259842491', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.299212598425108', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '12.59842519684982', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '12.59842519684984', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '6.29921259842491', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '6.299212598424918', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519684982', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519684982', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519684984', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519684984', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '9.448818897637366', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.299212598424981', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '6.29921259842491', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '12.59842519684996', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '3.149606299212455', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '6.299212598424981', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.29921259842491', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519684984', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.29921259842491', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '6.299212598424981', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.29921259842491', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519684984', 'F': 'Inh'})


    def append_akustik(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Извещатель охранный акустический", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель охранный акустический', 'Name': 'Извещатель охранный акустический', 'Type': 'Group', 'Master': f'{self.masters['Извещатель охранный акустический']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '12.59842519685049'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '12.59842519685042'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '6.299212598425246', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '6.299212598425211', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '50'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '6.299212598425246', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.299212598425211', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '12.59842519685049', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '12.59842519685042', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '6.299212598425246', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '6.299212598425211', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519685049', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519685049', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519685042', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519685042', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '6.299212598425246', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.299212598425211', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '12.59842519685049', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '12.59842519685042', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '6.299212598425246', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '6.299212598425211', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519685049', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519685042', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519685042', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519685049', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519685042', 'F': 'Inh'})


    def append_metal(self,x,y):
        self.sql.cashe('added_elements', self.file,self.lost_id, "Металлодетектор", "Таблица ИТСО")
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Металлодетектор', 'Name': 'Металлодетектор', 'Type': 'Group', 'Master': f'{self.masters['Металлодетектор']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '9.56430474520916'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '15.74803149606297'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '4.78215237260458', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '7.874015748031483', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '50'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '4.507316029351425', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '7.874015748031483', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '6.596072238075253', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '15.74803149606297', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '3.298036119037627', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '7.874015748031483', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.596072238075253', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.596072238075253', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '15.74803149606297', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '15.74803149606297', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '3.71029063391736', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '9.842519685039354', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '1.594050790868225', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '11.81102362204723', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '0.7970253954341126', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '5.905511811023612', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1.594050790868209', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '11.81102362204723', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1.594050790868209', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '1.902887139107595', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '5.276857790460184', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '4.855643044619441', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '2.396735361912498', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '1.198367680956249', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '4.507316029351425', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '3.937007874015742', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndX', 'V': '6.046399551568943', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '5.77427821522314', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '2.396735361912498', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '0.6046399551569229', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '7.874015748031483', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '1.209279910313846', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '0.6046399551569229', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '1.209279910313846', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '7.874015748031483', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '7.874015748031483', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Connection'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Connection', 'IX': '0'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1.649018059518925', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1.209279910313846', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '8.684828446799129', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '7.874015748031483', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '1.758952596820062', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '0.8794762984100308', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '7.805352148389098', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '7.874015748031483', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndX', 'V': '9.56430474520916', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '7.874015748031483', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Connection'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Connection', 'IX': '0'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1.649018059518808', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1.758952596820062', 'F': 'Inh'})



    def append_magnit(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Извещатель охранный магнитоконтактный", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель охранный магнитоконтактный', 'Name': 'Извещатель охранный магнитоконтактный', 'Type': 'Group', 'Master': f'{self.masters['Извещатель охранный магнитоконтактный']}'}) 
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '12.59842519685044'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '12.59842519685058'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '6.299212598425221', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '6.299212598425288', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '50'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '6.299212598425221', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.299212598425414', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '12.59842519685044', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '12.59842519685045', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '6.299212598425221', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '6.299212598425225', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519685044', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519685044', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519685045', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.59842519685045', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '6.299212598425221', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '11.02362204724425', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '12.59842519685044', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '3.14960629921277', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '6.299212598425221', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '1.574803149606385', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519685044', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519685044', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '3.14960629921277', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '3.14960629921277', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '6.299212598425221', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '1.574803149606322', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '12.59842519685044', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '3.149606299212518', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '6.299212598425221', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '1.574803149606259', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519685044', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.59842519685044', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '3.149606299212518', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '3.149606299212518', 'F': 'Inh'})


    def append_obiem(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Извещатель охранный ИК пассивный объёмный", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель охранный ИК пассивный объемный', 'Name': 'Извещатель охранный ИК пассивный объемный', 'Type': 'Group', 'Master': f'{self.masters['Извещатель охранный ИК пассивный объемный']}'})  
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '12.40157480314974'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '12.40157480314967'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '6.20078740157487', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '6.200787401574836', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '50'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '6.200787401574746', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.200787401574836', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '12.40157480314962', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '12.40157480314967', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '6.200787401574808', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '6.200787401574836', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.40157480314962', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.40157480314962', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.40157480314967', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.40157480314967', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '6.200787401574746', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.200787401574836', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '12.40157480314974', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '12.40157480314967', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '6.20078740157487', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '6.200787401574836', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.40157480314974', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.40157480314967', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.20078740157487', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '6.200787401574836', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.40157480314974', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '5'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.40157480314967', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '6'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '12.40157480314974', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '12.40157480314967', 'F': 'Inh'})


    def append_sovm(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Извещатель совмещённый", "Таблица ИТСО")
        try:
            el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Извещатель совмещённый', 'Name': 'Извещатель совмещённый', 'Type': 'Group', 'Master': f'{self.masters['Извещатель совмещённый']}'}) 
        except: return 0
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson


# дебаг
    def append_projector(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Прожектор", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'Type': 'Group', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '21.65353393554688'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '13.32525634765625'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '10.82676696777344', 'F': 'Width*0.5'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '6.662628173828125', 'F': 'Height*0.5'})
        child = el.add_child('Cell', {'N': 'Angle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        child = el.add_child('Cell', {'N': 'DisplayLevel', 'V': '0'})
        child = el.add_child('Cell', {'N': 'QuickStyleVariation', 'V': '2'})
        child = el.add_child('Cell', {'N': 'FillForegnd', 'V': '#ffff00', 'F': 'THEMEGUARD(RGB(255,255,0))'})
        child = el.add_child('Cell', {'N': 'FillBkgnd', 'V': '#ffff3c', 'F': 'THEMEGUARD(SHADE(FillForegnd,LUMDIFF(THEME("FillColor"),THEME("FillColor2"))))'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '10.82676696777344', 'F': 'Sheet.1!Width*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.662628173828125', 'F': 'Sheet.1!Height*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '21.65353393554688', 'F': 'Sheet.1!Width*1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '13.32525634765625', 'F': 'Sheet.1!Height*1'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '10.82676696777344', 'F': 'Width*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '6.662628173828125', 'F': 'Height*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'Angle', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FillForegnd', 'V': '#ffff00', 'F': 'THEMEGUARD(RGB(255,255,0))'})
        pragrandson = grandson.add_child('Cell', {'N': 'FillBkgnd', 'V': '#ffff3c', 'F': 'THEMEGUARD(SHADE(FillForegnd,LUMDIFF(THEME("FillColor"),THEME("FillColor2"))))'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '-4.618963679928924E-7'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '-6.872899787171033E-7'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '-6.872899787171033E-7'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0.9999993558796451'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '-4.618963679928924E-7'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0.9999993558796451'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '5'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '-4.618963679928924E-7'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '-6.872899787171033E-7'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '1'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.3107512836532076'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0.818133082807571'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'EllipticalArcTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '15.09122567382053', 'F': 'Width*0.69694054184137'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '10.90183298043826', 'F': 'Height*0.81813307721887'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '10.91004458538345', 'U': 'DL', 'F': 'Width*0.50384591345957'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '12.63373491582559', 'U': 'DL', 'F': 'Height*0.94810445564507'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '0', 'U': 'DA'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '1', 'F': 'Width/Height*0.6153848322089'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'EllipticalArcTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '15.09122567381797', 'F': 'Width*0.69694054184125'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '2.564721291328056', 'F': 'Height*0.19247069057543'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '16.82312090353548', 'U': 'DL', 'F': 'Width*0.77692264706586'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '6.736948013581581', 'U': 'DL', 'F': 'Height*0.50557736660477'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '0', 'U': 'DA'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '1', 'F': 'Width/Height*0.6153848322089'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'EllipticalArcTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.728863466096868', 'F': 'Width*0.31075128365309'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '2.56472136579896', 'F': 'Height*0.19247069616414'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '10.91004455453395', 'U': 'DL', 'F': 'Width*0.50384591203489'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '0.8328194304116323', 'U': 'DL', 'F': 'Height*0.062499317737937'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '0', 'U': 'DA'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '1', 'F': 'Width/Height*0.6153848322089'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'EllipticalArcTo', 'IX': '5'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.716219147104539', 'F': 'Width*0.31016734575962'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '10.91440101361172', 'F': 'Height*0.819076251057'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '4.996968283717251', 'U': 'DL', 'F': 'Width*0.23076918061463'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '6.736948071997062', 'U': 'DL', 'F': 'Height*0.50557737098859'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '0', 'U': 'DA'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '1', 'F': 'Width/Height*0.6153848322089'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '13.86658610819524', 'F': 'Sheet.1!Width*0.64038443560622'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.7395611427728', 'F': 'Sheet.1!Height*0.50577347008849'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '5.913083150947045', 'F': 'Sheet.1!Width*0.27307704915732'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '8.349679702889489', 'F': 'Sheet.1!Height*0.62660555902612'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '2.956541575473523', 'F': 'Width*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '4.174839851444745', 'F': 'Height*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'Angle', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FillForegnd', 'V': '#ffff00', 'F': 'THEMEGUARD(RGB(255,255,0))'})
        pragrandson = grandson.add_child('Cell', {'N': 'FillBkgnd', 'V': '#ffff3c', 'F': 'THEMEGUARD(SHADE(FillForegnd,LUMDIFF(THEME("FillColor"),THEME("FillColor2"))))'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0.5007594650186719'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.7071067722811573'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'EllipticalArcTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '4.193825515585388', 'F': 'Width*0.7092451447962'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '8.34967970288676', 'F': 'Height*0.99999999999967'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '5.913076370813769', 'U': 'DL', 'F': 'Width*0.99999885336751'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '4.172226722253527', 'U': 'DL', 'F': 'Height*0.49968703839139'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '0', 'U': 'DA'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '1', 'F': 'Width/Height*1.4120687109824'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0.4977353348113104'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '7.953505872789151', 'F': 'Sheet.1!Width*0.36730752109394'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.733277210355936', 'F': 'Sheet.1!Height*0.50530188948599'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '5.913077468813015', 'F': 'Sheet.1!Width*0.27307678674593'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '8.337111689106337', 'F': 'Sheet.1!Height*0.62566238664315'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '2.956538734406507', 'F': 'Width*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '4.168555844553168', 'F': 'Height*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'Angle', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FillForegnd', 'V': '#ffff00', 'F': 'THEMEGUARD(RGB(255,255,0))'})
        pragrandson = grandson.add_child('Cell', {'N': 'FillBkgnd', 'V': '#ffff3c', 'F': 'THEMEGUARD(SHADE(FillForegnd,LUMDIFF(THEME("FillColor"),THEME("FillColor2"))))'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0.4984856510247389'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.2928925482291057'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '1'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'EllipticalArcTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1.731896327714196', 'F': 'Width*0.29289254822867'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Height*0'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '1.14533457917787E-6', 'U': 'DL', 'F': 'Width*1.936951756879E-7'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '4.172226706194238', 'U': 'DL', 'F': 'Height*0.50044030376202'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '0', 'U': 'DA'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '1', 'F': 'Width/Height*1.4099446071996'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.9999999874052092'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0.501514340042339'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '10.91004471545165', 'F': 'Sheet.1!Width*0.50384591946636'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '3.789360931417377', 'F': 'Sheet.1!Height*0.28437433641446'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '8.362361916739019', 'F': 'Sheet.1!Width*0.38618924475008'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '5.913083002013877', 'F': 'Sheet.1!Height*0.44375003735323'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '4.181180958369509', 'F': 'Width*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '2.956541501006939', 'F': 'Height*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'Angle', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FillForegnd', 'V': '#ffff00', 'F': 'THEMEGUARD(RGB(255,255,0))'})
        pragrandson = grandson.add_child('Cell', {'N': 'FillBkgnd', 'V': '#ffff3c', 'F': 'THEMEGUARD(SHADE(FillForegnd,LUMDIFF(THEME("FillColor"),THEME("FillColor2"))))'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.499999978148526'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '1'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0.2928932717136166'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'EllipticalArcTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '8.362361916735779', 'F': 'Width*0.99999999999961'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '1.731901860917674', 'F': 'Height*0.29289320990891'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '4.181180797451816', 'U': 'DL', 'F': 'Width*0.49999998075691'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '0', 'U': 'DL', 'F': 'Height*0'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '0', 'U': 'DA'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '1', 'F': 'Width/Height*0.70710680318411'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.499999978148526'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '1'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '10.91004442447002', 'F': 'Sheet.1!Width*0.50384590602829'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '9.677193414818248', 'F': 'Sheet.1!Height*0.72622943696842'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '8.362361916730436', 'F': 'Sheet.1!Width*0.38618924474968'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '5.913083002010581', 'F': 'Sheet.1!Height*0.44375003735299'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '4.181180958365218', 'F': 'Width*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '2.95654150100529', 'F': 'Height*0.5'})
        pragrandson = grandson.add_child('Cell', {'N': 'Angle', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'FillForegnd', 'V': '#ffff00', 'F': 'THEMEGUARD(RGB(255,255,0))'})
        pragrandson = grandson.add_child('Cell', {'N': 'FillBkgnd', 'V': '#ffff3c', 'F': 'THEMEGUARD(SHADE(FillForegnd,LUMDIFF(THEME("FillColor"),THEME("FillColor2"))))'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.5000000218509608'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0.7071067282867777'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'EllipticalArcTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Width*0'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '4.181181141096204', 'F': 'Height*0.70710679009148'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '4.18118111927862', 'U': 'DL', 'F': 'Width*0.50000001924258'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '5.913083002012628', 'U': 'DL', 'F': 'Height*1.0000000000003'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '0', 'U': 'DA'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '1', 'F': 'Width/Height*0.70710680318444'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '0.5000000218509608'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '0'})



    def append_svet(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Светильник системы дежурного освещения", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Светильник системы дежурного освещения', 'Name': 'Светильник системы дежурного освещения', 'Type': 'Group', 'Master': f'{self.masters['Светильник системы дежурного освещения']}'})  
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '13.97637795275568'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '13.97637795275562'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '6.988188976377842', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '6.988188976377808', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '1'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '6.988188976377842', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.988188976377808', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '13.97637795275568', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '13.97637795275562', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '6.988188976377842', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '6.988188976377808', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'Ellipse', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '6.988188976377842', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '6.988188976377808', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'A', 'V': '13.97637795275568', 'U': 'DL', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'B', 'V': '6.988188976377808', 'U': 'DL', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'C', 'V': '6.988188976377842', 'U': 'DL', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'D', 'V': '13.97637795275562', 'U': 'DL', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '7.013020741350706', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.963357211405224', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '9.833128096874427', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Height', 'V': '9.8331280968741', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '4.916564048437214', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinY', 'V': '4.91656404843705', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '9.8331280968741', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '1.397637795275576', 'F': 'Inh'})
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Y', 'V': '8.43549030159857', 'F': 'Inh'})
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '9.833128096874427', 'F': 'Inh'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'PinX', 'V': '6.963357211405257', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'PinY', 'V': '6.963357211405015', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Width', 'V': '13.90614311515162', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'LocPinX', 'V': '6.953071557575811', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginX', 'V': '11.87992125984233', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'BeginY', 'V': '11.87992125984227', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndX', 'V': '2.046793162968184', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'EndY', 'V': '2.046793162967755', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'X', 'V': '13.90614311515162', 'F': 'Inh'})


    def append_shlakbaum(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Шлагбаум", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Шлагбаум', 'IsCustomNameU': '1', 'Name': 'Шлагбаум', 'IsCustomName': '1', 'Type': 'Shape', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '65.40570068359375'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '13.58267211914063'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '32.70285034179688', 'F': 'Width*0.5'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '6.791336059570313', 'F': 'Height*0.5'})
        child = el.add_child('Cell', {'N': 'Angle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LineWeight', 'V': '0.01666666666666667'})
        child = el.add_child('Cell', {'N': 'LineColor', 'V': '#005124', 'F': 'THEMEGUARD(RGB(0,81,36))'})
        child = el.add_child('Cell', {'N': 'FillForegnd', 'V': '#96afcf', 'F': 'THEMEGUARD(THEME("FillColor"))'})
        child = el.add_child('Cell', {'N': 'FillBkgnd', 'V': '#ffffff', 'F': 'THEMEGUARD(RGB(255,255,255))'})
        child = el.add_child('Cell', {'N': 'FillPattern', 'V': '2'})
        child = el.add_child('Cell', {'N': 'RotateGradientWithShape', 'V': '0'})
        child = el.add_child('Section', {'N': 'Character'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'Font', 'V': 'Century Gothic'})
        pragrandson = grandson.add_child('Cell', {'N': 'Style', 'V': '34'})
        pragrandson = grandson.add_child('Cell', {'N': 'Size', 'V': '0.1944444444444444', 'U': 'PT'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.792331935389651'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '1.000000024647187'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '1.000000024647187'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '1.000000313093417'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.792331935389651'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '1.000000313093417'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '5'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.792331935389651'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '1'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '4.596168277469902E-7'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.3539404280353076'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.7915560975512571'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.3539404280353076'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0.7915560975512571'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.6437956103970113'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '4.596168277469902E-7'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.6437956103970113'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '5'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '4.596168277469902E-7'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0.3539404280353076'})


    def append_TD(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Точка доступа", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Точка доступа', 'Name': 'Точка доступа', 'Type': 'Group', 'Master': f'{self.masters['Точка доступа']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '12'})
        #вход в дерево 3
        pragrandson = grandson


    def append_electricity_zamok(self,x,y):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Электромеханический замок", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Электромеханический замок.258', 'Name': 'Электромеханический замок.258', 'Type': 'Group', 'Master': f'{self.masters['Электромеханический замок']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson



    def append_heading(self, x = None, y = None, width = None, height = None, text = None):
        # width = 320.1237335205092  'added_elements'
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file, self.lost_id, "Заголовок", "Таблица")
        el = Append_Element('Shape', {'ID':f'{self.lost_id}', 'Type':"Shape", 'LineStyle':"1", 'FillStyle':"1", 'TextStyle':"3"})
        self.adress.append(el)
        #вход в дерево 1
        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': f'{width}'})
        child = el.add_child('Cell', {'N': 'Height', 'V': f'{height}'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': f'{width*.5}', 'F': 'Width*0.5'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': f'{height*.5}', 'F': 'Height*0.5'})
        child = el.add_child('Cell', {'N': 'Angle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        child = el.add_child('Cell', {'N': 'EventDblClick', 'V': '0', 'F': 'OPENTEXTWIN()'})
        child = el.add_child('Cell', {'N': 'FillForegnd', 'V': '1'})
        child = el.add_child('Cell', {'N': 'FillBkgnd', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FillPattern', 'V': '1'})
        child = el.add_child('Cell', {'N': 'ShdwForegnd', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShdwPattern', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FillForegndTrans', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FillBkgndTrans', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShdwForegndTrans', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShapeShdwType', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShapeShdwOffsetX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShapeShdwOffsetY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShapeShdwObliqueAngle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ShapeShdwScaleFactor', 'V': '1'})
        child = el.add_child('Cell', {'N': 'ShapeShdwBlur', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LeftMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'RightMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'TopMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'BottomMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'LineWeight', 'V': '0.01666666666666667'})
        child = el.add_child('Cell', {'N': 'LineColor', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LinePattern', 'V': '0'})
        child = el.add_child('Cell', {'N': 'Rounding', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LineCap', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LineColorTrans', 'V': '0'})
        child = el.add_child('Cell', {'N': 'CompoundType', 'V': '0'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '0.02'})
        child = el.add_child('Section', {'N': 'Character'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'Font', 'V': 'Century Gothic'})
        pragrandson = grandson.add_child('Cell', {'N': 'Color', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Style', 'V': '51'})
        pragrandson = grandson.add_child('Cell', {'N': 'Size', 'V': '0.25', 'U': 'PT'})
        pragrandson = grandson.add_child('Cell', {'N': 'AsianFont', 'V': '0'})
        pragrandson = grandson.add_child('Cell', {'N': 'ComplexScriptFont', 'V': 'Arial'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0', 'F': 'No Formula'})
        grandson = child.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Width*0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Height*0'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson # заливка
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': f'{width}', 'F': 'Width*1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Height*0'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 3
        pragrandson = grandson # ЗАЛИВКА БЛЯТЬ
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': f'{width}', 'F': 'Width*1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': f'{height}', 'F': 'Height*1'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Width*0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': f'{height}', 'F': 'Height*1'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '5'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Width*0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Height*0'})
        child = el.add_child('Text', {})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('cp', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        grandson = child.add_child('pp', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson.tail = text


    def append_title(self, x = None, y = None, width = None, height = None, text = None):
        # width = 248.1237335205092
        # height = 29.22727879354197 
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Строка", "Таблица")
        el = Append_Element('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3', 'UniqueID': '{04C3928B-5544-4886-AF1B-DCDEAB1695A9}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': f'{width}'})
        child = el.add_child('Cell', {'N': 'Height', 'V': f'{height}'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': f'{width*.5}', 'F': 'Width*0.5'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': f'{height*.5}', 'F': 'Height*0.5'})
        child = el.add_child('Cell', {'N': 'Angle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LineWeight', 'V': '0.01666666666666667'})
        child = el.add_child('Cell', {'N': 'LeftMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'RightMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'TopMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'BottomMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Section', {'N': 'Character'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'Font', 'V': 'Century Gothic'})
        pragrandson = grandson.add_child('Cell', {'N': 'Style', 'V': '51'})
        pragrandson = grandson.add_child('Cell', {'N': 'Size', 'V': '0.1944444444444444', 'U': 'PT'})
        pragrandson = grandson.add_child('Cell', {'N': 'ComplexScriptFont', 'V': 'Arial'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0', 'F': 'No Formula'})
        grandson = child.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Width*0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Height*0'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': f'{width}', 'F': 'Width*1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Height*0'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': f'{width}', 'F': 'Width*1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': f'{height}', 'F': 'Height*1'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Width*0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': f'{height}', 'F': 'Height*1'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '5'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Geometry1.X1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Geometry1.Y1'})
        child = el.add_child('Text', {})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('cp', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson.tail = text


    def append_rect(self, x = None, y = None, width = None, height = None, text = ''):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Квадрат V2", "Таблица")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'Type': 'Shape', 'LineStyle': '3', 'FillStyle': '3', 'TextStyle': '3'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': f'{width}'})
        child = el.add_child('Cell', {'N': 'Height', 'V': f'{height}'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': f'{width*.5}', 'F': 'Width*0.5'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': f'{height*.5}', 'F': 'Height*0.5'})
        child = el.add_child('Cell', {'N': 'Angle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LineWeight', 'V': '0.01666666666666667'})
        child = el.add_child('Cell', {'N': 'LeftMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'RightMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'TopMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'BottomMargin', 'V': '0.02777777777777778', 'U': 'PT'})
        child = el.add_child('Cell', {'N': 'DropOnPageScale', 'V': '0.02'})
        child = el.add_child('Section', {'N': 'Character'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'Font', 'V': 'Century Gothic'})
        pragrandson = grandson.add_child('Cell', {'N': 'Style', 'V': '34'})
        pragrandson = grandson.add_child('Cell', {'N': 'Size', 'V': '0.1944444444444444', 'U': 'PT'})
        pragrandson = grandson.add_child('Cell', {'N': 'ComplexScriptFont', 'V': 'Arial'})
        # pragrandson = grandson.add_child('Cell', {'N': 'LangID', 'V': 'en-US'})
        child = el.add_child('Section', {'N': 'Paragraph'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'IndLeft', 'V': '0', "U":"CM"})
        pragrandson = grandson.add_child('Cell', {'N': 'IndRight', 'V': '0.1023622047244095', "U":"CM"})
        if text.isdigit():
            pragrandson = grandson.add_child('Cell', {'N': 'HorzAlign', 'V': '1'})
        else:
            pragrandson = grandson.add_child('Cell', {'N': 'HorzAlign', 'V': '2'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0', 'F': 'No Formula'})
        grandson = child.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Width*0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Height*0'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': f'{width}', 'F': 'Width*1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Height*0'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': f'{width}', 'F': 'Width*1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': f'{height}', 'F': 'Height*1'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '4'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Width*0'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': f'{height}', 'F': 'Height*1'})
        grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '5'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '0', 'F': 'Geometry1.X1'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '0', 'F': 'Geometry1.Y1'})
        child = el.add_child('Text', {})
        #вход в дерево 2
        grandson = child


        grandson = child.add_child('cp', {'IX': '0'})
        #вход в дерево 3
        grandson.tail = text


        
        # if text != None:
        #     child = el.add_child('Text', {})
        #     child = child.add_child('cp', {'IX': '0'})
        #     child.tail = text

# дебаг
    def append_KEO(self, x = None, y = None, num = 0):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "КЭО", "Таблица КЭО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'Type': 'Shape', 'Master': f'{self.masters['КЭО']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})

        child = el.add_child('Text', {})
        child.text = 'КЭО ' + str(num)



    def append_POU(self, x = None, y = None, master = 0, num = 0):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Область ПОУ", "Таблица ПОУ")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'Type': 'Shape', 'LineStyle': '16', 'FillStyle': '16', 'TextStyle': '16'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'Width', 'V': '39.9632568359375'})
        child = el.add_child('Cell', {'N': 'Height', 'V': '15.9715576171875'})
        child = el.add_child('Cell', {'N': 'LocPinX', 'V': '19.98162841796875', 'F': 'Width*0.5'})
        child = el.add_child('Cell', {'N': 'LocPinY', 'V': '7.98577880859375', 'F': 'Height*0.5'})
        child = el.add_child('Cell', {'N': 'Angle', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipX', 'V': '0'})
        child = el.add_child('Cell', {'N': 'FlipY', 'V': '0'})
        child = el.add_child('Cell', {'N': 'ResizeMode', 'V': '0'})
        child = el.add_child('Cell', {'N': 'LineWeight', 'V': '0.003333333333333334'})
        child = el.add_child('Cell', {'N': 'LineColor', 'V': '#262626', 'F': 'THEMEGUARD(TINT(RGB(0,0,0),36))'})
        child = el.add_child('Cell', {'N': 'FillForegnd', 'V': '#ff3c3c', 'F': 'THEMEGUARD(SHADE(FillBkgnd,LUMDIFF(THEME("FillColor"),THEME("FillColor2"))))'})
        child = el.add_child('Cell', {'N': 'FillBkgnd', 'V': '#ff0000', 'F': 'THEMEGUARD(RGB(255,0,0))'})
        child = el.add_child('Section', {'N': 'Character'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'Style', 'V': '17'})
        pragrandson = grandson.add_child('Cell', {'N': 'Size', 'V': '0.1944444444444444', 'U': 'PT'})
        child = el.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Cell', {'N': 'NoFill', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoLine', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoShow', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoSnap', 'V': '0'})
        grandson = child.add_child('Cell', {'N': 'NoQuickDrag', 'V': '0'})
        grandson = child.add_child('Row', {'T': 'RelMoveTo', 'IX': '1'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '4.184079099439719E-7'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '-6.509624981191568E-7'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '2'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '1.000000609318139'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '-6.509624981191568E-7'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '3'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '1.000000609318139'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '1.0000010806504'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '4'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '4.184079099439719E-7'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '1.0000010806504'})
        grandson = child.add_child('Row', {'T': 'RelLineTo', 'IX': '5'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '4.184079099439719E-7'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '-6.509624981191568E-7'})
        child = el.add_child('Text', {})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('cp', {'IX': '0'})
        #вход в дерево 3
        pragrandson = grandson

        # часть 2
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "ПОУ", "Таблица ПОУ")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'ПОУ.276', 'Name': 'ПОУ.276', 'Type': 'Shape', 'Master': f'{self.masters['ПОУ']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Text', {})
        child.text = 'ПОУ ' + str(num)


    def append_say_SEO(self, x = None, y = None, master = 0, num = 0):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Речевой оповещатель СЭО", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Речевой оповещатель СЭО', 'Name': 'Речевой оповещатель СЭО', 'Type': 'Group', 'Master': f'{self.masters['Речевой оповещатель СЭО']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 3
        pragrandson = grandson


    def append_strelec_monitoring(self, x = None, y = None, master = 0, num = 0):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, 'Объектовая станция РСПИ «ОС ПАК „Стрелец мониторинг“', "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Объектовая станция РСПИ «ОС ПАК „Стрелец мониторинг“', 'Name': 'Объектовая станция РСПИ «ОС ПАК „Стрелец мониторинг“', 'Type': 'Group', 'Master': f'{self.masters['Объектовая станция РСПИ «ОС ПАК „Стрелец мониторинг“']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Group', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Shapes', {})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2


    def append_dist_system(self, x = None, y = None, master = 0, num = 0):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Система дистанционного открытия дверей", "Таблица ИТСО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Система дистанционного открытия дверей', 'Name': 'Система дистанционного управления', 'Type': 'Group', 'Master': f'{self.masters['Система дистанционного управления']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Group', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Shapes', {})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Group', 'MasterShape': '12'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Shapes', {})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '13'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '14'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '15'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '16'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '17'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '18'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '19'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        self.lost_id += 1
        pragrandson_v2 = pragrandson.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '20'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2

    def append_ellipse_detector(self, x = None, y = None, master = 0, num = 0):
        print('Необходимо наладить вывод детектора')
        # self.lost_id += 1
        # el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Устройство досмотра (обнаружитель металла).102', 'Name': 'Металлодетектор стационарный (арочный)', 'Type': 'Shape', 'Master': f'{self.masters['Металлодетектор стационарный (арочный)']}'})
        # self.adress.append(el)
        # #вход в дерево 1

        # child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        # child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        # child = el.add_child('Cell', {'N': 'Width', 'V': '12.33595800524821'})
        # child = el.add_child('Cell', {'N': 'LocPinX', 'V': '6.167979002624104', 'F': 'Inh'})
        # child = el.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        # #вход в дерево 2
        # grandson = child

        # grandson = child.add_child('Row', {'T': 'MoveTo', 'IX': '1'})
        # #вход в дерево 3
        # pragrandson = grandson
        # pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '12.33595800524821', 'F': 'Inh'})
        # grandson = child.add_child('Row', {'T': 'LineTo', 'IX': '2'})
        # #вход в дерево 3
        # pragrandson = grandson
        # pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '12.33595800524821', 'F': 'Inh'})


    def append_turnstile(self,x,y):
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Турникет', 'Name': 'Турникет', 'Type': 'Shape', 'Master': f'{self.masters['Турникет']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})

    def append_code_collection_panel(self,x,y):
        self.lost_id += 1
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Кодонаборная панель', 'Name': 'Кодонаборная панель', 'Type': 'Group', 'Master': f'{self.masters['Кодонаборная панель']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 3
        pragrandson = grandson
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '12'})
        #вход в дерево 3
        pragrandson = grandson



    def append_trash(self, x = None, y = None, master = 0, num = 0):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Мусорный бак", "Таблица УГО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Мусорка', 'Name': 'Мусорка', 'Type': 'Shape', 'Master': f'{self.masters['Мусорный бак']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})


    def append_fence(self, x = None, y = None, master = 0, num = 0):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Забор", "Таблица УГО")
        el = Append_Element("Shape", {'ID': '1000', 'Type': 'Group', 'Master': f'{self.masters['Защитное ограждение']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}', 'F': 'Inh'})
        child = el.add_child('Cell', {'N': 'BeginX', 'V': '748.0314721900928'})
        child = el.add_child('Cell', {'N': 'BeginY', 'V': '610.236200997181'})
        child = el.add_child('Cell', {'N': 'EndX', 'V': '866.1417084105652'})
        child = el.add_child('Cell', {'N': 'EndY', 'V': '610.236200997181'})
        child = el.add_child('Cell', {'N': 'LayerMember', 'V': '1;4'})
        child = el.add_child('Cell', {'N': 'Comment', 'V': 'Забор', 'F': 'Inh'})
        child = el.add_child('Section', {'N': 'User'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'N': 'visBESelected'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'Value', 'V': '0'})
        grandson = child.add_child('Row', {'N': 'CleanupBegin'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'Value', 'V': '1358.267673187274', 'U': 'DL', 'F': 'Inh'})
        grandson = child.add_child('Row', {'N': 'CleanupEnd'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'Value', 'V': '1476.377909407746', 'U': 'DL', 'F': 'Inh'})
        child = el.add_child('Section', {'N': 'Scratch'})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Row', {'IX': '10'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'X', 'V': '866.1417084105652', 'F': 'Inh'})
        pragrandson = grandson.add_child('Cell', {'N': 'Y', 'V': '610.236200997181', 'F': 'Inh'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        grandson = child.add_child('Shape', {'ID': '1001', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'LayerMember', 'V': '1;4'})
        grandson = child.add_child('Shape', {'ID': '1002', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'LayerMember', 'V': '1;4'})
        grandson = child.add_child('Shape', {'ID': '1003', 'Type': 'Shape', 'MasterShape': '8'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'LayerMember', 'V': '1;4'})
        grandson = child.add_child('Shape', {'ID': '1004', 'Type': 'Shape', 'MasterShape': '9'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'LayerMember', 'V': '1;4'})
        grandson = child.add_child('Shape', {'ID': '1005', 'Type': 'Shape', 'MasterShape': '10'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'LayerMember', 'V': '1;4'})
        grandson = child.add_child('Shape', {'ID': '1006', 'Type': 'Shape', 'MasterShape': '11'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'LayerMember', 'V': '1;4'})
        pragrandson = grandson.add_child('Cell', {'N': 'HideText', 'V': '1', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'User'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Row', {'N': 'Hide'})
        #вход в дерево 5
        pragrandson_v3 = pragrandson_v2
        pragrandson_v3 = pragrandson_v2.add_child('Cell', {'N': 'Value', 'V': '1', 'U': 'BOOL', 'F': 'Inh'})
        pragrandson = grandson.add_child('Section', {'N': 'Geometry', 'IX': '0'})
        #вход в дерево 4
        pragrandson_v2 = pragrandson
        pragrandson_v2 = pragrandson.add_child('Cell', {'N': 'NoShow', 'V': '1', 'F': 'Inh'})



    def append_grid(self, x = None, y = None, master = 0, num = 0):
        self.lost_id += 1
        self.sql.cashe('added_elements', self.file,self.lost_id, "Решётка", "Таблица УГО")
        el = Append_Element("Shape", {'ID': f'{self.lost_id}', 'NameU': 'Решётка', 'Name': 'Решётка', 'Type': 'Group', 'Master': f'{self.masters['Решётка']}'})
        self.adress.append(el)
        #вход в дерево 1

        child = el.add_child('Cell', {'N': 'PinX', 'V': f'{x}'})
        child = el.add_child('Cell', {'N': 'PinY', 'V': f'{y}'})
        child = el.add_child('Cell', {'N': 'LayerMember', 'V': '1;4'})
        child = el.add_child('Cell', {'N': 'Comment', 'V': 'Решётка', 'F': 'Inh'})
        child = el.add_child('Shapes', {})
        #вход в дерево 2
        grandson = child

        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '6'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'LayerMember', 'V': '1;4'})
        self.lost_id += 1
        grandson = child.add_child('Shape', {'ID': f'{self.lost_id}', 'Type': 'Shape', 'MasterShape': '7'})
        #вход в дерево 3
        pragrandson = grandson
        pragrandson = grandson.add_child('Cell', {'N': 'LayerMember', 'V': '1;4'})

