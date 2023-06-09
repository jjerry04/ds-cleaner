
import ast
from dscleaner.crud.create.Create import Create
from dscleaner.crud.read.Read import Read
from dscleaner.crud.update.Update import Update
from dscleaner.crud.delete.Delete import Delete

class Crud(Create, Read, Update, Delete):
    '''Initialize IO operations.
    Utilize C.R.U.D class for ArkFinance


    #Main directory is data by default. All csv file downloaded
    is added to data/category/[filename.csv].Implement ui
    to easily create folders and download directories.
    -Data
    --software_info.csv (example file)
    --category(directory)
        -crypto.csv (example file)
        -exchange.csv (example file)
        -realestateData (directory)
    --processed(directory)
        -realestate.csv
        -crypto.csv
    --test
        -TestData.csv
    '''
    def __init__(self):
        super(Crud, self).__init__()
        
        #Init dirctory hierarchy
        self.__fPaths = {'category': 'data/category/',
                            'data': 'data/',
                            'config': 'data/configuration/',
                            'test':'data/test/'}
        self.__fnames = {}

    def setPath(self, dir):
        self._setPath(dir)

    def defaultFile(self):
        '''file containing data'''
        return self.__dir('category', 'data')
    
    def testFile(self):
        return self.__dir('test', 'test')

    def evalStrData(self, data):
        '''Evaluate a str collection. Return new collection'''
        data = data[0]
        newData = {}
        for index, category in enumerate(data):
            newData[category] = ast.literal_eval(data[category])
        return newData

    def __dir(self, path, filename):
        '''Create dir using path and filename'''
        fpath = self.__fPaths[path]
        fname = self.__fnames[filename]
        return fpath+fname
     


    
