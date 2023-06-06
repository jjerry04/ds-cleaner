
from util.IO import IO

class Create(IO):
    '''
    Create folders and files. Files may have Data.
    Creating a new file will override old file.
    '''

    def __init__(self):
        super(Create, self).__init__()
        self.__fields = []

    def create(self, filename = '', data = []):
        '''
        Create files or folders. Specify file name,
        file path, and the data to store into the file. 
        Default parameters are set.
        '''
        if data == []:
            #create folder - may contain data
            self.createFolder(filename)
        else:
            #create folder - add new data
            self.createFile(filename, data)

    def createFolder(self, path=''):
        '''Creates folder path. May contain file
        '''
        self._setPath(path)
        self._initFolder()

    def createFile(self, filename='', data = [], field = [], header = False):
        '''
            Create folder path if path does not exist. 
            Create file with header, if header is true.
            If data is provided added data to file
        '''
        self._setPath(filename)
        #path = self._getPath()
        self._setFileName(filename)
        self._setData(data)
        self._setFiedNames(field)
        self._setCode('w')
        self._setHeader(header)
        self.__extractField(data)
        
        try:
           self._safeCreate()
           
        except (FileNotFoundError) as fileNotFound:
            self._initFolder()
            self.createFile(filename, data, field, header)
            print('File dir does not exist. New Dir created')

    def __extractField(self, data = []):
        '''Extract field from data'''
        if data is None:
           self.__extract()
        else:
            self.__extract(data)

    def __extract(self, data = []):
        data = self._getData()
        fieldnames = self._getFieldName()

        for number, asset in enumerate(data):
            if number < 1:
                for num, field in enumerate(asset):
                    fieldnames.append(field)
        self._setFiedNames(fieldnames)
                        

    
       

    