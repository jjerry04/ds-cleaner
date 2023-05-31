

from .create.Create import Create
from .delete.Delete import Delete
from .read.Read import Read
from .update.Update import Update

class Crud(Create, Delete, Read, Update):

    def __init__(self):
        pass
