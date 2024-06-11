
from vista.view import *
from modelo.model import *

class Controller:
    
    def __init__(self):
    
        # instancia View
        self.view = View(self)
        # instancia Model
        self.model = Model()

        # gestionar los botones
        self.gestion_botones()

    
    
    # recuperar cadena del modelo
    def recuperar_input(self):
    
        # devolvemos la cadena principal del modelo
        return self.model.recuperar_input()

    
    
    # ingresar caracter en el modelo
    def ingresar_char(self, char):
    
        # ingresamos el caracter a la cadena del modelo
        self.model.ingresar_char(char)
        
        # actualizar la caja de texto input
        self.view.actualizar_input()
 

    
    # gestor del boton de prediccion de caracter
    def ingresar_siguiente_caracter(self, caracter_apertura, caracter_cierre):
    
        # recuperamos la cadena principal
        input_actual = self.model.recuperar_input()
        
        # determinar el caracter predecido
        caracter = determinar_siguiente_caracter(input_actual, caracter_apertura, caracter_cierre)
        
        # ingresar en el caracter determinado
        self.ingresar_char(caracter)


    
    # gestor del boton de resultado
    def mostrar_resultado(self):
        
        # calcular resultado 
        resultado_original = self.model.calcular_resultado()
        
        # gestionar los errores -> error
        if not contiene_numeros(str(resultado_original)):
            self.view.mostrar_resultado(resultado_original)
            return     
        
        # comprobar que el numero sea entero
        resultado_original = float(resultado_original)
        resultado_entero = int(resultado_original)


        # caso sea convertible a entero
        if resultado_original == resultado_entero:
            # devolver el resultado como texto 
            self.view.mostrar_resultado(str(resultado_entero))
            
        else:
            # caso sea flotante : redondear a 7 numeros despues de la coma decimal
            self.view.mostrar_resultado(str(round(resultado_original, 7)))


    
    # gestor boton borrar
    def borrar(self):
    
        # llama a la funcion del modelo
        self.model.borrar()

        # actualizar la caja de texto input
        self.view.actualizar_input()


    
    # gestor boton undo
    def undo(self):


        # llama a la funcion del modelo
        self.model.deshacer()
        
        # actualizar la caja de texto input
        self.view.actualizar_input()


    
    # gestor boton redo
    def redo(self):

        # llama a la funcion del modelo
        self.model.rehacer()

        # actualizar la caja de texto input
        self.view.actualizar_input()


    
    # gestor boton limpiar
    def limpiar(self):

        # llama a la funcion del modelo
        self.model.limpiar()

        # actualizar las cajas de texto
        self.view.actualizar_input()
        self.view.limpiar()


    
    # gestor de todos los botones
    def gestion_botones(self):

        # conexion de los botones numericos
        self.view.ui.bt_0.clicked.connect(lambda:self.ingresar_char("0"))
        self.view.ui.bt_1.clicked.connect(lambda:self.ingresar_char("1"))
        self.view.ui.bt_2.clicked.connect(lambda:self.ingresar_char("2"))
        self.view.ui.bt_3.clicked.connect(lambda:self.ingresar_char("3"))
        self.view.ui.bt_4.clicked.connect(lambda:self.ingresar_char("4"))
        self.view.ui.bt_5.clicked.connect(lambda:self.ingresar_char("5"))
        self.view.ui.bt_6.clicked.connect(lambda:self.ingresar_char("6"))
        self.view.ui.bt_7.clicked.connect(lambda:self.ingresar_char("7"))
        self.view.ui.bt_8.clicked.connect(lambda:self.ingresar_char("8"))
        self.view.ui.bt_9.clicked.connect(lambda:self.ingresar_char("9"))
        self.view.ui.bt_punto.clicked.connect(lambda:self.ingresar_char("."))

        # conexion de los botones operacion
        self.view.ui.bt_sum.clicked.connect(lambda:self.ingresar_char("+"))
        self.view.ui.bt_dif.clicked.connect(lambda:self.ingresar_char("-"))
        self.view.ui.bt_mul.clicked.connect(lambda:self.ingresar_char("*"))
        self.view.ui.bt_div.clicked.connect(lambda:self.ingresar_char("/"))
        self.view.ui.bt_pow.clicked.connect(lambda:self.ingresar_char("^")) 

        # conexion de los botones de parentesis
        self.view.ui.bt_parentesis.clicked.connect(lambda:self.ingresar_char("(")) 
        self.view.ui.bt_parentesis2.clicked.connect(lambda:self.ingresar_char(")"))
        self.view.ui.bt_parentesis_completo.clicked.connect(lambda:self.ingresar_siguiente_caracter("(", ")"))
        
        # conexion de los botones de llaves
        self.view.ui.bt_llaves.clicked.connect(lambda:self.ingresar_char("{")) 
        self.view.ui.bt_llaves2.clicked.connect(lambda:self.ingresar_char("}"))
        self.view.ui.bt_llaves_completo.clicked.connect(lambda:self.ingresar_siguiente_caracter("{", "}"))
        
        # conexion de los botones de corchetes
        self.view.ui.bt_corchetes.clicked.connect(lambda:self.ingresar_char("[")) 
        self.view.ui.bt_corchetes2.clicked.connect(lambda:self.ingresar_char("]"))
        self.view.ui.bt_corchetes_completo.clicked.connect(lambda:self.ingresar_siguiente_caracter("[", "]"))

        # conexion de los botones de manejo de la cadena
        self.view.ui.bt_borrar.clicked.connect(self.borrar)
        self.view.ui.bt_limpiar.clicked.connect(self.limpiar)
        self.view.ui.bt_deshacer.clicked.connect(self.undo)
        self.view.ui.bt_rehacer.clicked.connect(self.redo)

        # conexion del boton del resultado
        self.view.ui.bt_resul.clicked.connect(self.mostrar_resultado)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    control = Controller()
    sys.exit(app.exec_())	