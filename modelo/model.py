
# from modelo.undo_redo import UndoRedo
# from modelo.procesamiento_cadenas import *

from modelo.undo_redo import *
from modelo.procesamiento_cadenas import *

class Model:
    def __init__(self):
        # inicializar la lista de caracteres interna
        self.input = ""
        # inicializar las pilas undo y redo
        self.undo_redo = UndoRedo()
        self.ultima_accion = ""

    # gestionar el ingreso de un caracter
    def ingresar_char(self, char):
        # 
        self.input += char
        self.undo_redo.ingresar_char(char)

        print(self.undo_redo.pila_undo)
        print(self.undo_redo.pila_redo)


    # recuperar la expresion | cadena -> input
    def recuperar_input(self):
        # concatenar cadena interna caracteres 
        return self.input
        
    # 
    def calcular_resultado(self):
        # caso este vacio la cadena interna
        if self.expresion_principal_esta_vacia():
            return "0"
        
        # transformar la lista en una cadena
        cadena = self.recuperar_input()
        
        ''' GESTION DE ERRORES '''
        # Caso los parentesis retorne False -> o sea esten mal
        if not verificar_parentesis(cadena):
            return "SYNTAX E."

        infijo = self.recuperar_input()
        postfijo = infijoPostfija(infijo)
        
        # Caso la expresion en postfijo retorne False -> o sea este mal
        if not postfijo and self.input:
            print(self.input)
            return "SYNTAX E."

        # tratar de evaluar la evaluacion_postfija
        try:
            # caso ocurra un error matematico
            return eval_postfija(postfijo)

        except: 
            # caso ocurra un error de sintaxis
            return "SYNTAX E."

    ''' RESOLVER '''
    def deshacer(self):

        x = self.undo_redo.undo2()

        if x == "borrar":

            i = -1

            while self.undo_redo.pila_undo[i] == "borrar":
                i -= 1

            self.input += self.undo_redo.pila_undo[i*2+1]
    
        elif x == "limpiar":

            cadena = self.undo_redo.pila_undo.pop()
            self.undo_redo.pila_redo.insert(-1, cadena)
            self.input = cadena

        else:
            self.input = self.input[:-1]
        
        print()
        print(self.undo_redo.pila_undo)
        print(self.undo_redo.pila_redo)
        print()

    ''' RESOLVER '''
    def rehacer(self):

        x = self.undo_redo.redo2()

        if x == "borrar":

            self.input = self.input[:-1]

        elif x == "limpiar":

            self.input = ""

            cadena = self.undo_redo.pila_redo.pop()

            self.undo_redo.pila_undo.insert(-1, cadena)

        else:

            self.input += x     

        print()
        print(self.undo_redo.pila_undo)
        print(self.undo_redo.pila_redo)
        print()

    def borrar(self):
        # verificar que haya algo que borrar
        if self.expresion_principal_esta_vacia():
            # no hacer nada -> ignorar peticion
            return

        # caso haya algo
        self.input = self.input[:-1] 
        self.undo_redo.pila_undo.append("borrar")

        print()
        print(self.undo_redo.pila_undo)
        print(self.undo_redo.pila_redo)
        print()


    def limpiar(self):

        if self.expresion_principal_esta_vacia():
            return

        cadena_antigua = self.input
        self.undo_redo.pila_undo.append(cadena_antigua)
        self.undo_redo.pila_undo.append("limpiar")

        self.input = ""
        
    def expresion_principal_esta_vacia(self):
        return self.input == ""