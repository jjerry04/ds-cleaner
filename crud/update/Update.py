
from util.IO import IO



class Update(IO):
    '''
        Update data by adding new data to old data.
        *Add new data to end
        *Overwrite old data with new data
        *overwrite specific data
    '''

    __updatedData = []

    def __init__(self):
        super(Update, self).__init__()
         
    def update(self, filename, data):
        '''Write new changes of data to file'''
        self._setIOProperty('w',filename, data, True)
        try:
            self._safeCreate()
        except FileNotFoundError:
            self._initFolder()
            self._safeCreate()
        print(f'\n{filename} has been updated!')
    
    def addData(self, filename, newData, oldData):
        '''Add data by copying old data that is not the same
        as the new data. Combine both into new data and 
        write to file. Old data that are the same, are overwritten'''
        #newRecord = []

        #copy new data into newRecord
        newRecord = self._appendData(self.__updatedData, newData)

        #Prevent unsimilar data from being overwritten
        for index, key in enumerate(newRecord):
            asset = key['name']
            #Does data exist in old record
            if self._exist(asset, oldData):
                print(f'{asset} exist in oldRecord. {asset} will not copy.')
            else:
                print(f'{asset} copied from old record to new record')
        
        newRecord =self._appendData(self.__updatedData, newRecord)
        self.update(filename, newRecord)

    def addDataByName(self, filename, name, newData, oldData):
        '''
            Get a new data. Add new data into old records.
            Old record is copied and overwritten,
            execept if new data that is the same as the 
            data in old records. 
        '''
        name = self.lowerCase(name)
        newRecord = []
        print(f'Searching for {name}')
        data = self._search(name, newData)
        newRecord.append(data)
        exist = self.exist(name, newRecord)

        #If name data does not exist in new record
        if exist is False:
            print(f'{name} does not exist - {exist}')
            print(f'Old record will not change')
        else:
            print(f'\nCopying old record')
            newRecord = self.copyData(name, oldData, newRecord)
            print(f'\n-New record ready to overwrite old record')
            self.update(filename, newRecord)
            print(f'Total asset: {self._dataCounter(newRecord) + 1} in new record')
        
    def _exist(self, name, data):
        '''Loop through data and see if specific data exist'''
        exist = False
        
        for index, key in enumerate(data):
            try:
                assetName = self.lowerCase(key['name'])
                name = self.lowerCase(name)
                if assetName == name:
                    exist = True
                    del data[index]
                    self.__updatedData = data
                    return exist
            except TypeError:
                 return exist
        return exist

    def copyData(self, name, data, newRecord = []):
        '''
            Copy all data in new list, except given data. Return new list
        '''
        for index, key in enumerate(data):
            assetName = self.lowerCase(key['name'])
            #check if chosen data exist in old record
            if assetName == name:
                print(f'{name} exist in old record and will be overwritten')
            else:
                #print(f'{name} - does not exist in old record')
                newRecord.append(key)
                print(f'{assetName} - copied from old record and added to New record')
        return newRecord
   
    def lowerCase(self, text):
        return text.lower()

    

    