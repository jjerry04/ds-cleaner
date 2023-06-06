
from util.IO import IO

class Read(IO):
    '''
    Get location of file and read data from file
    '''
    def __init__(self):
        super(Read, self).__init__()

    def read(self, filename = '', totalData = 0):
        '''Look through directories to find file
            with corresponding name. Set total rows to read
            in file
        '''
        self._setPath(filename)
        self._setCode('r')
        self._setDataRange(totalData)

        try:
            self._safeRead()
        except (FileNotFoundError, FileExistsError):
            self._initFolder()
            return None
           # self._safeCreate()

        return self._getData()

    def getFileData(self):
        return self._getData()