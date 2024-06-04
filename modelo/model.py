
from modelo.undo_redo import UndoRedo
from modelo.procesamiento_cadenas import *

class Model:
    def __init__(self):
        self.input = []
        self.undo_redo = UndoRedo()

    def ingresar_char(self, char, simbolo = ""):

        self.input.append(char)
        self.undo_redo.ingresar_char(char)

    def recuperar_input(self):
        return ''.join(self.input)
        
    def calcular_resultado(self):
        if not self.input:
            return "0.0"
        cadena = self.recuperar_input()
        if not verificar_parentesis(cadena):
            return "SYNTAX E."

        infijo = self.input
        postfijo = infijoPostfija(infijo)
        
        if not postfijo and self.input:
            return "SYNTAX E."

        try:
            if not eval_postfija(postfijo):
                return "MATH E."
        except IndexError as e: 
            return "SYNTAX E."

        return eval_postfija(postfijo)

    def deshacer(self):

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
        self.input = []
        self.undo_redo.Undo = []
        self.undo_redo.Redo = []
