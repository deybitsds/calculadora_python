
class UndoRedo:
    def __init__(self):

        # Inicializar pilas vacias
        self.pila_undo = []
        self.pila_redo = []

    
    # funcion para gestionar el ingreso de un char
    def ingresar_char(self, char):

        # ingresar a pila undo
        self.pila_undo.append(char)
        
        # limpiar pila redo
        self.pila_redo = []

    
    # funcion para retirar el top de pila_undo y colocarlo en pila_redo
    def undo(self):

        # si no hay nada en la pila devolver cadena vacia
        if self.pila_undo_esta_vacia():
            return ""

        # retirar top pila_undo y colocarlo en pila_redo
        x = self.pila_undo.pop()
        self.pila_redo.append(x)

        # devuelve el elemento desplazado
        return x

    
    # funcion para retirar el top de pila_redo y colocarlo en pila_undo
    def redo(self):

        # si no hay nada en la pila devolver cadena vacia
        if self.pila_redo_esta_vacia():
            return ""


        # retirar top pila_redo y colocarlo en pila_undo
        x = self.pila_redo.pop()
        self.pila_undo.append(x)

        # devuelve el elemento desplazado
        return x
    
    
    # funcion que devuelve el estado de la pila_undo
    def pila_undo_esta_vacia(self):
        
        return not self.pila_undo
    
    
    # funcion que devuelve el estado de la pila_redo
    def pila_redo_esta_vacia(self):

        return not self.pila_redo