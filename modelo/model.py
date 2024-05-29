
from modelo.undo_redo import UndoRedo

class Model:
    def __init__(self):
        self.input = []
        self.undo_redo = UndoRedo()

    def ingresar_char(self, char, simbolo = ""):
        if simbolo != "":
            self.input.append(simbolo)
        else:
            self.input.append(char)
        
        self.undo_redo.ingresar_char(char)

    def evaluacion_postfija(self):
        # self.input
        pass

    def recuperar_input(self):
        return ''.join(self.input)
        
    def calcular_resultado(self):
        return str(len(self.input))

    def deshacer(self):
        if not self.undo_redo.undo():
            return
        else:
            self.input.pop()

    def rehacer(self):
        redo = self.undo_redo.redo()
        if not redo:
            return
        else:
            self.input.append(redo)

    def borrar(self):
        if not self.input:
            return
        else:
            self.input.pop()
            self.undo_redo.undo()

    def limpiar(self):
        while self.input:
            self.borrar()
