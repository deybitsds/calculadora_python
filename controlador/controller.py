
from vista.view import *
from modelo.model import *

class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model()

        self.gestion_botones()

    def recuperar_input(self):
        return self.model.recuperar_input()

    def gestion_botones(self):
        
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
        self.view.ui.bt_mul.clicked.connect(lambda:self.ingresar_char("*", "x"))
        self.view.ui.bt_div.clicked.connect(lambda:self.ingresar_char("/"))
        self.view.ui.bt_pow.clicked.connect(lambda:self.ingresar_char("^"))

        self.view.ui.bt_parentesis.clicked.connect(self.ingresar_parentesis)
        self.view.ui.bt_parentesis2.clicked.connect(lambda:self.ingresar_char(")"))
        self.view.ui.bt_llaves.clicked.connect(self.ingresar_llaves)
        self.view.ui.bt_llaves2.clicked.connect(lambda:self.ingresar_char("}"))
        self.view.ui.bt_corchetes.clicked.connect(self.ingresar_corchetes)
        # self.view.ui.bt_corchetes2.clicked.connect(lambda:self.ingresar_char(""))

        self.view.ui.bt_borrar.clicked.connect(self.borrar)
        self.view.ui.bt_limpiar.clicked.connect(self.limpiar)
        self.view.ui.bt_deshacer.clicked.connect(self.undo)
        self.view.ui.bt_rehacer.clicked.connect(self.redo)

        self.view.ui.bt_resul.clicked.connect(self.mostrar_resultado)

    def ingresar_char(self, char, simbolo = ""):
        if simbolo == "":
            simbolo = char

        self.model.ingresar_char(char, simbolo)
        self.view.actualizar_input()
 
    def ingresar_parentesis(self):
        input_actual = self.model.recuperar_input()
        caracter = recuperar_parentesis_correspondientes(input_actual)
        self.ingresar_char(caracter)

    def ingresar_llaves(self):
        input_actual = self.model.recuperar_input()
        caracter = recuperar_llaves_correspondientes(input_actual)
        self.ingresar_char(caracter)     

    def ingresar_corchetes(self):
        input_actual = self.model.recuperar_input()
        caracter = recuperar_corchetes_correspondientes(input_actual)
        self.ingresar_char(caracter)     

    def mostrar_resultado(self):
        resultado_original = self.model.calcular_resultado()
        resultado_entero = int(resultado)

        if resultado_original == resultado_entero:
            self.view.mostrar_resultado(str(int(resultado)))
        else:
            self.view.mostrar_resultado(str(round(resultado,7)))

    def borrar(self):
        self.model.borrar()
        self.view.actualizar_input()

    def undo(self):
        self.model.deshacer()
        self.view.actualizar_input()

    def redo(self):
        self.model.rehacer()
        self.view.actualizar_input()

    def limpiar(self):
        self.model.limpiar()
        self.view.actualizar_input()
        self.view.limpiar()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    control = Controller()
    sys.exit(app.exec_())	