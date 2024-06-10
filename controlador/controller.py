
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
        return self.model.recuperar_input()

    # ingresar caracter en el modelo
    def ingresar_char(self, char):
        #
        self.model.ingresar_char(char)
        # actualizar la caja de texto input
        self.view.actualizar_input()
 
    def ingresar_siguiente_caracter(self, caracter_apertura, caracter_cierre):
        #
        input_actual = self.model.recuperar_input()
        # recuperar caracter correspondiente
        caracter = determinar_siguiente_caracter(input_actual, caracter_apertura, caracter_cierre)
        #
        self.ingresar_char(caracter)

    def mostrar_resultado(self):
        # calcular resultado 
        resultado_original = self.model.calcular_resultado()
        print(resultado_original)
        
        # gestionar los errores
        if not contiene_numeros(str(resultado_original)):
            self.view.mostrar_resultado(resultado_original)
            return     
        
        # comprobar que el numero sea entero
        resultado_original = float(resultado_original)
        resultado_entero = int(resultado_original)


        # caso sea convertible a entero
        if resultado_original == resultado_entero:
            # 
            self.view.mostrar_resultado(str(resultado_entero))
        else:
            # caso sea flotante redondear a 7 numeros despues de la coma decimal
            self.view.mostrar_resultado(str(round(resultado_original, 7)))

    def borrar(self):
        #
        self.model.borrar()
        # actualizar la caja de texto input
        self.view.actualizar_input()

    def undo(self):
        #
        self.model.deshacer()
        # actualizar la caja de texto input
        self.view.actualizar_input()

    def redo(self):
        # 
        self.model.rehacer()
        # actualizar la caja de texto input
        self.view.actualizar_input()

    def limpiar(self):
        # borrar la cadena en el modelo
        self.model.limpiar()
        # actualizar la caja de texto input
        self.view.actualizar_input()
        # borrar la caja de texto output
        self.view.limpiar()

    def gestion_botones(self):
        
        # conexion de los botones con las funciones correspondientes
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

        self.view.ui.bt_sum.clicked.connect(lambda:self.ingresar_char("+"))
        self.view.ui.bt_dif.clicked.connect(lambda:self.ingresar_char("-"))
        self.view.ui.bt_mul.clicked.connect(lambda:self.ingresar_char("*"))
        self.view.ui.bt_div.clicked.connect(lambda:self.ingresar_char("/"))
        self.view.ui.bt_pow.clicked.connect(lambda:self.ingresar_char("^")) # <------

        self.view.ui.bt_parentesis.clicked.connect(lambda:self.ingresar_char("(")) # <------
        self.view.ui.bt_parentesis2.clicked.connect(lambda:self.ingresar_char(")"))
        self.view.ui.bt_parentesis_completo.clicked.connect(lambda:self.ingresar_siguiente_caracter("(", ")"))
        
        self.view.ui.bt_llaves.clicked.connect(lambda:self.ingresar_char("{")) # <------
        self.view.ui.bt_llaves2.clicked.connect(lambda:self.ingresar_char("}"))
        self.view.ui.bt_llaves_completo.clicked.connect(lambda:self.ingresar_siguiente_caracter("{", "}"))
        
        self.view.ui.bt_corchetes.clicked.connect(lambda:self.ingresar_char("[")) # <------
        self.view.ui.bt_corchetes2.clicked.connect(lambda:self.ingresar_char("]"))
        self.view.ui.bt_corchetes_completo.clicked.connect(lambda:self.ingresar_siguiente_caracter("[", "]"))

        self.view.ui.bt_borrar.clicked.connect(self.borrar)
        self.view.ui.bt_limpiar.clicked.connect(self.limpiar)
        self.view.ui.bt_deshacer.clicked.connect(self.undo)
        self.view.ui.bt_rehacer.clicked.connect(self.redo)

        self.view.ui.bt_resul.clicked.connect(self.mostrar_resultado)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    control = Controller()
    sys.exit(app.exec_())	