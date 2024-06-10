
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

    # funcion para gestionar la insutrccion undo
    def undo(self, elemento = ""):
        # Si existe el elemento
        if elemento != "":
            # Agregar el elemento a la lista de deshacer (pila_undo)
            self.pila_undo.append(elemento)
            return True
        
        # Realizar la operación de deshacer
        if self.pila_undo:
            # Obtener el último elemento de la lista de deshacer (pila_undo)
            x = self.pila_undo.pop()
            # Agregar el elemento a la lista de rehacer (pila_redo)
            self.pila_redo.append(x)
            return True
        
        # Si no hay elementos para deshacer, retornar False
        return False

    def undo2(self):

        if self.pila_undo_esta_vacia():
            return ""

        x = self.pila_undo.pop()
        self.pila_redo.append(x)

        return x

    def redo2(self):

        if self.pila_redo_esta_vacia():
            return ""

        x = self.pila_redo.pop()
        self.pila_undo.append(x)

        return x
    
    def redo(self):

        if self.pila_redo_esta_vacia():

            return ""

        # Si la lista de rehacer (pila_redo) no está vacía
        if self.pila_redo:
            # Obtener y eliminar el último elemento de la lista de rehacer (pila_redo)
            x = self.pila_redo.pop()
            # Agregar el elemento a la lista de deshacer (pila_undo)
            self.pila_undo.append(x)
            # Retornar el elemento que se rehizo
            return x
        
        # Si la lista de rehacer (pila_redo) está vacía, retornar False
        return False

    def pila_undo_esta_vacia(self):
        return not self.pila_undo
    
    def pila_redo_esta_vacia(self):
        return not self.pila_redo
