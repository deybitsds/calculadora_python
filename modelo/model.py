
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
        print(self.undo_redo.Undo)
        print(self.undo_redo.Redo)
        print("input -> ", self.input)
        
        if not self.undo_redo.undo():
            return
        else:
            if self.input:
                self.input.pop()

    def rehacer(self):
        redo = self.undo_redo.redo()
        if not redo:
            return
        else:
            self.input.append(redo)
        
        print(self.undo_redo.Undo)
        print(self.undo_redo.Redo)

    def borrar(self):
        if not self.input:
            return
        else:
            self.input.pop()
            self.undo_redo.undo()

    def limpiar(self):
        input = self.recuperar_input()
        self.input = []
        self.undo_redo.undo(input)
        print(self.undo_redo.Undo)
        print(self.undo_redo.Redo)