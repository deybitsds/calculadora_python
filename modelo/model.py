
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
        # añadir char a undo_redo
        self.undo_redo.ingresar_char(char)
        self.ultima_accion = "añadir"

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

        if self.ultima_accion == "borrar":
            self.input += self.undo_redo.redo()
            return 

        if self.ultima_accion == "limpiar":
            
            return
        
        # caso no haya nada en la pila undo o no haya cadena ingresada
        if self.expresion_principal_esta_vacia():
            # no hacer nada -> ignorar peticion
            return

        # caso base
        self.undo_redo.undo2()
        self.input = self.input[:-1]
        self.ultima_accion = "deshacer"
    
    ''' RESOLVER '''
    def rehacer(self):
        # recuperar la listra de redos
        redo = self.undo_redo.redo()
        # caso no haya algun elemento que se pueda "rehacer"
        if not redo:
            # no hacer nada -> ignorar peticion
            return 

        if self.ultima_accion == "limpiar":
            # self.undo_redo.
            pass

        # caso contrario quitar la lista de redo
        self.input += redo

    def borrar(self):
        # verificar que haya algo que borrar
        if self.expresion_principal_esta_vacia():
            # no hacer nada -> ignorar peticion
            return

        # caso haya algo
        self.input = self.input[:-1] 
        self.undo_redo.undo2() 
        self.ultima_accion = "borrar"

    ''' RESOLVER '''
    def limpiar(self):
        # limpiar todo
        self.input = ""
        self.undo_redo.Undo = []
        self.undo_redo.Redo = []

    def expresion_principal_esta_vacia(self):
        return self.input == ""