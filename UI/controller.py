import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._stato = None

    def handleCalcola(self, e):
        annoInput = self._view._txtAnno.value
        if annoInput == "":
            self._view._txt_result.controls.clear()
            self._view.create_alert("Devi inserire un anno per procedere")
            return
        try:
            anno_int = int(annoInput)
        except ValueError:
            self._view._txt_result.controls.clear()
            self._view.create_alert("Devi inserire un anno per procedere")
            return
        self._view._txt_result.controls.clear()
        self._model.setAnno(anno_int)
        self._model.buildGraph()
        self._view._txt_result.controls.append(ft.Text("Grafo creato correttamnete"))
        self._view._txt_result.controls.append(ft.Text(f"Numero di nodi: {self._model.getNumNodes} "
                                                       f"Numero di archi: {self._model.getNumEdges}"))

        self._view._txt_result.controls.append(ft.Text(f"Il grafo ha "
                                                       f"{self._model.calcolaNumeroComponentiConnesse()}"
                                                       f" componenti connesse"))

        self._view._txt_result.controls.append(ft.Text("Di seguito le il dettaglio sui nodi"))

        nodes = self._model.getNodes
        for node in nodes:
            self._view._txt_result.controls.append(ft.Text(f"{node} -- "
                                                           f" {self._model.cacolaGradoDiUnNodo(node)} vicini"))

        self._view._ddStato.disabled = False
        self._view._btnRaggiungi.disabled = False
        self.fillDDStati()

        self._view.update_page()


    def handleRaggiungi(self, e):
        self._view._txt_result.controls.clear()
        if self._stato is None:
            self._view._txt_result.controls.clear()
            self._view.create_alert("Scegli uno Stato per procedere")
            return

        nodi_esplorati = self._model.cercaNodiConnessiBFS(self._stato)

        if nodi_esplorati is None:
            self._view._txt_result.controls.clear()
            self._view._txt_result.controls.append(ft.Text(f"Lo stato {self._stato} è un nodo isolato"))
        else:
            self._view._txt_result.controls.append(ft.Text(f"Lo stato {self._stato} è collegato a: "))
            for nodo in nodi_esplorati:
                self._view._txt_result.controls.append(ft.Text(nodo))

        self._view.update_page()


    def handleReadSato(self, e):
        self._stato = e.control.data


    def fillDDStati(self):
        stati = self._model.getNodes
        self._view._ddStato.options.clear()
        for stato in stati:
            self._view._ddStato.options.append(ft.dropdown.Option(text=stato.StateNme,
                                                                  data=stato,
                                                                  on_click=self.handleReadSato))






