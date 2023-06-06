
import ast
from create.Create import Create
from read.Read import Read
from update.Update import Update
from delete.Delete import Delete

class CRUD(Create, Read, Update, Delete):
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
        super(CRUD, self).__init__()
        
        #Init dirctory hierarchy
        self.__fPaths = {'category': 'data/category/',
                            'data': 'data/',
                            'config': 'data/configuration/',
                            'test':'data/test/'}
        self.__fnames = {}

    def defaultFile(self):
        '''file containing crypto data'''
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

        return None

    def __dir(self, path, filename):
        '''Create dir using path and filename'''
        fpath = self.__fPaths[path]
        fname = self.__fnames[filename]
        return fpath+fname
     


    
