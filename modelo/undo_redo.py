
class UndoRedo:
        
    def __init__(self):
        # Inicializar pilas vacias
        self.Undo = []
        self.Redo = []

    # funcion para gestionar el ingreso de un char
    def ingresar_char(self, char):
        # ingresar a pila undo
        self.Undo.append(char)
        # limpiar pila redo
        self.Redo = []

    # funcion para gestionar la insutrccion undo
    def undo(self, elemento = ""):
        # Si existe el elemento
        if elemento != "":
            # Agregar el elemento a la lista de deshacer (Undo)
            self.Undo.append(elemento)
            return True
        
        # Realizar la operación de deshacer
        if self.Undo:
            # Obtener el último elemento de la lista de deshacer (Undo)
            x = self.Undo.pop()
            # Agregar el elemento a la lista de rehacer (Redo)
            self.Redo.append(x)
            return True
        
        # Si no hay elementos para deshacer, retornar False
        return False

    def undo2(self):

        if not self.Undo:
            return False

        x = self.Undo.pop()
        self.Redo.append(x)
        return True

    
    def redo(self):
        # Si la lista de rehacer (Redo) no está vacía
        if self.Redo:
            # Obtener y eliminar el último elemento de la lista de rehacer (Redo)
            x = self.Redo.pop()
            # Agregar el elemento a la lista de deshacer (Undo)
            self.Undo.append(x)
            # Retornar el elemento que se rehizo
            return x
        
        # Si la lista de rehacer (Redo) está vacía, retornar False
        return False
