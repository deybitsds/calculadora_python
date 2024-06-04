
from modelo.undo_redo import UndoRedo
from modelo.procesamiento_cadenas import *

class Model:
    def __init__(self):
        # inicializar la lista de caracteres interna
        self.input = []
        # inicializar las pilas undo y redo
        self.undo_redo = UndoRedo()

    # gestionar el ingreso de un caracter
    def ingresar_char(self, char):
        # 
        self.input.append(char)
        # añadir char a undo_redo
        self.undo_redo.ingresar_char(char)

    # 
    def recuperar_input(self):
        # concatenar lista interna caracteres 
        return ''.join(self.input)
        
    # 
    def calcular_resultado(self):
        # caso este vacio la lista interna
        if not self.input:
            return "0.0"
        
        # transformar la lista en una cadena
        cadena = self.recuperar_input()
        
        ''' GESTION DE ERRORES '''
        # Caso los parentesis retorne False -> o sea esten mal
        if not verificar_parentesis(cadena):
            return "SYNTAX E."

        infijo = self.input
        postfijo = infijoPostfija(infijo)
        
        # Caso la expresion en postfijo retorne False -> o sea este mal
        if not postfijo and self.input:
            return "SYNTAX E."

        # tratar de evaluar la evaluacion_postfija
        try:
            # caso ocurra un error matematico 
            if not eval_postfija(postfijo):
                return "MATH ERROR"

        except IndexError as e: 
            # caso ocurra un error de sintaxis
            return "SYNTAX E."

        # caso pase todas las "pruebas", devolver el numero
        return eval_postfija(postfijo)

    def deshacer(self):
        # caso no haya nada en la pila undo
        if not self.undo_redo.undo():
            # no hacer nada -> ignorar peticion
            return

        # caso si haya un elem en la pila
        if self.input:
            # quitar  el ultimo elemento de la lista interna
            self.input.pop()

    def rehacer(self):
        # recuperar la listra de redos
        redo = self.undo_redo.redo()
        # caso no haya algun elemento que se pueda "rehacer"
        if not redo:
            # no hacer nada -> ignorar peticion
            return

        # caso contrario quitar la lista de redo
        self.input.append(redo)

    def borrar(self):
        # verificar que haya algo que borrar
        if not self.input:
            # no hacer nada -> ignorar peticion
            return

        # caso haya algo
        self.input.pop() # quitar ultimo elem lista interna
        self.undo_redo.undo() # llamar a undo

    def limpiar(self):
        # limpiar todo
        self.input = []
        self.undo_redo.Undo = []
        self.undo_redo.Redo = []
