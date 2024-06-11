
from modelo.undo_redo import *
from modelo.procesamiento_cadenas import *

class Model:
    def __init__(self):

        # inicializar la lista de caracteres interna
        self.input = ""
        
        # inicializar las pilas undo y redo
        self.undo_redo = UndoRedo()


    # gestionar el ingreso de un caracter
    def ingresar_char(self, char):

        # ingresar caracter a la cadena principal
        self.input += char

        # llama a la funcion de undo_redo
        self.undo_redo.ingresar_char(char)


    # recuperar la cadena interna principal
    def recuperar_input(self):

        # devolver la cadena principal
        return self.input
        

    # gestor del calculo del resultado
    def calcular_resultado(self):

        # caso esté vacia la cadena interna
        if self.expresion_principal_esta_vacia():
            
            return "0"
        
        # recuperar la cadena interna
        cadena = self.recuperar_input()
        
        ''' GESTION DE ERRORES '''
        # Caso los parentesis retorne False -> o sea esten mal
        if not verificar_parentesis(cadena):

            # devolver error
            return "SYNTAX E."

        # convertir la cadena de not. infija a not. postfija 
        postfijo = infijoPostfija(cadena)
        
        # Caso la expresion en postfijo retorne False y la cadena no sea vacia
        if not postfijo and self.input:

            # devolver error
            return "SYNTAX E."

        # tratar de evaluar la evaluacion_postfija
        try:
            # devolver el resultado de la evaluación
            return eval_postfija(postfijo)

        # si ocurre algun error
        except: 

            # devolver error
            return "SYNTAX E."


    # gestor de la opcion de deshacer
    def deshacer(self):

        # sacar el tope de la pila undo
        x = self.undo_redo.undo()

        # si la accion fue de borrar
        if x == "borrar":

            # se busca el numero mas cercano en la pila
            i = -1
            while self.undo_redo.pila_undo[i] == "borrar":
                i -= 1

            # ese numero se recupera y se añade a la cadena principal
            self.input += self.undo_redo.pila_undo[i * 2 + 1]
    
        # si la accion fue limpiar
        elif x == "limpiar":

            # se recupera toda la cadena
            cadena = self.undo_redo.pila_undo.pop()

            # se inserta en la penultima posicion de la pila_redo
            self.undo_redo.pila_redo.insert(-1, cadena)
            
            # se reestablece la cadena
            self.input = cadena

        # caso contrario -> fue un numero y simplemente se elimina el ultimo caracter de la cadena principal
        else:
            self.input = self.input[:-1]
        

    # gestor de la opcion de deshacer
    def rehacer(self):

        # sacar el tope de la pila redo
        x = self.undo_redo.redo()

        # si la accion fue borrar
        if x == "borrar":

            # se debe rehacer la accion -> realizarla denuevo
            self.input = self.input[:-1]

        # si la accion fue limpiar
        elif x == "limpiar":

            # se debe rehacer la accion -> realizarla denuevo
            self.input = ""
            
            # se debe recuperar toda la cadena
            cadena = self.undo_redo.pila_redo.pop()
            # guardarla en la pila undo
            self.undo_redo.pila_undo.insert(-1, cadena)

        # caso contrario -> fue un numero y simplemente se agrega el caracter de la pila en la cadena principal
        else:

            self.input += x     


    # gestor de la opcion de deshacer
    def borrar(self):
        
        # si la cadena principal esta vacia no realizar nada
        if self.expresion_principal_esta_vacia():
            return

        # borrar el ultimo elemento en la cadena principal
        self.input = self.input[:-1]
        # indicar a la pila_undo que se realizo una accion borrar 
        self.undo_redo.pila_undo.append("borrar")


    # gestor de la opcion de deshacer
    def limpiar(self):

        # si la cadena principal esta vacia no realizar nada
        if self.expresion_principal_esta_vacia():
            return


        # recuperar la cadena principal
        cadena_antigua = self.input

        # guardar el estado del programa en pila_undo
        self.undo_redo.pila_undo.append(cadena_antigua)
        self.undo_redo.pila_undo.append("limpiar")

        # limpiar la cadena principal
        self.input = ""
        
   
    # gestor de la opcion de deshacer
    def expresion_principal_esta_vacia(self):

        return self.input == ""