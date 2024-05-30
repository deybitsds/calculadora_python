
class UndoRedo:
        
    def __init__(self):
        self.Undo = []
        self.Redo = []

    def ingresar_char(self, char):
        self.Undo.append(char)
        self.Redo = []

    def undo(self, elemento = ""):
        if elemento != "":
            print(elemento)
            self.Undo.append(elemento)
            return True

        if (self.Undo):
            x = self.Undo.pop()
            self.Redo.append(x)
            return True
        else:
            #print("undo: (pila Undo vacía)")
            return False
    
    def redo(self):
        if (self.Redo):
            x = self.Redo.pop()
            self.Undo.append(x)
            return x
        else:
            # print("redo: (pila Redo vacía)")
            return False
        
    def recuperar_cadena(self):
        cadena_actual = ""
        for k in range(len(self.Undo)):
            cadena_actual += self.Undo[k]
        return cadena_actual


