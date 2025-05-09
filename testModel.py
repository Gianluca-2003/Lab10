from model.Country import Country
from model.model import Model

myModel = Model()

myModel.buildGraph()


print(f"Numero di nodi: {myModel.getNumNodes} e archi: {myModel.getNumEdges}")


visitati = myModel.visita_iterativa(Country("USA",2,	"United States of America"))
lista = []
for v in visitati:
    lista.append(v)
print(lista)
print(len(lista))

