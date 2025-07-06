import xml.etree.ElementTree as ET

import shapes 
import custom_zipFile as zipfile
from visualization import Rooms, ITSO, Dangerous, Dangerous, Other_elements

class Visio_master:
    """ Форматирование vsdx документа"""    
    def __init__(self,files,table_POU_KEO,pos_tables,operations):
        self.files = files
        self.table_POU_KEO = table_POU_KEO
        self.pos_tables = pos_tables
        self.operations = operations
        self.width_excel = 1655.511811023622/6.672121959211056
        self.height_excel = 1169.291338582677/60.0102739726
        self.get_end_dir()
        
    def post_tables(self):
        for index_file, self.file in enumerate(self.files):
            self.start_cheme_name = len(self.file) - self.file[::-1].index('/')
            with zipfile.ZipFile(self.file, 'a') as zf:
                self.get_masters()
                # Извлечение содержимого XML файла  
                with zf.open('visio/pages/page1.xml') as f:
                    tree = ET.parse(f)
                    self.root = tree.getroot()[0]
                    self.place = shapes.Shapes(self.root,self.masters,self.file)
                    for table in self.pos_tables[self.file[self.start_cheme_name:-5]]:
                        if table.type == 'Rooms':
                            self.room = table
                        elif table.type == 'ITSO':
                            self.ITSO = table
                        elif table.type == 'Dangerous':
                            self.DANGEROUS = table
                        elif table.type == 'other_table':
                            self.table_elements = table

                    self.set_tables()
                    
                    ET.register_namespace("", 'http://schemas.microsoft.com/office/visio/2012/main')
                    xml_data = ET.tostring(tree.getroot(), encoding='unicode')
                
                self.reg_update(zf,xml_data)
                

    def reg_update(self,zf,xml_data):
        zf.remove('visio/pages/page1.xml')
        with zf.open('visio/pages/page1.xml', 'w') as f:
            f.write(xml_data.encode('utf-8'))
                    
    def set_tables(self):
        if self.operations['Экспликация']:
            self.room.vsdx_format(self.place, 'Экспликация помещений')
            self.room.add_header(self.file)
    
        if self.operations['ИТСО']:
            self.ITSO.vsdx_format(self.place, 'Условные графические обозначения ИТСО')
            self.ITSO.add_header(self.file)
        
        if self.operations['ПОУ и КЭО']:
            self.DANGEROUS.vsdx_format(self.place, 'Условные графические обозначения ПОУ и КЭО')
            self.DANGEROUS.add_header(self.file) 

    def get_end_dir(self):
        for i, sym in enumerate(self.files[0]):
            if sym == '/': 
                self.index_start_name = i+1

    def get_masters(self):
        """ Получение мастеров файла """
        with zipfile.ZipFile(self.file, 'a') as visio:
            self.masters = {}
            with visio.open('visio/masters/masters.xml', 'r') as masters:
                tree = ET.parse(masters)
                masters_root = tree.getroot()
                for name_element in masters_root:
                    try:
                        name_element = name_element.attrib
                        self.masters[name_element['Name']] = name_element['ID']
                    except KeyError as e:
                        print('Ошибка получения мастеров:', e)


