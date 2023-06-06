
from base64 import encode
import csv
import os
from types import NoneType
from typing import Type

from requests import head

class IO:
    '''Base input/output class for
    C.R.U.D classes. The Create, Read, Update,
    and Delete classes can utilizes base fields 
    properties'''

    def __init__(self):
        super(IO, self).__init__()
        self.__fieldnames = []
        self.__filename = ''
        self.__path = ''
        self.__data = {}
        self.__code = ''
        self.__totalData = None
        self.__header = False

    def _setHeader(self, header):
        self.__header = header

    def _getHeader(self):
        return self.__header

    def _setDataRange(self, totalData):
        self.__totalData = totalData

    def _getDataRange(self):
        return self.__totalData

    def _setData(self, data):
        self.__data = data

    def _getData(self):
        return self.__data

    def _setFileName(self, filename):
        self.__filename = filename

    def _setFiedNames(self, fields):
        self.__fieldnames = fields

    def _setCode (self, code):
        self.__code = code

    def _getCode(self):
        return self.__code

    def _setPath(self, path = ''):
        self.__path = path

    def _getFileName(self):
        return self.__filename

    def _getFieldName(self):
        return self.__fieldnames

    def _getPath(self):
        return self.__path

############Default Implementation#################
    def _extractField(self, data = []):
        '''Loop through data structure. Extract keys,
        and fieldnames'''
        data = self._getData()
        fieldnames = []

        try:
            for number, asset in enumerate(data):
                dtype = type(data)
                #extract field from 1st data
                if number < 1 and dtype is list:
                    for num, field in enumerate(asset):
                        fieldnames.append(field)
                elif dtype is dict:
                    #for num, field in enumerate(asset):
                    fieldnames.append(asset)
        except TypeError:
            if TypeError is NoneType:
                print('No data to represent fields')
            print('Check Network')
        self._setFiedNames(fieldnames)

    def _setIOProperty(self,code='', filename='', data=[], header=False ):
        '''
        Override default properties.
        Read/Write code ('r', 'w','u'). Filename, data, and header.
        fieldnames are extracted from the data 
        '''
        self._setCode(code)
        self._setFileName(filename)
        self._setPath(filename)
        self._setData(data)
        self._extractField(data)
        self._setHeader(header)

    def _initFolder(self):
        '''Create folder/subfolders using path as directory'''
        path = self._getPath()
        os.makedirs(os.path.dirname(path), exist_ok = True)

    def _safeCreate(self):
        '''Safely create folder or file base on 
        code ('r', 'w', 'u' etc)'''
        code  = self._getCode()
        
        if code == 'w':
            self.__write()
            
        if code == 'a':
            self.__add()
    
    def _safeRead(self):
        '''Safely read file based on code ('r')'''
        code = self._getCode()
        if code == 'r':
            self.__read()

##########Private implementation################
    def __write(self):
        '''Get properties (path, field, code, header, data)
        required to write data to file. '''
        path = self._getPath()
        field = self._getFieldName()
        code = self._getCode()
        header = self._getHeader()
        data = self._getData()
        if type(data) is dict:
            listData = []
            listData.append(data)
            data = listData

        with open(path, code, encoding='utf-8') as file_obj:
            #open file
            writer = csv.DictWriter(file_obj, fieldnames=field)
            #write header in file
            if header is True and data != None:
                writer.writeheader()
                writer.writerows(data)
            if header is True and data is None:
                writer.writeheader()
            #write data in file
            if data == None:
                writer.writerows(data)

    def __read(self):
        '''Read entire csv file and set new data'''
        path = self._getPath()
        code = self._getCode()
        try:
            with open(path, code, encoding='utf-8') as file_obj:
                #open file
                reader = csv.DictReader(file_obj)
                #heading = next(file_obj)
                asset = self.__getRow(reader)
                self._setData(asset)
        except FileNotFoundError as fnf:
            self.__write()
            self._initFolder()
            print(f'{fnf} - new directory created.')

    def __getRow(self, reader):
        '''Read individual rows of file. Returns
            dictionary data per range. If range is 0
            return all data'''
        asset = []
        dataRange = self._getDataRange()
        totalData = 0

        for row in reader:
            if totalData < dataRange:
                asset.append(row)
                totalData += 1
            if totalData >= dataRange and totalData != 0:
                return asset
            if dataRange == 0:
                 asset.append(row)
        return asset

    def _dataCounter(self, data):
        '''Count total data in list'''
        counter = 0
        for count, key in enumerate(data):
            counter = count
        return counter

    def _appendData(self, data, record):
        '''Loop through dictionary key.
        returned new data'''
       
        for index, key in enumerate(data):
            record.append(key)
        return record
            
    def _exist(self, name, data):
        '''Loop through data and see if specific data exist'''
        exist = False
        for index, key in enumerate(data):
            try:
                assetName = self.lowerCase(key['name'])
                name = self.lowerCase(name)
                if assetName == name:
                    exist = True
                    return exist
            except TypeError:
                 return exist
        return exist
    
    def _search(self, name, data):
        '''Search a specific dataset for a single data. Return data'''
       
        #newRecord = []
        for index, key in enumerate(data):
            assetName = self.lowerCase(key['name'])
            if assetName == name:
                print(f'{name} exist and has been extracted from new data ')
                print(f'{name} - is ready to be added to new record')
                newRecord = key
                return newRecord
                
