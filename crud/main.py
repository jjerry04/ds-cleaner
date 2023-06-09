from dscleaner.crud.Crud import Crud

crud = Crud()
dir = "Data/"
crud.createFolder(dir)

filename = dir+'/dsc_testData.csv'
testData = {"name": 'Jonathan', 'age':'26', 'height':5.8, 'location':'Az'}
testData = testData.items()
field = ['name', 'age', 'height', 'location']

crud.createFile(filename=filename,field = field, data = testData, header = True)
open = crud.Read(filename, directory)


#Open csv file by reading