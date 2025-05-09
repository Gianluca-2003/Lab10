from database.DAO import DAO
from model.model import Model

my_model = Model()
edges = DAO.getAllEdges(my_model._idMap,1820)
for arco in edges:
    print(arco)