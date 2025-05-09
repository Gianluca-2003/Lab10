from model.Country import Country
from model.model import Model

myModel = Model()

myModel.buildGraph()


print(f"Numero di nodi: {myModel.getNumNodes} e archi: {myModel.getNumEdges}")


myModel.cercaNodiConnessiBFS(Country("USA",2,	"United States of America"))
