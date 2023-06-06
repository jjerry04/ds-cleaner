from util.IO import IO

class Delete(IO):

    '''
        Delete file in directory
        *delete folder directory
        *Account for missing file
        *account for missing folder
    '''

    def __init__(self):
        super(Delete, self).__init__()

    def deleteData(self, data, start = 'top'):
        '''Delete single row containing data.
        Delete first data on top'''

        if start == 'top':
            #look in data
            return self.__delete(data)
        else:
            return self.__deleteFromBtm(data)

    def deleteRange(self, data, start, end):
        '''Delete data in range. 2 - 5. Delete data
        between 2,5 inclusive'''

        while int(start) < int(end):
                try: 
                    if len(data) < end:
                        end = len(data)
                        print(f'Improper range - rang adjusted to {start} - {end}')
                    elif start > len(data):
                        return data
                    else:
                        del data[start]
                        end -= 1
                except IndexError:
                    pass
        return data

    def delete(self, data):
        '''Clear entire data. If not empty'''
        if len(data) != 0:
            data.clear()
        return data

    def __delete(self, data):
        for index, asset in enumerate(data):
                name = asset['name']
                if index == 0:
                    print(f'{name} deleted.')
                    del data[index]
                    return data

    def __deleteFromBtm(self, data):
        for index, asset in enumerate(data):
                name = asset['name']
                if index == len(data) -1:
                    print(f'{name} - deleted.')
                    del data[index]
                    return data
        #delete first item in data
        #return new data w/out first item

    